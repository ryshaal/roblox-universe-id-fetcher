"""Utility functions for terminal operations and animations"""

import os
import sys
import time
from colorama import Fore

from .config import LOADING_FRAMES, LOADING_FRAME_DELAY


def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def loading_animation(text="Fetching data", duration=1.0):
    """Display loading animation with configurable duration"""
    end_time = time.time() + duration
    
    while time.time() < end_time:
        for frame in LOADING_FRAMES:
            if time.time() >= end_time:
                break
            sys.stdout.write(f"\r{Fore.CYAN}{text} {frame}")
            sys.stdout.flush()
            time.sleep(LOADING_FRAME_DELAY)
    
    sys.stdout.write("\r" + " " * 60 + "\r")
    sys.stdout.flush()


def validate_place_id(place_id):
    """Validate Place ID input"""
    if not place_id:
        return False, "Place ID cannot be empty."
    
    if not place_id.isdigit():
        return False, "Place ID must contain only numbers."
    
    if len(place_id) < 1:
        return False, "Place ID is too short."
    
    if int(place_id) <= 0:
        return False, "Place ID must be a positive number."
    
    return True, ""