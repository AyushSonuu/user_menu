from database import add_entry,view_entry

menu = """please select on of the following action:
1) aAd new entry for today.
2) View entries
3) Exit.

Your selection: """

welcome = "welcome to programming dairy"

# user_input = input(menu)
# entries = [
#     {"content":"today i started learning programming.","date":"01-01-2020"}
#     {"content":"today i created my first sqlite database.","date":"02-01-2020"}
#     {"content":" i finished writing my programming dairy application.","date":"03-01-2020"}
#     {"content":"today iam going to lcontinue programming","date":"04-01-2020"}
# ]

print(welcome)

while (user_input := input(menu)) != "3" :
    #dealing with the user input
    # user_input = input(menu)
    if user_input=="1":
        add_entry()
    elif user_input=="2":
        view_entry()
    else:
        print("invalid option. please choose any of the available options")
