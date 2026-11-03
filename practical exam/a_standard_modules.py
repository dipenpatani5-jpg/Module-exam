
from datetime import datetime, timedelta


# Q1. Check Leap Year
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


years = [1900, 2000, 2024, 2023, 2100]

for year in years:
    print(year, is_leap_year(year))


# Q2. Find Day of Week
def day_of_week(text):
    date = datetime.strptime(text, "%Y-%m-%d")
    return date.strftime("%A")


dates = ['2026-01-01', '2026-03-08', '2026-12-25']

for date in dates:
    print(date, day_of_week(date))


# Q3. Calculate Number of Days
date1 = datetime(2026, 1, 1)
date2 = datetime(2026, 12, 31)

difference = date2 - date1

print(difference.days)


# Q4. Format Date and Time
now = datetime(2026, 3, 8, 14, 30, 45)

print(now.strftime("%d-%m-%Y"), now.strftime("%m/%d/%Y"))

print(now.strftime("%H:%M:%S"), now.strftime("%I:%M:%S %p"))


# Q5. Add 2 Weeks, 3 Days and 5 Hours
new_date = now + timedelta(weeks=2, days=3, hours=5)

print(new_date.strftime("%Y-%m-%d %H:%M:%S"))



import math
import random


# Q1. Bus Calculation
passengers = 47
bus_capacity = 10

buses = math.ceil(passengers / bus_capacity)

print(buses)


# Q2. Convert Seconds into Hours, Minutes and Seconds
total_seconds = 3725

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(hours, minutes, seconds)


# Q3. Simplify Fraction
def simplify(n, d):
    gcd = math.gcd(n, d)

    return (n // gcd, d // gcd)


print(simplify(24, 36))


# Q4. Calculate Tower Height
dist = 50
angle = 30

height = dist * math.tan(math.radians(angle))

print(round(height, 2))


# Q5. Roll a Die 5 Times
random.seed(12)

rolls = []

for i in range(5):
    rolls.append(random.randint(1, 6))

print(rolls, sum(rolls))


# Q6. Shuffle Deck and Play Rock Paper Scissors
deck = list(range(1, 9))

random.shuffle(deck)

print(deck)

print(random.choice(["rock", "paper", "scissors"]))


import uuid
import time
from datetime import datetime, timezone


# Q1. Generate UUID5 for Different Names
names = ['Asha', 'Ravi', 'Meena', 'Karan']

ids = {}

for name in names:
    ids[name] = uuid.uuid5(
        uuid.NAMESPACE_DNS,
        name.lower() + ".example"
    )

for name, value in ids.items():
    print(name, str(value)[:8])

print(len(set(ids.values())) == len(ids))


# Q2. Compare UUID3 and UUID5
uuid3_value = uuid.uuid3(uuid.NAMESPACE_DNS, "example.com")
uuid5_value = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")

print(
    uuid3_value != uuid5_value,
    uuid3_value.version,
    uuid5_value.version
)


# Q3. Time Module and Date Formatting
ts = 31536000

gmt = time.gmtime(ts)

print(time.strftime("%Y-%m-%d %H:%M:%S", gmt))

print(time.asctime(time.gmtime(ts)))

date = datetime.fromtimestamp(ts, timezone.utc)

print(date.strftime("%d %b %Y"))


# Q4. Measure Execution Time
start = time.perf_counter()

total = sum(range(1_000_000))

end = time.perf_counter()

elapsed = end - start

print(total, type(elapsed).__name__, elapsed >= 0)
