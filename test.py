import time, winsound
class Timer:
    def __init__(self,total_seconds):
        self.total_seconds = total_seconds
    
    def countdown(self):
        while self.total_seconds > 0:
          hours, remaining_seconds = divmod(self.total_seconds, 3600)
          minutes, seconds = divmod(remaining_seconds, 60)
          timer_format = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
          print(timer_format, end = "\r")
          time.sleep(1)
          self.total_seconds -= 1
        print("Time out!")

def user_input():
    print("Please enter the amount of seconds")
    seconds = int(input())
    print(f"Total amount of seconds that you entered: {seconds}")
    return seconds
seconds = user_input()
timer = Timer(seconds)
timer.countdown()
