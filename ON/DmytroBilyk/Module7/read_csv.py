import csv

def max_rate():
    max_hourly_rate = float(file_data[1][4])
    name = ''
    dept = ''
    job_title = ''

    for i in range(1, len(file_data)):
        # compare each value one by one from first to last
        if float(file_data[i][4]) > max_hourly_rate:
            max_hourly_rate = float(file_data[i][4])
            name = file_data[i][2] + ' ' + file_data[i][1]
            dept = file_data[i][0]
            job_title = file_data[i][3]
    return (name, dept, job_title, max_hourly_rate)

def low_rate():
    low_hourly_rate = []
    for i in range(1, len(file_data)):
        low_hourly_rate.append(float(file_data[i][4]))

    return min(low_hourly_rate)                        

def search_job_titles(words):
    count = 0
    for i in range(1, len(file_data)):
        if words in file_data[i][0].lower():
            count += 1
    percent = (count/(len(file_data) -1)) * 100
    return (words, count, round(percent, 2))

if __name__ == "__main__":
    file = open('city-of-seattle-wage-data.csv')
    file_reader = csv.reader(file)
    file_data = list(file_reader)
    print("# of Rows:", file_reader.line_num)
    print("# of Columns:", len(file_data[0]))

    n, d, j, m = max_rate()
    print("\nInformation of highest-rated employee:\n")
    print("Name: {}\nDepartment: {}\nJobTitle: {}\nHourly Rate: {}\n".format(n, d, j, m))

    w, c, p = search_job_titles('tech')
    print("Jobs that contain '{}' appear {} times which is {} percents".format(w, c, p))
