import os

running = True

current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

def change_directory(command:list[str], token_no:int):
    os.chdir(command[token_no + 1])
    current_directory = os.getcwd()
    print(f"{current_directory}")

while running:
    current_command = input(">")

    tokens = current_command.split(" ")

    for i in range(0, len(tokens), 1):
        if(tokens[i] == "cd"):
            change_directory(tokens, i)

        if(tokens[i] == "quit"):
            running = False