#!/bin/bash

# Prompt for topic
read -p "Enter your research topic: " topic

# Generate context
python3 MCP_assistant.py "$topic"

# Call the model with 'long' duration for better research
MCP_DURATION=long python3 send_to_claude.py
