months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")

        # Format: M/D/YYYY
        if "/" in date:
            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break

        # Format: Month D, YYYY
        elif "," in date:
            month, rest = date.split(" ", 1)
            day, year = rest.split(",")

            month = month.strip()
            day = int(day.strip())
            year = int(year.strip())

            if month in months and 1 <= day <= 31:
                month = months.index(month) + 1
                print(f"{year:04}-{month:02}-{day:02}")
                break

    except (ValueError, IndexError):
        pass
