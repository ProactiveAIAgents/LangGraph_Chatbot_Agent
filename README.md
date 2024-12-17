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
![Architecture](https://github.com/user-attachments/assets/2ea6a8c1-b354-42d9-b0f3-5f83d5922b2b)

The project architecture demonstrates a clean, modular structure with the following components:
- `chatbot_agent.py`: Core implementation of the LangGraph-based chatbot
- `requirements.txt`: Dependency management for reproducible environments
- `.env`: Secure configuration for API keys and environment variables
- `.gitignore`: Version control configuration
- `README.md`: Comprehensive project documentation

### Implementation
![Implementation Part 1](https://github.com/user-attachments/assets/d376c746-d8cf-488d-9a39-2b6730a68bb7)
![Implementation Part 2](https://github.com/user-attachments/assets/57b478e5-00ec-40eb-91a2-6a1ea1fe9cc7)

The implementation showcases:
- Integration of LangGraph with Claude AI model
- Type-safe state management using TypedDict
- Structured conversation flow with StateGraph
- Robust error handling and message processing
- Clean separation of concerns between different components

### Interactive Demo
![Demo](https://github.com/user-attachments/assets/7d5f4ebb-04b4-4fd0-9d47-8f060771e462)

The interactive demo illustrates:
- Natural language conversation capabilities
- Contextual understanding and response generation
- Clean command-line interface
- Proper handling of user inputs and exits
- Real-time response generation using Claude AI

### Setup Process
![Setup](https://github.com/user-attachments/assets/1cf3ec39-9052-45bd-a07b-957844177dc9)

The setup process demonstrates:
- Virtual environment configuration
- Dependency installation via pip
- Environment variable management
- Project initialization steps
- Verification of successful installation
