"""User interface and display functions"""

from colorama import Fore, Style

from .config import APP_TITLE, SEPARATOR


def print_header():
    """Print application header"""
    print(Style.BRIGHT + Fore.MAGENTA + SEPARATOR)
    print(Style.BRIGHT + Fore.MAGENTA + f"         🔎 {APP_TITLE}")
    print(Style.BRIGHT + Fore.MAGENTA + SEPARATOR + "\n")


def print_separator():
    """Print separator line"""
    print("\n" + Fore.MAGENTA + SEPARATOR)


def display_success(place_id, universe_id, elapsed):
    """Display successful result"""
    print(f"{Fore.GREEN}✓ Successfully retrieved data in {elapsed}s\n")
    print(f"{Fore.YELLOW}📦 Place ID   : {Fore.WHITE}{place_id}")
    print(f"{Fore.CYAN}🌐 Universe ID: {Fore.WHITE}{universe_id}")


def display_error(error_type, message, details=None):
    """Display error message"""
    icons = {
        'not_found': '❌',
        'bad_request': '❌',
        'api_error': '❌',
        'timeout': '⏰',
        'connection': '📡',
        'request': '💥',
        'invalid': '⚠️',
        'unexpected': '💥'
    }
    
    icon = icons.get(error_type, '⚠️')
    print(f"{Fore.RED}{icon} {message}")
    
    if details:
        print(f"{Fore.YELLOW}⚠️  {details}")


def display_validation_error(error_message):
    """Display validation error"""
    print(f"\n{Fore.RED}❌ Invalid input: {error_message}")
    print(f"{Fore.YELLOW}Example: 1818 or 292439477")


def display_no_internet():
    """Display no internet connection message"""
    print(f"{Fore.RED}📡 No internet connection detected.")
    print(f"{Fore.YELLOW}⚠️  Please check your network and try again.")


def prompt_place_id():
    """Prompt user for Place ID"""
    return input(f"{Fore.YELLOW}Enter Roblox Place ID: {Fore.WHITE}").strip()


def wait_for_exit():
    """Wait for user input before exiting"""
    print(f"\n{Fore.CYAN}Press Enter to exit...", end="")
    try:
        input()
    except (KeyboardInterrupt, EOFError):
        print()