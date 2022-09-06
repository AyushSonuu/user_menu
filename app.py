from database import add_entry,get_entry,create_table

menu = """please select on of the following action:
1) Aad new entry for today.
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

def promp_new_entry():
    '''adds new entry to the prompt'''
    entry_content = input("what have you learned today")
    entry_date = input("enter the date")
    add_entry(entry_content, entry_date)

def view_entries(entries):
    '''displays entry present in the  prompt'''
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")

print(welcome)
create_table()

while (user_input := input(menu)) != "3" :
    #dealing with the user input
    # user_input = input(menu)
    if user_input=="1":
        promp_new_entry()

    elif user_input=="2":
        entries=get_entry()
        view_entries(entries)

    else:
        print("invalid option. please choose any of the available options")
