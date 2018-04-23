print("""******************

Alarm Program

******************""")

import time

Ahour = int(input("Please enter the alarm hour:"))
Aminute = int(input("Please enter the alarm minute:"))

while True:
    LT = time.localtime(time.time())
    if Ahour == LT.tm_hour and Aminute == LT.tm_min :
        print( "Time is:", LT.tm_hour, ":", LT.tm_min, "The alarm is ringing")
        break
    elif (LT.tm_min == 30 and LT.tm_sec ==1 ) or (LT.tm_min == 7 and LT.tm_sec ==1 ):
        rhour = Ahour - LT.tm_hour
        rminute= Aminute - LT.tm_min
        print( "Remaining to Alarm:", rhour, ":", rminute)
    else:
        pass

print (" The Alarm Has been terminated")

