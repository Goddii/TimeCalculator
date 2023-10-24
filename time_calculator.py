
def add_time(start, duration, day=None):

    days_of_week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

    start_time, period  = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    duration_hour, duration_minute = map(int, duration.split(':'))

    if period.lower() == 'pm':
        start_hour += 12

    total_minutes = start_hour*60 + start_minute + duration_hour*60 + duration_minute

    # convert total minutes from adding start and duration back to hours and minutes
    end_hours, end_minutes = divmod(total_minutes, 60)
    end_day = end_hours // 24
    end_hours = end_hours % 24

    # convert back to 12hr format
    period = 'AM' if end_hours < 12 else 'PM'
    end_hours = end_hours if 0 < end_hours <= 12 else abs(end_hours-12)

    time_string = f'{end_hours}:{end_minutes:02d} {period}'

    if day:
        day_index = (days_of_week.index(day.lower()) + end_day) % 7
        time_string += f',{days_of_week[day_index].capitalize()}'

    if end_day == 1:
        time_string += '(next day)'
    elif end_day > 1:
        time_string += f', {end_day} days later'

    return time_string

print(add_time('3:00 PM', '3:10'))
print(add_time('11:30 AM', '2:32', 'Monday'))
print(add_time('11:43 AM', '00:20'))
print(add_time('10:10 PM', '3:30'))
print(add_time('11:43 PM', '24:20', 'Tuesday'))
print(add_time('6:30 PM', '205:12'))





