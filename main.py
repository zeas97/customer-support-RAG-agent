from customer_support_rag import RAGAgent
from dotenv import load_dotenv
import os
from termcolor import colored

def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print(colored("Error: Set GEMINI_API_KEY environment variable.", "red"))
        return

    agent = RAGAgent(api_key=api_key)
    print(colored("Hi! I’m your Customer Support AI Agent. How can I assist you today?\n", "blue"))

    while True:
        try:
            query = input(colored("You: ", "yellow")).strip().lower()
            if query == "exit":
                print(colored("Goodbye!", "blue"))
                break

            context = agent.retrieve_context(query)
            response = agent.generate_response(query, context)
            print(colored(f"Agent: {response}\n", "green"))

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(colored(f"Error: {str(e)}", "red"))

if __name__ == "__main__":
    main()
