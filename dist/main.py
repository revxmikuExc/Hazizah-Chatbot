# main.py

import random
from zizah_core_en import Zizah

def start_chat():
    chatbot = Zizah()
    ascii_menu = '''                                                                            
                                                                               
██╗  ██╗ █████╗ ███████╗██╗███████╗ █████╗ ██╗  ██╗
██║  ██║██╔══██╗╚══███╔╝██║╚══███╔╝██╔══██╗██║  ██║
███████║███████║  ███╔╝ ██║  ███╔╝ ███████║███████║
██╔══██║██╔══██║ ███╔╝  ██║ ███╔╝  ██╔══██║██╔══██║
██║  ██║██║  ██║███████╗██║███████╗██║  ██║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
                                                                                                                    
'''
    if not chatbot.memory.get("user_name"):
        print(f"彡 {chatbot.personality['NAME_SHORT']}: {chatbot.personality['INITIAL_GREETING']}")
    elif not chatbot.memory.get("user_hobby"):
        print(f"彡 {chatbot.personality['NAME_SHORT']}: {chatbot.personality['INITIAL_GREETING_HOBBY']}")
    elif not chatbot.memory.get('human_traits'): 
        print(f"[ZIZAH LOG]: human_traits not found")
    else:
        user_name = chatbot.memory.get("user_name", "(unknown)")
        user_hobby = chatbot.memory.get("user_hobby", "(unknown)")
    

    print( "-" * 35,"\n" ,(ascii_menu))
    print(f"彡 {chatbot.personality['NAME_SHORT']}: Hello my handsome, {user_name}! I remember your hobby is {user_hobby}. Nice to talk to you again.")

    while True:
        try:
            user_name = chatbot.memory.get("user_name") or "(unknown)"
            user_input = input(f"➥ {user_name}: ") 


            if user_input.lower() in ["exit", "quit", "bye", "goodbye"]:
                farewell_message = random.choice(chatbot.personality['FAREWELL']) 
                print(f"彡 {chatbot.personality['NAME_SHORT']}: {farewell_message}") 
                chatbot.save_state()
                break
            # Mereset riwayat percakapan
            elif "/reset" in user_input.lower():
                chatbot.memory['conversation_history'] = []
                chatbot.memory['human_traits'] = []
                reset_message = random.choice(chatbot.personality["FAREWELL_RESET"])
                chatbot.save_state()
                print(f"彡 {chatbot.personality['NAME_SHORT']}: {reset_message}") 
                break
            

            response = chatbot.get_response(user_input)
            print(f"彡 {chatbot.personality['NAME_SHORT']}: {response}", "\n")

        except KeyboardInterrupt:
            chatbot.save_state()
            break
        # except Exception as e:
        #     print(f"[ERROR]: An error occurred -> {e}")
        #     print(f"Type: {type(e).__name__}")
        #     chatbot.save_state()
        #     break

if __name__ == "__main__":
    start_chat()
