import os

running = True

current_line = 0

current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

def change_directory(command:list[str], token_no:int):
    os.chdir(command[token_no + 1])
    current_directory = os.getcwd()
    print(f"{current_directory}")

def list_directory_contents(command:list[str], token_no:int):
    if(token_no + 1 < len(command)):
        files = os.listdir(command[token_no + 1])
        print_sequence(files)
    else:
        files = os.listdir(os.getcwd())
        print_sequence(files)

def print_sequence(sequence:list[str]):
    for i in range(0, len(sequence), 1):
        print(sequence[i])

while running:
    current_command = input(f"{current_line:<2}. | >")
    current_line += 1

    tokens = current_command.split(" ")

    for i in range(0, len(tokens), 1):
        if(tokens[i] == "cd"):
            change_directory(tokens, i)

        if(tokens[i] == "ls"):
            list_directory_contents(tokens, i)

        if(tokens[i] == "quit"):
            running = False