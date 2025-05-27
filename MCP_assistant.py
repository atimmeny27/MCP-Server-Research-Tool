import sys
import wikipedia
import subprocess
import json
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
import re


def fetch_wikipedia_summary(topic):
    try:
        # Do a search and grab the best match
        search_results = wikipedia.search(topic)
        if not search_results:
            print(f"❌ No Wikipedia pages found for '{topic}'")
            return None, None

        best_match = search_results[0]
        summary = wikipedia.summary(best_match, sentences=5)
        page = wikipedia.page(best_match)
        return summary, page.url
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"⚠️ Topic '{topic}' is too ambiguous. Try one of these:")
        for option in e.options[:5]:
            print(f" - {option}")
        return None, None
    except wikipedia.exceptions.PageError:
        print(f"❌ No page found for '{topic}'. Try another topic.")
        return None, None


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
            print("❌ No video found.")
            return None

        title, link = output.split(" | ", 1)
        return {
            "title": title,
            "link": link
        }

    except Exception as e:
        print(f"❌ Error during YouTube search: {e}")
        return None


def save_context_to_file(topic, summary, wiki_url, video_data):
    context = {
        "topic": topic,
        "wikipedia": {
            "summary": summary,
            "url": wiki_url
        },
        "youtube": video_data
    }

    with open("context.json", "w") as f:
        json.dump(context, f, indent=2)
    print("\n✅ Saved context to context.json")


def main():
    if len(sys.argv) < 2:
        print("Usage: python MCP_assistant.py \"your topic here\"")
        return

    topic = sys.argv[1]
    print(f"🔍 Researching topic: {topic}")

    # Wikipedia
    summary, url = fetch_wikipedia_summary(topic)
    if summary:
        print("\n📄 Wikipedia Summary:\n")
        print(summary)
    else:
        print("⚠️ Wikipedia summary not compotent, searching internet...")
        summary = "No Wikipedia summary found."
        url = ""

    print("\n=== YouTube Video Suggestion ===\n")
    video_data = fetch_youtube_summary_link(topic)
    if video_data:
        print(f"Use this video for summarization:\n📺 {video_data['title']}")
    else:
        print("❌ Could not retrieve video.")

    if summary and video_data:
        save_context_to_file(topic, summary, url, video_data)


if __name__ == "__main__":
    main()
