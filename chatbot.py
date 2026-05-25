import datetime

def main():
    print("--- DecodeLabs Chatbot Engine ---")
    print("Welcome! Type your message below.")
    print("Commands: time, date, project info, system 1, system 2, white box, exit")
    print("---------------------------------")

    while True:
        try:
            raw_input = input("You: ")
            clean_input = raw_input.lower().strip()
            
            if not clean_input:
                print("Bot: Please say something.\n")
                continue

            if clean_input in ['exit', 'quit', 'bye']:
                print("Bot: Goodbye!")
                break
                
            elif clean_input in ['hello', 'hi', 'hey']:
                print("Bot: Hello! How can I help you today?\n")
                
            elif clean_input in ['time', 'what time is it?']:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                print(f"Bot: The time is {current_time}.\n")
                
            elif clean_input in ['day', 'date', 'today']:
                current_day = datetime.datetime.now().strftime("%A, %B %d")
                print(f"Bot: Today is {current_day}.\n")
                
            elif clean_input in ['project info', 'project 1', 'project1']:
                print("Bot: This is Project 1, a rule-based chatbot built with if-else logic.\n")
                
            elif clean_input in ['system 1', 'system1', 'what is system 1?']:
                print("Bot: System 1 is a probabilistic AI that predicts text.")
                print("Use case: Used for creative tasks like content writing or brainstorming.\n")
                
            elif clean_input in ['system 2', 'system2', 'what is system 2?']:
                print("Bot: System 2 is a deterministic rule-based logic engine with zero error.")
                print("Use case: Used as critical guardrails to filter and secure AI outputs.\n")
                
            elif clean_input in ['white box', 'what is white box?']:
                print("Bot: A white box system is fully transparent, making every response traceable.\n")
                
            elif clean_input in ['guardrails', 'ai guardrails']:
                print("Bot: Guardrails are rule-based filters used to block unsafe AI outputs.\n")
                
            else:
                print("Bot: Sorry, I did not understand that. Try typing 'project info'.\n")
                
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Session closed.")
            break

if __name__ == "__main__":
    main()