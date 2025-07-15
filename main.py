from tasks.check_price import get_emag_price
#from tasks.forms import complete_form
from tasks.teams import send_teams_message
from tasks.social_feed import extract_x_posts, create_html_feed
from tasks.forms import create_quiz
from tasks.LLM import conversation
from config import user_messages

def main():
    print("1. Verificare pret eMAG")
    print("2. Creati un formular")
    print("3. Trimiteti mesaje persoanelor in Teams")
    print("4. Creati un feed")
    print("5. Porneste conversatia cu ChatGPT")
    opt = input("Alege opțiunea: ")

    if opt == "1":
        url = input("Introdu URL produs eMAG: ")
        pret = get_emag_price(url)
        print("Preț:", pret)
    elif opt == "2":
        create_quiz()
    elif opt == "3":
        send_teams_message(user_messages)
    elif opt == "4":
        posts = extract_x_posts(max_posts=4)
        create_html_feed(posts)
    elif opt == "5":
        conversation()
    else: 
        print("Opțiune invalidă.")

if __name__ == "__main__":
    main()

