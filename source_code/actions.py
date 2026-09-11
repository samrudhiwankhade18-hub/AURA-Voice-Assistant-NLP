from datetime import datetime
import webbrowser


def get_time():
    return datetime.now().strftime("%I:%M %p")


def get_date():
    return datetime.now().strftime("%d %B %Y")


def open_website(website):
    webbrowser.open(website)