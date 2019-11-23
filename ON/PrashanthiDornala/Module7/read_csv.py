import csv

#file=open('city-of-seattle-wage-data.csv')
#file_reader=csv.reader(file)
#file_data=list(file_reader)

#print(file_data[0])

#print(file_data[1])

#print(file_data[0][4])

def max_rate():
    max_hourly_rate=float(file_data[1][4])
    name=''
    dept=''
    job_title=''
    for i in range(1,len(file_data)):
        if float(file_data[i][4])>max_hourly_rate:
            max_hourly_rate=float(file_data[i][4])
            name=file_data[i][2]+''+file_data[i][1]
            dept=file_data[i][0]
            job_title=file_data[i][3]
    return(name,dept,job_title,max_hourly_rate)

def low_rate():
    low_hourly_rate=[]
    for i in range(1,len(file_data)):
        low_hourly_rate.append(float(file_data[i][4]))
    return min(low_hourly_rate)

def search_job_titles(words):
    count=0
    for i in range(1,len(file_data)):
        if words in file_data[i][0].lower():
            count+=1
    percent=(count/(len(file_data)-1))*100
    return(words,count,round(percent,2))

if __name__=="__main__":
    file=open('city-of-seattle-wage-data.csv')
    file_reader=csv.reader(file)
    file_data=list(file_reader)
    print("# of Rows:",file_reader.line_num)
    print("# of columns:", len(file_data[0]))
    n,d,j,m=max_rate()
    print("\nInformatin of highest-rated employee:\n")
    print("Name: {}\nDepartment: {}\nJob Title: {}\nHourly Rates: {}\n".format(n,d,j,m))

    l=low_rate()
    print("Lowest hourly rate fount on Seattle Database: {}".format(l))

    w,c,p=search_job_titles('tech')
    print("Jobs thet contain '{}' appear {} times which is {} percents".format(w,c,p))