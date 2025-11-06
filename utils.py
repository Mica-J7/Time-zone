from datetime import datetime
import pytz

def convert_time(hour_str, tz_from_key, tz_to_key):
    tz_from = pytz.timezone(tz_from_key)
    tz_to = pytz.timezone(tz_to_key)
    h, m = map(int, hour_str.split(":"))
    now = datetime.now()
    dt_from_naive = datetime(now.year, now.month, now.day, h, m)
    dt_from = tz_from.localize(dt_from_naive)
    dt_to = dt_from.astimezone(tz_to)
    return dt_to.strftime("%H:%M")

def get_diff_hours(tz1_key, tz2_key):
    tz1_dt = pytz.timezone(tz1_key).localize(datetime.now())
    tz2_dt = pytz.timezone(tz2_key).localize(datetime.now())
    return (tz1_dt - tz2_dt).total_seconds() / 3600