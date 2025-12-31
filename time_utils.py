from datetime import datetime


def current_time():
    """
    Mengembalikan waktu sekarang dalam format string.
    """
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
