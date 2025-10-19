"""Network operations and API calls"""

import requests

from .config import CONNECTION_TEST_URL, CONNECTION_TIMEOUT


def check_internet():
    """Check internet connectivity"""
    try:
        requests.get(CONNECTION_TEST_URL, timeout=CONNECTION_TIMEOUT)
        return True
    except requests.ConnectionError:
        return False
    except Exception:
        return False