import sys
import wikipedia
import subprocess
import json
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
import re
import os


def fetch_wikipedia_summary(topic):
    try:
        # First try Wikipedia API
        search_results = wikipedia.search(topic)
        if not search_results:
            raise wikipedia.exceptions.PageError(topic)

        best_match = search_results[0]
        summary = wikipedia.summary(best_match, sentences=5)
        page = wikipedia.page(best_match)
        return summary, page.url
    except (wikipedia.exceptions.WikipediaException, wikipedia.exceptions.PageError) as e:
        print(f"\n⚠️ Wikipedia API error: {str(e)}")
        print("Using fallback description...")
        
        # Load existing context to check if a description has been made
        try:
            with open("context.json", "r") as f:
                existing_context = json.load(f)
                if existing_context.get("wikipedia", {}).get("summary"):
                    return existing_context["wikipedia"]["summary"], ""
        except (json.JSONDecodeError, FileNotFoundError):
            pass
            
        # Generate a topic-specific fallback summary based on keywords
        topic_lower = topic.lower()
        topic_words = topic_lower.split()
        
        # Extract time period if present (e.g., 2020-2025, 1800s, etc.)
        time_period = ""
        time_match = re.search(r'(\d{4})\s*-\s*(\d{4})', topic_lower)
        if time_match:
            start_year = time_match.group(1)
            end_year = time_match.group(2)
            time_period = f" from {start_year} to {end_year}"
        
        # Detect topic category and provide relevant fallback
        if any(word in topic_words for word in ["ai", "artificial intelligence", "machine learning"]):
            return get_ai_fallback(time_period), ""
        elif any(word in topic_words for word in ["history", "ancient", "medieval", "century", "dynasty"]):
            return get_history_fallback(topic, time_period), ""
        elif any(word in topic_words for word in ["science", "physics", "chemistry", "biology", "quantum"]):
            return get_science_fallback(topic, time_period), ""
        elif any(word in topic_words for word in ["technology", "tech", "software", "hardware", "digital"]):
            return get_technology_fallback(topic, time_period), ""
        else:
            # Generic but informative fallback
            return f"This research explores {topic}{time_period}. The investigation will cover key developments, significant events, and important figures in this field, analyzing their impact and contributions. The study aims to provide a comprehensive understanding of {topic} through various reliable sources including academic publications, expert analyses, and primary documents where available.", ""

def get_ai_fallback(time_period):
    base = "Artificial Intelligence (AI) represents the development of computer systems capable of performing tasks that typically require human intelligence. "
    if time_period:
        return base + f"This research specifically examines AI evolution{time_period}, focusing on major breakthroughs, emerging technologies, and their societal impact during this period. Key areas include machine learning, neural networks, natural language processing, and their applications across various industries."
    return base + "The field encompasses machine learning, neural networks, natural language processing, and their applications across various industries."

def get_history_fallback(topic, time_period):
    base = f"This historical investigation examines {topic}"
    if time_period:
        return base + f"{time_period}, analyzing key events, social developments, cultural changes, and significant figures of the era. The research draws from historical records, archaeological evidence, and scholarly interpretations."
    return base + ", exploring its chronological development, cultural significance, and lasting impact on society."

def get_science_fallback(topic, time_period):
    base = f"This scientific exploration focuses on {topic}"
    if time_period:
        return base + f"{time_period}, examining key discoveries, theoretical developments, and experimental breakthroughs. The research covers both fundamental principles and practical applications in this field."
    return base + ", investigating its fundamental principles, experimental evidence, and practical applications in modern science."

def get_technology_fallback(topic, time_period):
    base = f"This technological analysis explores {topic}"
    if time_period:
        return base + f"{time_period}, examining innovations, breakthroughs, and their impact on industry and society. The research covers both technical developments and their practical applications."
    return base + ", investigating its development, implementation, and impact on various sectors of industry and society."


def fetch_youtube_summary_link(topic):
    print("\n🎥 Searching YouTube...")

    try:
        cmd = [
            "yt-dlp",
            f"ytsearch1:{topic}",
            "--print", "%(title)s | %(webpage_url)s",
            "--quiet"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout.strip()

        if not output:
            print("❌ No video found for this topic.")
            return None

        title, link = output.split(" | ", 1)
        return {
            "title": title,
            "link": link
        }

    except FileNotFoundError:
        print("❌ Error: yt-dlp is not installed. YouTube search functionality is unavailable.")
        return None
    except Exception as e:
        print(f"❌ Error during YouTube search: {e}")
        print("YouTube search functionality is currently unavailable.")
        return None


def save_context_to_file(topic, summary, wiki_url, video_data):
    # Create fresh context with current search topic
    context = {
        "topic": topic,
        "wikipedia": {
            "summary": summary,
            "url": wiki_url
        },
        "youtube": video_data if video_data else {"link": ""}
    }

    # Always overwrite the existing context.json
    with open("context.json", "w") as f:
        json.dump(context, f, indent=2)
    print("\n✅ Saved context to context.json")


def main():
    if len(sys.argv) < 2:
        print("Usage: python MCP_assistant.py \"your topic here\"")
        return

    topic = sys.argv[1]
    print(f"🔍 Researching topic: {topic}")

    # First, ensure we start with a clean context
    if os.path.exists("context.json"):
        os.remove("context.json")

    # Wikipedia
    summary, url = fetch_wikipedia_summary(topic)
    if summary:
        print("\n📄 Summary:\n")
        print(summary)
        if not url:
            print("\n⚠️ Using fallback/cached description as Wikipedia API was unavailable")
    else:
        print("❌ Could not retrieve any description")
        summary = "No description available."
        url = ""

    print("\n=== YouTube Video Suggestion ===\n")
    video_data = fetch_youtube_summary_link(topic)
    if video_data:
        print(f"Use this video for summarization:\n📺 {video_data['title']}")
    else:
        print("❌ Could not retrieve video.")

    # Always save context with the current search topic
    save_context_to_file(topic, summary, url, video_data)


if __name__ == "__main__":
    main()
