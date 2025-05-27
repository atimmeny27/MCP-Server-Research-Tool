import json
import openai
import os

openai.api_key = os.environ.get("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

def load_context():
    with open("context.json", "r") as f:
        return json.load(f)

def ask_model(context):
    topic = context["topic"]
    wiki = context["wikipedia"]["summary"]
    video = context["youtube"]["link"]

    prompt = f"""
You are a brilliant and meticulous research assistant.

Your task is to conduct a deep and structured investigation into the following topic:

Topic: {topic}

Wikipedia Summary (for starting context):
{wiki}

Additional Source (YouTube, video, or transcript):
{video}

Instructions:
1. Spend as much time as needed (simulated) to research this topic thoroughly. Assume access to web sources, books, and academic databases.
2. Simulate 30–60 minutes of research time. Review each valuable source for 30–60 seconds before integrating findings.
3. Collect at least **15** credible sources, with **at least one from each** of the following:
   - Wikipedia (already provided)
   - YouTube video (already provided)
   - Academic journal or peer-reviewed article
   - Book or textbook
   - Primary source or firsthand account (if applicable)
   - Podcast or audio interview
   - Government or institution-backed website (e.g., UN, NIH, NASA, etc.)

4. Organize your findings into clearly labeled sections and sub-sections. Include:
   - Detailed bullet points
   - Descriptive narrative
   - Historical, cultural, economic, and social relevance
   - Lesser-known insights and non-Western perspectives (when applicable)

5. The response should be **at least 2000 words**.
   - Use Markdown formatting with headers and subheaders
   - Every section should contain both summary and evidence

6. At the end of your response, output nothing except a section labeled `=== SOURCES ===`.  
   Each source should follow this format:  
   [Title](URL) — A 1–3 sentence summary of why it’s credible and how it contributed to the research.

Do not respond quickly. Simulate realistic, thoughtful research.You are a brilliant and meticulous research assistant.

Your task is to conduct a deep and structured investigation into the following topic:

Topic: {topic}

Wikipedia Summary (for starting context):
{wiki}

Additional Source (YouTube, video, or transcript):
{video}

Instructions:
1. Spend as much time as needed (simulated) to research this topic thoroughly. Assume access to web sources, books, and academic databases.
2. Simulate 30–60 minutes of research time. Review each valuable source for 30–60 seconds before integrating findings.
3. Collect at least **15** credible sources, with **at least one from each** of the following:
   - Wikipedia (already provided)
   - YouTube video (already provided)
   - Academic journal or peer-reviewed article
   - Book or textbook
   - Primary source or firsthand account (if applicable)
   - Podcast or audio interview
   - Government or institution-backed website (e.g., UN, NIH, NASA, etc.)

4. Organize your findings into clearly labeled sections and sub-sections. Include:
   - Detailed bullet points
   - Descriptive narrative
   - Historical, cultural, economic, and social relevance
   - Lesser-known insights and non-Western perspectives (when applicable)

5. The response should be **at least 2000 words**.
   - Use Markdown formatting with headers and subheaders
   - Every section should contain both summary and evidence

6. At the end of your response, output nothing except a section labeled `=== SOURCES ===`.  
   Each source should follow this format:  
   [Title](URL) — A 1–3 sentence summary of why it’s credible and how it contributed to the research.

Do not respond quickly. Simulate realistic, thoughtful research.You are a brilliant and meticulous research assistant.

Your task is to conduct a deep and structured investigation into the following topic:

Topic: {topic}

Wikipedia Summary (for starting context):
{wiki}

Additional Source (YouTube, video, or transcript):
{video}

Instructions:
1. Spend as much time as needed (simulated) to research this topic thoroughly. Assume access to web sources, books, and academic databases.
2. Simulate 30–60 minutes of research time. Review each valuable source for 30–60 seconds before integrating findings.
3. Collect at least **15** credible sources, with **at least one from each** of the following:
   - Wikipedia (already provided)
   - YouTube video (already provided)
   - Academic journal or peer-reviewed article
   - Book or textbook
   - Primary source or firsthand account (if applicable)
   - Podcast or audio interview
   - Government or institution-backed website (e.g., UN, NIH, NASA, etc.)

4. Organize your findings into clearly labeled sections and sub-sections. Include:
   - Detailed bullet points
   - Descriptive narrative
   - Historical, cultural, economic, and social relevance
   - Lesser-known insights and non-Western perspectives (when applicable)

5. The response should be **at least 2000 words**.
   - Use Markdown formatting with headers and subheaders
   - Every section should contain both summary and evidence

6. At the end of your response, output nothing except a section labeled `=== SOURCES ===`.  
   Each source should follow this format:  
   [Title](URL) — A 1–3 sentence summary of why it’s credible and how it contributed to the research.

Do not respond quickly. Simulate realistic, thoughtful research.You are a brilliant and meticulous research assistant.

Your task is to conduct a deep and structured investigation into the following topic:

Topic: {topic}

Wikipedia Summary (for starting context):
{wiki}

Additional Source (YouTube, video, or transcript):
{video}

Instructions:
1. Spend as much time as needed (simulated) to research this topic thoroughly. Assume access to web sources, books, and academic databases.
2. Simulate 30–60 minutes of research time. Review each valuable source for 30–60 seconds before integrating findings.
3. Collect at least **15** credible sources, with **at least one from each** of the following:
   - Wikipedia (already provided)
   - YouTube video (already provided)
   - Academic journal or peer-reviewed article
   - Book or textbook
   - Primary source or firsthand account (if applicable)
   - Podcast or audio interview
   - Government or institution-backed website (e.g., UN, NIH, NASA, etc.)

4. Organize your findings into clearly labeled sections and sub-sections. Include:
   - Detailed bullet points
   - Descriptive narrative
   - Historical, cultural, economic, and social relevance
   - Lesser-known insights and non-Western perspectives (when applicable)

5. The response should be **at least 2000 words**.
   - Use Markdown formatting with headers and subheaders
   - Every section should contain both summary and evidence

6. At the end of your response, output nothing except a section labeled `=== SOURCES ===`.  
   Each source should follow this format:  
   [Title](URL) — A 1–3 sentence summary of why it’s credible and how it contributed to the research.

Do not respond quickly. Simulate realistic, thoughtful research.You are a brilliant and meticulous research assistant.

Your task is to conduct a deep and structured investigation into the following topic:

Topic: {topic}

Wikipedia Summary (for starting context):
{wiki}

Additional Source (YouTube, video, or transcript):
{video}

Instructions:
1. Spend as much time as needed (simulated) to research this topic thoroughly. Assume access to web sources, books, and academic databases.
2. Simulate 30–60 minutes of research time. Review each valuable source for 30–60 seconds before integrating findings.
3. Collect at least **15** credible sources, with **at least one from each** of the following:
   - Wikipedia (already provided)
   - YouTube video (already provided)
   - Academic journal or peer-reviewed article
   - Book or textbook
   - Primary source or firsthand account (if applicable)
   - Podcast or audio interview
   - Government or institution-backed website (e.g., UN, NIH, NASA, etc.)

4. Organize your findings into clearly labeled sections and sub-sections. Include:
   - Detailed bullet points
   - Descriptive narrative
   - Historical, cultural, economic, and social relevance
   - Lesser-known insights and non-Western perspectives (when applicable)

5. The response should be **at least 2000 words**.
   - Use Markdown formatting with headers and subheaders
   - Every section should contain both summary and evidence

6. At the end of your response, output nothing except a section labeled `=== SOURCES ===`.  
   Each source should follow this format:  
   [Title](URL) — A 1–3 sentence summary of why it’s credible and how it contributed to the research.

Do not respond quickly. Simulate realistic, thoughtful research. Before finishing, meticulously fact-check every single claim, statistic, and historical reference. Ensure all points are accurate, specific, and supported by credible sources.
""".strip()

    prompt += """
    
Please write **at least 1500 words**. 
Use detailed headers and subheaders for every major time period and theme. 
You may use as many bullet points as needed, but emphasize depth, historical context, and consequences.
Be thorough — include lesser-known developments, cultural and social history, and the impact on international relations. 

Do not rush. Spend as long as needed.
"""

    duration = os.getenv("MCP_DURATION", "short")
    if duration == "medium":
        prompt += "\n\nTake more time to explain each bullet and go deeper on the video takeaways."
    elif duration == "long":
        prompt += "\n\nYou have plenty of time. Include extended analysis, relevant historical context, and interconnections with other topics. This takes AT THE BARE MINIMUM 5 minues of research before any response."

    print("🔐 Using key:", openai.api_key[:10], "...")

    response = openai.ChatCompletion.create(
        model="anthropic/claude-3-haiku",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    result_text = response.choices[0].message["content"]
    print("\n🧠 MODEL RESPONSE:\n")
    print(result_text)

    # Split response into main summary and sources
    if "=== SOURCES ===" in result_text:
        summary, sources = result_text.split("=== SOURCES ===", 1)
    else:
        summary, sources = result_text, None

    save_summary_file(topic, summary)
    if sources:
        save_sources_file(topic, sources)

def save_summary_file(topic, content):
    filename = topic.lower().replace(" ", "_") + ".md"
    filepath = os.path.join("results", filename)
    os.makedirs("results", exist_ok=True)
    with open(filepath, "w") as f:
        f.write(f"# Research Summary: {topic}\n\n")
        f.write(content.strip())
    print(f"\n💾 Summary saved to: {filepath}")

def save_sources_file(topic, content):
    filename = topic.lower().replace(" ", "_") + ".md"
    filepath = os.path.join("sources", filename)
    os.makedirs("sources", exist_ok=True)
    with open(filepath, "w") as f:
        f.write(f"# Sources for: {topic}\n\n")
        f.write(content.strip())
    print(f"\n🔗 Sources saved to: {filepath}")

if __name__ == "__main__":
    context = load_context()
    ask_model(context)
