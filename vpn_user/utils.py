import datetime

def date_range(start_date, end_date):
    """Returns a generator of all the days between two datetime objects.
   
    :param start_date: datetime obj
    :param end_date: datetime obj

    :return generater: yield all dates as datetime obj between start_date and
                       end_date 
    """
    date_arr = []
    while True:
        date_arr.append(start_date)
        start_date += datetime.timedelta(days=1)
        if start_date > end_date:
            break
    return date_arr
