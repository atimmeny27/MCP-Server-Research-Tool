#!/bin/bash

# Prompt for topic
read -p "Enter your research topic: " topic

# Step 1: Generate context
python MCP_assistant.py "$topic"

# Step 2: Call the model with 'long' duration
MCP_DURATION=long python send_to_claude.py
