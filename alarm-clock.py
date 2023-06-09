# install playsound 1.2.2 
from playsound import playsound
import time


# clear terminal command and start from the bottom of terminal the chrono and print evrey second on next line
CLEAR = "\033[2J"
# will be return on a same line and don't change the position when chrono run 
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        
        
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60  # 125 sec // 60 = 2
        seconds_left = time_left % 60 # 125 % 60 = 5
        
        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")
        
        
    playsound("iphone_alarm.mp3")
    
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds



alarm(total_seconds)


