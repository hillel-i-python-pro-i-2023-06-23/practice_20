import pytz


def get_timezone_by_city(city_name):
    try:
        timezone = pytz.timezone(city_name)
        return timezone
    except pytz.UnknownTimeZoneError:
        return None
