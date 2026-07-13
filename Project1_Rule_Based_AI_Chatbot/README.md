# DecodeLabs Project 1: Rule-Based AI Chatbot

A lightweight, beginner-friendly, and professional **Rule-Based AI Chatbot** implemented in Python. This project is built without external dependencies, machine learning libraries, or large language models, relying entirely on basic Python control flow (`if-elif-else`) to process and respond to user inputs.

## Project Description

This chatbot demonstrates the fundamental concept of rule-based systems in AI. It runs continuously in the terminal, accepts user input, processes it (normalizing letter cases and trailing punctuation), and returns a mapped response. If a query does not match any predefined rules, a friendly default fallback response is provided.

## Features

- **Continuous Conversation**: The chatbot keeps running in a loop until an exit command is given.
- **Robust Input Matching**: Normalizes inputs to lowercase and removes common trailing punctuation (`?`, `!`, `.`) for a smoother user experience.
- **Predefined Response Rules**: Includes rules for:
  - Greetings (hi, hello, hey)
  - Time-specific greetings (good morning/afternoon/evening)
  - Identity questions (what is your name, who are you)
  - Help info (help)
  - Basic AI/Python concepts (what is ai, what is machine learning, what is python)
  - Casual questions (how are you, thank you, thanks)
- **Graceful Termination**: Handles exit commands (`bye`, `exit`, `quit`) as well as keyboard interrupts (like `Ctrl+C`).
- **Clean Structure**: Fully organized with a `main()` function entry point and `if __name__ == "__main__":` block.

## Technologies Used

- **Python 3.x** (Standard Library only)

## How to Run

1. Make sure Python 3 is installed on your system.
2. Clone or download this repository.
3. Open a terminal/command prompt in the project directory.
4. Run the chatbot using the following command:
   ```bash
   python chatbot.py
   ```

## Example Conversation

```text
==================================================
    Welcome to the Rule-Based AI Chatbot!         
    Type 'help' for instructions or 'exit' to quit. 
==================================================
User: hi
Bot: Hello! Welcome.

User: what is ai?
Bot: Artificial Intelligence is the simulation of human intelligence by machines.

User: thanks!
Bot: You're welcome!

User: exit
Bot: Goodbye! Have a great day!
```

## Project Structure

```text
Rule-Based AI Chatbot/
│
├── chatbot.py         # Main Python executable script containing chatbot logic
├── README.md          # Project documentation (this file)
└── requirements.txt   # File specifying project dependencies
```

## Future Improvements

- **Regular Expression Matching**: Implement the `re` module to handle slightly more complex sentence patterns.
- **GUI or Web Interface**: Build a web UI using Flask, FastAPI, or Streamlit to make it interactive.
- **External API Integration**: Connect to an LLM API (e.g., Gemini API or OpenAI API) or database to provide dynamic, non-predefined responses.
