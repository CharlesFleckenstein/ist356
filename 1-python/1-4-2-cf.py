import datetime

def parse_date_mdy(date: str) ->datetime:
    return datetime.datetime.strptime(date, "%m/%d/%Y")


def format_date_ymd(date: datetime.datetime) -> str:
    return date.strftime("%Y-%m-%d")


date = '12/30/2024'
date_dt = parse_date_mdy(date)
date_str = format_date_ymd(date_dt)
print(date, date_str) # 2024-12-30