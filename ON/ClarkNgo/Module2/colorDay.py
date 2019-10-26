import datetime
import calendar

def color_of_mybirthday(date):
    # return 0 - 6
    born = datetime.datetime.strptime(date, '%m/%d/%Y').weekday()
    day = calendar.day_name[born]
    if day == 'Sunday':
        return 'Red'
    elif day == 'Monday':
        return 'Yellow'
    elif day == 'Tuesday':
        return 'Pink'
    elif day == 'Wednesday':
        return 'Green'
    elif day == 'Thursday':
        return 'Orange'
    elif day == 'Friday':
        return 'Blue'
    elif day == 'Saturday':
        return 'Purple'

day = input("What is ur birthday? (mm/dd/yyy): ")
color = color_of_mybirthday(day)
print("Color of my Birthday: " + color)
