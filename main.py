import requests

API_KEY = "e78fab82-7dd7-40f3-aeb2-e70a8d00db5a"


def get_holidays_data(country, month, year, day="0"):
    """returns list of holidays for specific month"""
    api_url_holidays = f"https://holidayapi.com/v1/holidays?pretty&key={API_KEY}" \
        f"&country={country}&year={year}&month={month}&day={day}"
    holiday_data = requests.get(url=api_url_holidays)
    holiday_data = holiday_data.json()

    return holiday_data["holidays"]


def main():
    """Printing all holiday from 16/4/2022 to the end of the year"""
    current_month, day, year = "4", "16", "2022"
    country = "IL"

    # getting holidays for current month from current day for this month
    holidays = get_holidays_data(country, current_month, year, day)

    # adding holidays for rest fo the year
    for month in range(int(current_month)+1, 13):
        str_month = str(month)
        temp_holidays = get_holidays_data(country, str_month, year)
        if temp_holidays:
            holidays.extend(temp_holidays)

    # printing holidays
    for holiday in holidays:
        name, date = holiday["name"], holiday["date"]
        print(f"{name}: {date}")


if __name__ == '__main__':
    main()
