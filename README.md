# MCP-Server-Research-Tool

A long-form research assistant tool powered by LLMs, designed to gather information from primary sources, podcasts, academic PDFs, textbooks, YouTube, and more. This tool simulates deep, realistic research and outputs structured markdown files containing both a detailed topic summary and source list.

---

## 🚀 Installation

To get started on macOS:

1. Open **Terminal** (`⌘ + Space`, type `Terminal`, hit Enter).
2. Run the following commands:

```bash
git clone https://github.com/atimmeny27/MCP-Server-Research-Tool
cd MCP-Server-Research-Tool
chmod +x start.sh
```

3. The tool is now verified, anytime you wish to launch the program, enter

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

5. Steps 3 and 4 accomplish the same thing.
6. Enter your topic, and wait up to 2 minutes for the LLM to research using primary sources, podcasts, pdfs, textbooks, and academic materials.
7. Once it's done, you can scroll through in the terminal, or search for "yourtopic.md" in finder, this will pull up the notes as well as sources used.


8. I hope you find this helpful and a fun tool to learn with.
