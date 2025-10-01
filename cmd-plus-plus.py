import os
import re
from prompt_toolkit import prompt
from prompt_toolkit.lexers import Lexer
from prompt_toolkit.formatted_text import FormattedText

running = True
current_line = 0
border = "     | "
current_directory = os.getcwd()
custom_commands: list[str] = ["cd", "ls", "mkdir", "rmdir", "ren", "echo", "preset", "cls", "quit"]

# ------------------------
# Terminal functions
# ------------------------
def start_cmd():
    global running, current_directory, current_line
    os.system("cls")
    running = True
    current_line = 0
    current_directory = os.getcwd()

def change_directory(command: list[str]):
    global current_directory
    os.chdir(" ".join(command[1:]))
    current_directory = os.getcwd()
    print(f"{border}{current_directory}")

def list_directory_contents(command: list[str], token_no: int):
    if token_no + 1 < len(command):
        files = os.listdir(" ".join(command[1:]))
    else:
        files = os.listdir(os.getcwd())
    print_sequence(files, True)

def print_sequence(sequence: list[str], showing_files: bool):
    files = []
    directories = []
    for name in sequence:
        if "." in name:
            files.append(name)
        else:
            directories.append(name)
    file_display_sequence = directories + files
    if showing_files:
        for item in file_display_sequence:
            print(f"{border}{item}")

def create_new_directory(command: list[str]):
    os.mkdir(" ".join(command[1:]))
    print(f"{border}Success!")

def remove_directory(command: list[str]):
    os.rmdir(" ".join(command[1:]))
    print(f"{border}Success!")

def rename_directory(command: str):
    tokens = command.split('"')
    os.rename(tokens[1], tokens[3])
    print(f"{border}Success!")

def echo_statement(command: list[str]):
    text = " ".join(command[1:])
    # Color quoted parts blue in output
    colored_text = re.sub(r'"(.*?)"', lambda m: f"\033[34m\"{m.group(1)}\"\033[0m", text)
    print(f"{border}{colored_text}")

def make_preset():
    global custom_commands
    for i in range(len(custom_commands)):
        custom_commands[i] = input(f"{border}{custom_commands[i]}: ")

# ------------------------
# Real-time input coloring
# ------------------------
def get_colored_fragments(text: str) -> FormattedText:
    fragments = []

    # Highlight first word bright green
    match = re.match(r'\S+', text)
    if match:
        first_word = match.group()
        fragments.append(("fg:#00FF00", first_word))  # bright green
        rest_start = match.end()
    else:
        rest_start = 0

    # Rest of the text, quotes blue
    rest = text[rest_start:]
    parts = re.split(r'(".*?")', rest)
    for p in parts:
        if p.startswith('"') and p.endswith('"'):
            fragments.append(("fg:blue", p))
        else:
            fragments.append(("fg:white", p))

    return FormattedText(fragments)

class InputLexer(Lexer):
    def lex_document(self, document):
        def get_line(lineno):
            return get_colored_fragments(document.text)
        return get_line

# ------------------------
# Main loop
# ------------------------
while running:
    raw_input_text = prompt(f"{current_line:<3}. | {current_directory}> ", lexer=InputLexer())
    if not raw_input_text.strip():
        continue
    current_line += 1

    tokens = raw_input_text.split(" ")

    for i in range(len(tokens)):
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
                rename_directory(raw_input_text)
        elif tokens[i] in ("echo", "tell", custom_commands[5]):
            echo_statement(tokens)
        elif tokens[i] in ("preset", "mera", custom_commands[6]):
            make_preset()
        elif tokens[i] in ("cls", "clear", "saf", custom_commands[7]):
            start_cmd()
        elif tokens[i] in ("quit", "chod", custom_commands[8]):
            running = False
