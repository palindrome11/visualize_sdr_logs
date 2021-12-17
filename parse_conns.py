import datetime
import os
import itertools
import sqlite3

MHASH = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12
}

def db_create(db_name):

    db = sqlite3.connect(db_name)

    db.executescript("""
    
    drop table if exists connections;
    create table connections (
      id integer primary key autoincrement,
      datetime_julian real not null,
      connections integer);
     """)

    db.close()

def db_update_record(db_name, db_record_update):
    db = sqlite3.connect(db_name)
    cursor = db.cursor()
    print("Successfully Connected to {} database",format(db_name))

    sqllite_insert_with_param = ("""
    INSERT INTO connections (datetime_julian, connections) VALUES (?, ?);
    """)
    data_tuple = (db_record_update[0],db_record_update[1])
    cursor.execute(sqllite_insert_with_param, data_tuple)
    db.commit()

    cursor.close()
    db.close()

# This was an older routine that seem to have been ost in space. Need to revisit and possibly reuse the delta time
# logic
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

def month_to_num(Month):
    Month_num = MHASH[Month]
    return(Month_num)


def split_clock_time(Time):
    ctime=[]
    ctime = Time.split(":")
#    print(ctime)
    Hour=ctime[0]
    Minute=ctime[1]
    Seconds=ctime[2]
    return([Hour,Minute,Seconds])

def collate(Month,Day,Time,Year,Connections):
    Month_Num=month_to_num(Month)
    Hours, Minutes, Seconds = split_clock_time(Time)
    jtime=datetime.datetime(int(Year),int(Month_Num),int(Day),int(Hours),int(Minutes),int(Seconds)).timestamp()
    print("Month: {}\nDay: {}\nYear: {}\nHours: {}\nMinutes: {}\nSeconds: {}\nConnections: {}\nJulian Time(UTC): {}\n\n ".format(Month,Day,Year,Hours,Minutes,Seconds,Connections,jtime))
    record = {"Month" : Month_Num,
              "Day" : Day,
              "Year" : Year,
              "Hours" : Hours,
              "Minutes" : Minutes,
              "Seconds" : Seconds,
              "jtime" : jtime,
              "Connections" : Connections
    }
    return(record)

def parse_file(filename, db_name):

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


    with open(filename, "r+") as fh:
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
            record = collate(Month,Day,Time,Year,Connections)
#            print(record['Day'])
            jdate_time = record['jtime']
            connect_no = record['Connections']
            db_record_update = [jdate_time,int(connect_no)]
            db_update_record(db_name,db_record_update)


db_create("connections.db")
parse_file("conn_histry.txt", "connections.db")


