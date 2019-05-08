
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yearNames = ["normal-year", "leap-year"]
dayNames = ["Mon.", "Tue.", "Wed.", "Thu", "Fri", "Sat.", "Sun"]

def friday13th():
    for leap in range(2):
        for firstDay in range(7):
            day, count = firstDay, 0
            for month in range(12):
                if(day + (13 - 1))%7==4:
                    count += 1
                day += days[month] + (leap if month == 1 else 0)
            # print(f"# Friday 13ths's [jan 1st: {da")