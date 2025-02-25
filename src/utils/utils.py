from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def print_color(message, **kwargs):
    color = kwargs.get("color", Fore.WHITE)
    bold = kwargs.get("bold", False)
    style = Style.BRIGHT if bold else Style.NORMAL
    print(f"{color}{style}{message}{Style.RESET_ALL}")
