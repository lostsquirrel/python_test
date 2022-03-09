import time
import schedule

def job():
    print("I'm working...")

schedule.every(3).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)