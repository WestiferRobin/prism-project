

def handle_hotkey(ascii_char: chr) -> bool:
    return ascii_char == 'e'


def handle_input(root_path: str) -> bool:
    command = input(f"{root_path}:> ")
    if len(command) == 0:
        return True
    elif len(command) == 1:
        return command[0].lower() == 'e'
    else:
        return command.lower() == 'exit'

