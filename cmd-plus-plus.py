import os

running = True

current_line = 0

border = "    | "

current_directory = os.getcwd()
print(f"{border}Current working directory: {current_directory}")

def change_directory(command:list[str], token_no:int):
    os.chdir(command[token_no + 1])
    current_directory = os.getcwd()
    print(f"{border}{current_directory}")

def list_directory_contents(command:list[str], token_no:int):
    if(token_no + 1 < len(command)):
        files = os.listdir(command[token_no + 1])
        print_sequence(files, True)
    else:
        files = os.listdir(os.getcwd())
        print_sequence(files, True)

def print_sequence(sequence:list[str], showing_files:bool):
    file_display_sequence = []

    files = []
    directories = []

    for name in sequence:
        if "." in name:
            directories.append(name)
        else:
            files.append(name)

    file_display_sequence = files + directories
            
    if(showing_files):
        for j in range(0, len(file_display_sequence), 1):
            print(f"{border}{file_display_sequence[j]}")

while running:
    current_command = input(f"{current_line:<2}. | >")
    current_line += 1

    tokens = current_command.split(" ")

    for i in range(0, len(tokens), 1):
        if(tokens[i] == "cd" or tokens[i] == "goto"):
            change_directory(tokens, i)

        if(tokens[i] == "ls" or tokens[i] == "show"):
            list_directory_contents(tokens, i)

        if(tokens[i] == "quit"):
            running = False