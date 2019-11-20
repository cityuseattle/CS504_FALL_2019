import csv

def max_rate():
    # we know where the hourly rate column is, last column from 0-4
    # put first value from hourly rate to max_hourly_rate
    max_hourly_rate = float(file_data[1][4])
    name = ''
    dept = ''
    job_title = ''
    for i in range(1, len(file_data)):
        # compare each value 1 by 1 from first to last
        if float(file_data[i][4]) > max_hourly_rate:
            # if current element is greater, update max_hourly_rate
            max_hourly_rate = float(file_data[i][4])
            name = file_data[i][2] + ' ' + file_data[i][1]
            dept = file_data[i][0]
            job_title = file_data[i][3]
    return (name, dept, job_title, max_hourly_rate)

def low_rate():
    low_hourly_rate = []
    for i in range(1, len(file_data)):
        # add everything to list, low_hourly_rate
        low_hourly_rate.append(float(file_data[i][4]))
    # another way to find min or max value
    # in this case, use min() to get minimum value from the list
    return min(low_hourly_rate)

def search_job_titles(words):
    count = 0
    for i in range(1, len(file_data)):
        # file_data[i][0] will go through the first column of value to the end
        if words in file_data[i][0].lower():
            count += 1
    percent = (count/(len(file_data)-1)) * 100
    return (words, count, round(percent, 2)) # round (number, # of decimal)

if __name__ == "__main__":
    file = open('city-of-seattle-wage-data.csv')
    file_reader = csv.reader(file)
    file_data = list(file_reader)
    print("# of Rows:", file_reader.line_num)
    print("# of Columns:", len(file_data[0]))
    # (name, dept, job_title, max_hourly_rate) returned from max_rate
    n, d, j, m = max_rate()
    print("\nInformation of highest-rated employee:\n")
    print("Name: {}\nDepartment: {}\nJob Title: {}\nHourly Rate: {}\n".format(n, d, j, m))
    # (words, count, round(percent, 2)) returned from search_job_titles()
    w, c, p = search_job_titles('tech')
    print("Jobs that contain '{}' appear {} times which is {} percents".format(w, c, p))
