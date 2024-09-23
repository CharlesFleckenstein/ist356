import datetime

def parse_date_mdy(date: str) ->datetime:
    return datetime.datetime.strptime(date, "%m/%d/%Y")


def format_date_ymd(date: datetime.datetime) -> str:
    return date.strftime("%Y-%m-%d")

if __name__ == '__main__':
    date = '12/30/2024'
    date_dt = parse_date_mdy(date)
    date_str = format_date_ymd(date_dt)
    print(date, date_str) # 2024-12-30
    date_dt_expect = datetime.datetime(2024, 12, 30)
    date_dt_actual = parse_date_mdy(date)
    assert date_dt_actual == date_dt_expect 

    def test_format_dat_ymf():
        date_dt = datetime.datetime(2024, 12, 30)
        expect = '2024-12-30'
        actual = format_date_ymd(date_dt)
        assert actual == expect
        
