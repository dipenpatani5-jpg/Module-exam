
# Custom Module: datetools.py

DATE_FORMAT = "%Y-%m-%d"


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def day_name(text):
    import datetime

    date = datetime.datetime.strptime(text, DATE_FORMAT)
    return date.strftime("%A")


# Main Guard
if __name__ == "__main__":
    print("Testing datetools directly")
    print(is_leap_year(2024), day_name("2026-01-01"))
