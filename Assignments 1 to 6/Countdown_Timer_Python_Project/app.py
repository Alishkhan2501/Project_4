import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

    print("0:00\nTime's up!")

if __name__ == "__main__":
    user_input = int(input("Enter time in seconds: "))
    countdown_timer(user_input)

