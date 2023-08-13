departure_time = '5:25'

hours, minutes = departure_time.split(':')
hours = int(hours)
minutes = int(minutes)

sleep_hours = hours - 8
if sleep_hours < 0:
    sleep_hours += 24

sleep_time = f'{sleep_hours:02}:{minutes:02}'
print(sleep_time)
