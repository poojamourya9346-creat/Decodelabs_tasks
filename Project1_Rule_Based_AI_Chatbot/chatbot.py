#!/usr/bin/env python3
"""
DecodeLabs AI Industrial Training - Project 1: Rule-Based AI Chatbot
Author: DecodeLabs Student

This script implements a simple rule-based AI chatbot. It runs continuously
in a terminal loop, accepts user input, processes it using standard Python
control flow (if-elif-else), and provides predefined responses based on the query.
"""

def main():
    print("==================================================")
    print("    Welcome to the Rule-Based AI Chatbot!         ")
    print("    Type 'help' for instructions or 'exit' to quit. ")
    print("==================================================")
    
    # Continuous loop until user decides to exit
    while True:
        try:
            # 1. Accept user input
            user_input = input("User: ")
        except (KeyboardInterrupt, EOFError):
            # Handle user interrupting the program (e.g. Ctrl+C or Ctrl+D)
            print("\nBot: Goodbye! Have a great day!")
            break
            
        # 2. Ignore case and strip leading/trailing spaces
        cleaned_input = user_input.strip().lower()
        
        # 3. Strip trailing punctuation (like ?, !, .) to make matching more robust
        cleaned_input = cleaned_input.rstrip('?!.')
        
        # 4. Respond using only if-elif-else statements
        if cleaned_input in ["hi", "hello", "hey"]:
            print("Bot: Hello! Welcome.")
            
        elif cleaned_input in ["what is your name", "who are you"]:
            print("Bot: I am a Rule-Based AI Chatbot, created to assist you with simple questions.")
            
        elif cleaned_input == "good morning":
            print("Bot: Good morning! Hope you have a wonderful day ahead.")
            
        elif cleaned_input == "good afternoon":
            print("Bot: Good afternoon! How can I help you today?")
            
        elif cleaned_input == "good evening":
            print("Bot: Good evening! Hope your day went well.")
            
        elif cleaned_input == "help":
            print("Bot: I can help you with simple tasks! Ask me about:")
            print("     - Greetings (hi, hello, hey)")
            print("     - Time greetings (good morning/afternoon/evening)")
            print("     - AI topics (what is ai/machine learning/python)")
            print("     - Identity (what is your name/who are you)")
            print("     - Or exit the chat using 'exit', 'quit', or 'bye'")
            
        elif cleaned_input == "what is ai":
            print("Bot: Artificial Intelligence is the simulation of human intelligence by machines.")
            
        elif cleaned_input == "what is machine learning":
            print("Bot: Machine Learning is a subset of AI that allows systems to learn and improve from experience without being explicitly programmed.")
            
        elif cleaned_input == "what is python":
            print("Bot: Python is a popular, easy-to-learn programming language widely used in AI, web development, and data science.")
            
        elif cleaned_input == "how are you":
            print("Bot: I'm doing great, thank you! How are you doing today?")
            
        elif cleaned_input in ["thank you", "thanks"]:
            print("Bot: You're welcome!")
            
        elif cleaned_input in ["bye", "exit", "quit"]:
            # Display a goodbye message before terminating
            print("Bot: Goodbye! Have a great day!")
            break
            
        else:
            # Default response for unknown questions
            print("Bot: I'm sorry, I don't understand that. Please ask another question.")

if __name__ == "__main__":
    main()
