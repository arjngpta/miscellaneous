# this program interrupts your work every 2 hours
# and launches the courseplay website to encourage you
# to resume your training program!

import webbrowser
import time
total_breaks = 3
break_number = 0

print ("The program started on "+time.ctime())
while break_number < total_breaks:
    time.sleep(2*60*60)
    break_number = break_number + 1
    webbrowser.open("app.courseplay.co")
    print ("The current time is "+time.ctime())
    print ("This is break # %d" % break_number)
