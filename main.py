"""Main program entry point for Roblox Universe ID Fetcher"""

import sys
from colorama import init, Fore

from core.utils import clear_screen, validate_place_id
from core.network import check_internet
from core.ui import (print_header, prompt_place_id, display_validation_error, 
                     display_no_internet, wait_for_exit)
from core.api import get_universe_id

# Initialize colorama
init(autoreset=True)


def main():
    """Main program entry point"""
    clear_screen()
    print_header()

    place_id = prompt_place_id()

    # Validate Place ID
    is_valid, error_message = validate_place_id(place_id)
    if not is_valid:
        display_validation_error(error_message)
        sys.exit(1)

    print()
    
    # Check internet connection
    if not check_internet():
        display_no_internet()
        sys.exit(1)

    get_universe_id(place_id)
    
    # Wait for user input before closing
    wait_for_exit()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}⚠️  Program interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}💥 Fatal error: {str(e)}")
        sys.exit(1)