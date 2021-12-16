import datetime
import os
import itertools

def interval_proc(series):
    interval_series=[]
    for line in fh:
        interval_list=[]
        el1=line.strip()
        el2=next(fh).strip()
        el1_d=datetime.datetime.strptime(el1,"%H:%M:%S")
        el2_d=datetime.datetime.strptime(el2,"%H:%M:%S")
        interval_list.append(el1_d)
        interval_list.append(el2_d)
        delta_time = el2_d - el1_d
        interval_list.append(str(delta_time))
        intervel_series = interval_series.append(interval_list)
        print(delta_time)

def split_clock_time(Time):
    ctime=[]
    ctime = Time.split(":")
#    print(ctime)
    Hour=ctime[0]
    Minute=ctime[1]
    Seconds=ctime[2]
    return([Hour,Minute,Seconds])

def collate(Month,Day,Time,Year,Connections):
    Hours, Minutes, Seconds = split_clock_time(Time)
    print("Month: {}\nDay: {}\nYear: {}\nHours: {}\nMinutes: {}\nSeconds: {}\nConnections: {}\n\n ".format(Month,Day,Year,Hours,Minutes,Seconds,Connections))


# sdr.stats:SDR Stats at ---- ----Mon Dec 13 00:05:06 2021
# 0 sdr.stats:SDR
# 1 Stats
# 2 at
# 3 ----
# 4 ----Mon
# 5 Dec
# 6 13
# 7 00:05:06
# 8 2021


with open("conn_histry.txt", "r+") as fh:
    el1=[]
    el2=[]
    for line in fh:
        line=line.strip()
        el1=line.split(" ")
        try:
            el1.remove("")
        except:
            pass
#        print(el1)
        Month=(el1[5])
#        print('Month: {}'.format(Month))
        Day=(el1[6])
#        print('Day: {}'.format(Day))
        Time=(el1[7])
#        print('Time: {}'.format(Time))
        Year=(el1[8])
#        print('Year: {}'.format(Year))
#        exit()
        line=next(fh)
        line=line.strip()
        el2=line.split(" ")
        Connections=(el2[1])
        collate(Month,Day,Time,Year,Connections)






