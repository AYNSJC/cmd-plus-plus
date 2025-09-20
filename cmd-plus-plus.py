import os

running = True

current_line = 0

border = "     | "

current_directory = os.getcwd()

custom_commands:list[str] = ["cd", "ls", "mkdir", "rmdir", "ren", "preset","cls", "quit"]

def start_cmd():
    global running
    global current_directory
    global current_line

    os.system("cls")

    running = True

    current_line = 0

    current_directory = os.getcwd()

def change_directory(command:list[str]):
    global current_directory
    os.chdir(" ".join(command[1:]))
    current_directory = os.getcwd()
    print(f"{border}{current_directory}")

def list_directory_contents(command:list[str], token_no:int):
    if(token_no + 1 < len(command)):
        files = os.listdir(" ".join(command[1:]))
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

def create_new_directory(command:list[str]):
    os.mkdir(" ".join(command[1:]))
    print(f"{border}Success!")

def remove_directory(command:list[str]):
    os.rmdir(" ".join(command[1:]))
    print(f"{border}Success!")

def rename_directory(command:str):
    tokens = command.split('"')
    os.rename(tokens[1], tokens[3])
    print(f"{border}Success!")
    
def make_preset():
    global custom_commands
    for i in range(0, len(custom_commands), 1):
        custom_commands[i] = input(f"{border}{custom_commands[i]}: ")

while running:
    current_command = input(f"{current_line:<3}. | {current_directory}>")
    current_line += 1

    tokens = current_command.split(" ")

    for i in range(0, len(tokens), 1):
        if tokens[i] in ("cd", "goto", "jao", custom_commands[0]):
            if len(tokens) > 1:
                change_directory(tokens)
        elif tokens[i] in ("ls", "show", "dikhao", custom_commands[1]):
            list_directory_contents(tokens, i)
        elif tokens[i] in ("mkdir", "create", "banao", custom_commands[2]):
            if len(tokens) > 1:
                create_new_directory(tokens)
        elif tokens[i] in ("rmdir", "remove", "hatao", custom_commands[3]):
            if len(tokens) > 1:
                remove_directory(tokens)
        elif tokens[i] in ("ren", "rename", "badlo", custom_commands[4]):
            if len(tokens) > 3:
                rename_directory(current_command)
        elif tokens[i] in ("preset", "mera", custom_commands[5]):
            make_preset()
        elif tokens[i] in ("cls", "clear", "saf", custom_commands[6]):
            start_cmd()
        elif tokens[i] in ("quit", "chod", custom_commands[7]):
            running = False
