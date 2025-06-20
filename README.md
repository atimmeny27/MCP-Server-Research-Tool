# MCP-Server-Research-Tool

A long-form research assistant tool powered by LLMs, designed to gather information from primary sources, podcasts, academic PDFs, textbooks, YouTube, and more. This tool simulates deep, realistic research and outputs structured markdown files containing both a detailed topic summary and source list.

---

## 🚀 Installation

To get started on macOS:

You will need a free API key from OpenRouter or another source, scroll to bottom after step 2 if you don't have a dedicated one for this project. 

1. Open **Terminal** (`⌘ + Space`, type `Terminal`, hit Enter).
2. Run the following commands:

```bash
git clone https://github.com/atimmeny27/MCP-Server-Research-Tool
cd MCP-Server-Research-Tool
chmod +x start.sh
```

4. Then
```bash
python3 -m ensurepip --upgrade
python3 -m pip install -r requirements.txt
clear
```

3. The tool is now verified, if you still need to setup an API go below. Anytime you wish to launch the program, enter

```bash
./start.sh
```

4. You can also launch the scripts manually with

```bash
python MCP_assistant.py "Topic Here"
```
then
```bash
MCP_DURATION=long python send_to_claude.py
```

5. Step 3 is just a script to automate 4, they accomplish the same thing.


6. I hope you find this helpful and a fun tool to learn with. To edit the research prompt, look around lines 18-220 in send_to_claude.py. It will be the long f-string where the intructions are sent to Claude.

7. The more specific the research topic, the better the results will be (ex. "AI" vs “The Evolution of Machine Learning into Large Language Models and Modern AI (1950–2024): Key breakthroughs, paradigms, and societal impact”

8. Please be specific with dates, times, geography, people, etc... and just rename the markdown (.md) file so they arent 100 characters long.

9. Once it's done, you can scroll through in the terminal, or search for "whatever-your-search-was.md" in finder, this will pull up the notes as well as sources used. This outputs into markdown, so its best to open the notes in a markdown friendly editor (like obsidian)

10. Enter your topic, and wait up to 2 minutes for the LLM to research using primary sources, podcasts, pdfs, textbooks, and academic materials. This is being forwarded to Claude, so spelling errors or niche topics may still cause confusion.

9. If you see "🔐 Using key: sk-or-v1-2 ...", it means it's currently researching, even if it says "❌ Could not retrieve video."

11. If you want to add this as a desktop tool, you can copy the "start.sh" contents (```open -e start.sh```),
   then paste them into a shell script inside the apple automator app.

12. To start tool in the future you only need
```bash
cd MCP-Server-Research-Tool
./start.sh
```

### 🔑 How to Get Your Free OpenAI API Key

To use this tool, you’ll need a free API key from OpenRouter (or OpenAI / Anothropic but this one is free). Follow these steps:

1. Sign Up or Log In

[Go to https://platform.openai.com/signup](https://openrouter.ai/)
➡️ Create an account or log in with Google/GitHub.

2. Generate an API Key
	•	After logging in, click your profile icon → “Keys”
	•	Click “Create Key” and copy the resulting string (starts with sk-or-...)
	•	Save it somewhere safe

3. Set Up Your Key Locally

4. To permanently keep this key active
```bash
touch ~/.zshrc 
open -e ~/.zshrc 
```
5. Then paste ```export OPENROUTER_API_KEY="your-key-here-starting-with-sk-"``` at the end of the file, and save it
6. Now paste ```source ~/.zshrc``` in your terminal or refresh the session. You can now start the tool with ```./start.sh```

7. If you plan on using other projects with API keys in terminal, you may want to do step 3 inside of a .env file in this root directory(```touch .env
  open -e .env```
paste here)

8. Start tool with ```./start.sh```, if you get any errors it probably means wikipedia's API is overloaded and cannot process your request, just try in a few minutes (or paste a traceback log to chat gpt if you want)
8. Enter your topic, and wait up to 2 minutes for the LLM to research using primary sources, podcasts, pdfs, textbooks, and academic materials.

9. If you see "✅ Saved context to context.json
🔐 Using key: sk-or-v1-2 ...", it means it's currently researching

   



