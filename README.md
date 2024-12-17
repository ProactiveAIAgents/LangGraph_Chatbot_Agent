# LangGraph Chatbot Agent

## Description
A project designed to leverage LangGraph and Anthropic's Claude model for creating an intelligent conversational agent. This chatbot demonstrates how LangGraph can be used to create structured conversation flows and manage complex dialogue states, showcasing the integration of advanced language models with graph-based conversation management.

## Features
- Interactive chat interface with Claude AI model integration
- Structured conversation flow using LangGraph
- State management for contextual conversations
- Extensible architecture for adding new conversation patterns
- Error handling and graceful conversation termination

## Technologies Used
- LangGraph for conversation flow management
- Anthropic's Claude model for natural language processing
- Python as the primary programming language
- Python-dotenv for environment variable management
- Langchain Core for prompt engineering

## Skills Learned
- Advanced conversation flow management with LangGraph
- Integration with Claude AI model
- State management in conversational AI
- Environment configuration and security practices
- Graph-based dialogue system implementation

## Tools Used
- Visual Studio Code/Cursor2 IDE
- Git for version control
- LangGraph for conversation management
- Anthropic's Claude API
- Python's type hinting for code reliability

## Project Implementation

### 1. Project Setup
- **Dependencies Management**: Configuration of LangGraph, Langchain, and Claude API requirements
- **Environment Configuration**: Secure API key management using .env
- **Project Structure**: Organized codebase with clear separation of concerns

### 2. Core Implementation
- **LangGraph Integration**: Setup of StateGraph for conversation management
- **Claude AI Integration**: Configuration of ChatAnthropic for natural language processing
- **State Management**: Implementation of ChatState for maintaining conversation context

### 3. Application Logic
- **Conversation Flow**: Implementation of structured dialogue paths
- **Message Handling**: Processing of user inputs and generating appropriate responses
- **Error Management**: Graceful handling of exceptions and edge cases

### 4. User Interface
- **CLI Interface**: Implementation of an interactive command-line interface
- **User Experience**: Clear prompts and intuitive interaction patterns

### 5. Deployment and Testing
- **Local Testing**: Instructions for testing the chatbot locally
- **Error Handling**: Robust error management for various scenarios
- **Documentation**: Comprehensive setup and usage instructions

## Installation
1. **Clone the Repository**: `git clone https://github.com/ProactiveAIAgents/LangGraph_Chatbot_Agent.git`
2. **Install Dependencies**: `pip install -r requirements.txt`
3. **Set Up Environment**: Configure `.env` with your Anthropic API key
4. **Run the Application**: `python chatbot_agent.py`

## Project Documentation

### Architecture
![LangGraph Chatbot Agent Architecture](images/architecture.png)
[Architecture description]

### Implementation
![Core Chatbot Agent Code](images/implementation.png)
[Implementation details]

### Interactive Demo
![Chatbot in Action](images/demo.png)
[Demo description]

### Setup Process
![Environment Configuration](images/setup.png)
[Setup instructions]
