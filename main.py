def attack():
    print("You attack!")


switcher = {
    "a":attack,
    "attack":attack,
    "equip":equip
}

def unknown_action():
    print("Unknown action, please try again.")
    get_action()

def get_action():
    user_input = input("What do you want to do? \n").lower()
    switcher.get(user_input, unknown_action)()


if __name__ == "__main__":
    print("hello world")
    get_action()
