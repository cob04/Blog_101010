# cli.py

from users import User


users = {}


def main():
    print("Welcome to the #101010 microblog")
    print("You start here by creating an account.")
    username = input("Enter your username:  ")
    password = input("Enter your password:  ")
    # create an new user and log then in.
    user = User(username, password)
    users[user.username] = user
    login_user = user.login(username, password)
    print("\n")
    print(f"Welcome, {user.username}\n")

    exit = None
    while not exit:
        if login_user:
            print("You are now logged in!")

            # prompt for comment.
            stop = None
            while not stop:
                message = input(f"hey{login_user},  make a new comment below"
                                " or press s to do something else, \n >>  ")
                if message == 's':
                    stop = 's'
                    break

                new_comment = login_user.create_comment(message)
                if new_comment:
                    print("------------------------------------------")
                    print(f"author:  {new_comment.author}")
                    print(f"message: {new_comment.message}")
                    print("----------------------------------------")

            if login_user.view_comments():
                for index, comment in enumerate(login_user.view_comments()):
                    print(f"------ Comment: NO {index + 1} ------")
                    print(f"author:  {comment.author}")
                    print(f"message: {comment.message}")
                    print("------------------------------------------")
            else:
                print("------------------------------------------")
                print("Sorry, We have no comments to show you.")

            stop_edit = None
            while not stop_edit:
                choice = input("Press 1 to edit your comments, "
                               "0 to disregard: ")
                if int(choice) == 1:
                    message_index = input("Enter the NO of the message"
                                          " to edit: ")
                    try:
                        i = int(message_index) - 1
                        edit_comment = login_user.view_comments()[i]
                        print(f"{edit_comment.message}")
                        print('')
                        new_message = input("Enter the new message to "
                                            "replace: ")
                        login_user.edit_comment(edit_comment, new_message)
                        print("Comment updated.")
                        print(f"{edit_comment.message}\n")
                    except IndexError:
                        print("No such comment found.")
                elif int(choice) == 0:
                    stop_edit = 0
                    break
                else:
                    print("Plesase enter either 1 or 0")
        print("------------------------------------------")
        exit = input("To logout the app just Enter x to exit: \n")


if __name__ == "__main__":
    main()
