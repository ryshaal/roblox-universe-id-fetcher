"""Core package for Roblox Universe ID Fetcher"""

from .api import get_universe_id
from .network import check_internet
from .ui import (
    print_header,
    print_separator,
    display_success,
    display_error,
    display_validation_error,
    display_no_internet,
    prompt_place_id,
    wait_for_exit
)
from .utils import clear_screen, loading_animation, validate_place_id
from .config import (
    ROBLOX_API_URL,
    CONNECTION_TEST_URL,
    API_TIMEOUT,
    CONNECTION_TIMEOUT,
    APP_TITLE
)

__all__ = [
    'get_universe_id',
    'check_internet',
    'print_header',
    'print_separator',
    'display_success',
    'display_error',
    'display_validation_error',
    'display_no_internet',
    'prompt_place_id',
    'wait_for_exit',
    'clear_screen',
    'loading_animation',
    'validate_place_id',
    'ROBLOX_API_URL',
    'CONNECTION_TEST_URL',
    'API_TIMEOUT',
    'CONNECTION_TIMEOUT',
    'APP_TITLE'
]