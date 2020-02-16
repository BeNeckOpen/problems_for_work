import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE lessons
                  (id text primary key not null, event_id text not null, subject varchar not null,
                   scheduled_time datetime not null)
               """)
cursor.execute("""CREATE TABLE quality
                  (lesson_id text not null, tech_quality tinyint, foreign key (lesson_id) references lessons(id))
               """)
cursor.execute("""CREATE TABLE users
                  (id text not null, role text not null)
               """)
cursor.execute("""CREATE TABLE participants
                  (event_id text not null, user_id text not null, foreign key (user_id) references users(id))
               """)


def parsings():
    min = 6
    sum = 0
    count = 0
    f = open('lessons.txt', 'r')
    list_ = [list_.split('|') for list_ in f]
    list_.pop(0)
    list_.pop(0)
    list_.pop()
    list_.pop()
    for i in list_:
        i[3] = i[3].replace('\n','')
    cursor.executemany("INSERT INTO lessons VALUES (?,?,?,?)", list_)
    f.close()
    conn.commit()

    f = open('quality.txt', 'r')
    list_ = [list_.split('|') for list_ in f]
    list_.pop(0)
    list_.pop(0)
    list_.pop()
    list_.pop()
    for i in list_:
        i[1] = i[1].replace('\n', '')
    cursor.executemany("INSERT INTO quality VALUES (?,?)", list_)
    f.close()
    conn.commit()

    f = open('users.txt', 'r')
    list_ = [list_.split('|') for list_ in f]
    list_.pop(0)
    list_.pop(0)
    list_.pop()
    list_.pop()
    for i in list_:
        i[1] = i[1].replace('\n', '')
    cursor.executemany("INSERT INTO users VALUES (?,?)", list_)
    f.close()
    conn.commit()

    f = open('participants.txt', 'r')
    list_ = [list_.split('|') for list_ in f]
    list_.pop(0)
    list_.pop(0)
    list_.pop()
    list_.pop()
    for i in list_:
        i[1] = i[1].replace('\n', '')
    cursor.executemany("INSERT INTO participants VALUES (?,?)", list_)
    f.close()
    conn.commit()
    for i in range(11, 21):
        sqltest = "SELECT id, event_id FROM lessons WHERE scheduled_time LIKE ' 2020-01-"+str(i)+"%' AND subject = ' phys    '"
        cursor.execute(sqltest)
        some = cursor.fetchall()
        for item in some:
            sql_2 = "SELECT tech_quality FROM quality WHERE lesson_id = '"+item[0]+"'"
            cursor.execute(sql_2)
            quality_data = cursor.fetchall()
            sql_3 = "SELECT user_id FROM participants WHERE event_id = '"+item[1]+"'"
            cursor.execute(sql_3)
            some3 = cursor.fetchall()
            for item_2 in some3:
                sql_4 = "SELECT role FROM users WHERE id = '"+item_2[0]+" '"
                cursor.execute(sql_4)
                role = cursor.fetchall()
                if role[0][0] == ' tutor':
                    teach = item_2[0]
            for mark in quality_data:
                if type(mark[0]) == type(1):
                    sum = sum+mark[0]
                    count = count+1
            if count == 0:
                actual_sum = 0
            else:
                actual_sum = float(sum)/count
            sum = 0
            count = 0
            if (actual_sum < min) and (actual_sum > 0):
                min = actual_sum
                bad_teach = teach
        print('2020-01-'+str(i) +' ' + bad_teach + ' ' + str(min))
        bad_teach = None
        actual_sum = 0
        min = 6

parsings()