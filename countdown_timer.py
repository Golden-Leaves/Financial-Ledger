import time
import winsound
def countdown(seconds):
    while seconds > 0:
        hours, remaining_seconds = divmod(seconds,3600)
        mins, secs = divmod(remaining_seconds,60)
        timer = "{:02d}:{:02d}:{:02d}".format(hours,mins, secs)
        print(timer, end = "\r")
     
        time.sleep(1) #basically pausing for 1 second before continuing the countdown
        seconds -= 1
    winsound.Beep(400,1000)
    print("Time's up" )
def user_input():
    while True:
        print("Enter the time in seconds(or press 'Enter' to exit the porgram): ")
        user_input_time = int(input())
        if user_input_time == "":
            print("Exiting program")
        else:
            countdown(user_input_time)


user_input()
