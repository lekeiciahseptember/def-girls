import menu


def chat(menu):
    "Platform where users can ask questions and get answers"

    # If someone inputs something or "hello" teh chatbot shoulld respond with a greeting 
    
    user = input()

    if user == "Hello":
        print("Hello! Welcome to SheHealthMatters, choose a catergory? ")

    if menu == "Mental health":
        menu.mentalHealth()

    elif menu == "Physical Health":
        menu.physicalHealth()
    
    elif menu == "Pregnancy":
        menu.Pregnancy()

    elif menu == "Abortion":
        menu.Abortion()

    elif menu == "Postnatal":
        menu.Postnatal()

    