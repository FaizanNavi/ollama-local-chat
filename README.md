# Bot-Phi3-Mini

Bot-Phi3-Mini is a chatbot application built using the `langchain-ollama` library. It leverages the `OllamaLLM` model to provide context-aware conversational AI capabilities. This project is ideal for customer support, research assistance, or general-purpose chatbot applications.

## Features

- **Context-Aware Conversations**: Maintains conversation history for better responses.
- **Powered by OllamaLLM**: Uses the `phi3` model for natural language understanding.
- **Customizable Prompts**: Easily modify the chatbot's behavior using templates.

## Requirements

The project dependencies are listed in the `requirements.txt` file. Install them using the following command:


##Dependencies
langchain-ollama
langchain-core

##File Structure
bot.py: Main script to run the chatbot. It provides an interactive terminal-based interface.
sample.py: Example script demonstrating how to use the OllamaLLM model with a predefined prompt.
requirements.txt: Contains the list of dependencies required for the project.

Usage
1. Clone the Repository:
  git clone https://github.com/FaizanNavi/ollama-local-chat.git
  cd ollama-local-chat

2. Install Dependencies:
     pip install -r requirements.txt

3. Run the Chatbot:
     python bot.py
