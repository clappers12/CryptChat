import re
from datetime import datetime

def validate_email(email):
    """ Validates if the input string is a valid email address. """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def format_message(username, message):
    """ Formats a chat message with a timestamp. """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"[{timestamp}] {username}: {message}"

def sanitize_string(input_string):
    """ Removes potentially harmful characters or tags from a string. """
    return re.sub(r'[<>]', '', input_string)

# Add more utility functions as needed
