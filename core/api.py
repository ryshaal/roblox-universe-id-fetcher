"""Roblox API interaction functions"""

import requests
import time
from colorama import Fore

from .config import ROBLOX_API_URL, API_TIMEOUT
from .utils import clear_screen, loading_animation
from .ui import print_header, print_separator, display_success, display_error


def get_universe_id(place_id):
    """Fetch Universe ID from Roblox API"""
    url = ROBLOX_API_URL.format(place_id)
    loading_animation("Connecting to Roblox API", 1.2)

    start = time.time()
    try:
        response = requests.get(url, timeout=API_TIMEOUT)
        elapsed = round(time.time() - start, 3)

        clear_screen()
        print_header()

        if response.status_code == 200:
            data = response.json()
            universe_id = data.get("universeId")

            if universe_id:
                display_success(place_id, universe_id, elapsed)
            else:
                display_error('invalid', "Response did not contain 'universeId'.")
                print(f"{Fore.WHITE}Raw data: {data}")
                
        elif response.status_code == 404:
            display_error('not_found', "Place ID not found.", 
                         f"The Place ID '{place_id}' does not exist.")
                         
        elif response.status_code == 400:
            display_error('bad_request', "Bad request.", 
                         f"The Place ID '{place_id}' is invalid.")
        else:
            display_error('api_error', "Failed to fetch data from API.")
            print(f"{Fore.WHITE}Status Code : {response.status_code}")
            print(f"{Fore.WHITE}Response    : {response.text[:200]}")

    except requests.Timeout:
        clear_screen()
        print_header()
        display_error('timeout', "Request timed out after 10 seconds.",
                     "Please check your connection and try again.")
                     
    except requests.ConnectionError:
        clear_screen()
        print_header()
        display_error('connection', "Connection error occurred.",
                     "Please check your internet connection.")
                     
    except requests.RequestException as e:
        clear_screen()
        print_header()
        display_error('request', f"An error occurred: {str(e)[:50]}")
        
    except ValueError:
        clear_screen()
        print_header()
        display_error('invalid', "Invalid response format from API.")
        
    except Exception as e:
        clear_screen()
        print_header()
        display_error('unexpected', f"Unexpected error: {str(e)[:50]}")

    print_separator()