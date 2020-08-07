from os import system
import keyboard
import sqlite3 
from schedule import Schedule

conn = sqlite3.connect("schedule.db") 

# c.execute("""CREATE TABLE schedule(
#     time integer,
#     name text,
#     message text
#     )""")

# conn.commit()

def newschedule(time, name, what_it_will_print):
    c = conn.cursor()
    c.execute("INSERT INTO " + dbname + " VALUES ('" + str(time) + ", " + name + ", " + what_it_will_print + ")")
    c.close()

def printall():
    c = conn.cursor()
    c.execute("SELECT * FROM schedule")
    print(c.fetchall())
    conn.commit()
    c.close()

# def deleteschedule(row):
#     pass



class NewSchedule:
    def __init__(self, time, name, message):
        self.time = time
        self.name = name 
        self.message = message
    def __repr__(self):
        return "schedule('{}', '{}', '{}')".format(self.time, self.name, self.message) 

def main():
    newschedule("10", "test", "test")
    while True:
        new_schedule_breakcheck = False
        #creating cursor to execut sqlcommand 
        printall()
        print('press "n" to make new shedule')
        print('press "d" to delete the schedule')
        if keyboard.is_pressed("n"):#new shedule
            while True:
                #break if the new_schedule_breakcheck is true, default : False
                if new_schedule_breakcheck == True: break
                system("cls")
                print("enter the name of the new shedule")
                new_schedule_name = input(">>> ")
                system("cls")
                print("enter the time which this will execute")
                new_schedule_time = input(">>> ")
                system("cls")
                print("enter what the message is")
                new_scheduraw_message = input(">>> ")
                system("cls")
                print("is this corre\nthe name : " + new_schedule_name + "\nthe time : " + new_schedule_time + "\ntge message : " + new_scheduraw_message)
                while True:
                    print("yes[y] no[n]")
                    new_schedule_yes_no = input(">>> ")
                    if new_schedule_yes_no == "y":
                        system("cls")
                        print("great")
                        new_schedule_breakcheck = True
                        newschedule(new_schedule_time, new_schedule_name, new_scheduraw_message)
                        break
                    else:
                        system("cls")
                        print("please enter y or n")
                        sleep(3)
                        system("cls")
    
        elif keyboard.is_pressed("d"):
            pass
        else:
            #main loop
            while True:
                pass
                
conn.close()

if __name__ == "__main__":
    main()