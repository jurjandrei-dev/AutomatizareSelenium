from tasks.check_price import get_emag_price
#from tasks.forms import complete_form
from tasks.teams import send_teams_message

def main():
    print("1. Verificare preț eMAG")
    print("2. Completați un formular")
    print("3. Trimiteți un mesaj în Teams")
    opt = input("Alege opțiunea: ")

    if opt == "1":
        url = input("Introdu URL produs eMAG: ")
        pret = get_emag_price(url)
        print("Preț:", pret)
    elif opt == "2":
        #complete_form()
        print("Option 2")
    elif opt == "3":
        user_name = input("Scrieti numele persoanei: ")
        message = input("Scrieti un mesaj: ")
        send_teams_message(user_name, message)
    else:
        print("Opțiune invalidă.")

if __name__ == "__main__":
    main()

