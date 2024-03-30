from Bot import *


if __name__ == "__main__":
    ui = ConsoleUI()
    bot = Bot(ui)

    while True:
        action = ui.get_input("Enter action (add, search, edit, remove, save, load, congratulate, view, exit): ")
        bot.handle(action)
        if action == 'exit':
            break
