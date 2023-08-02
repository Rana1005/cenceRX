from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from .jobs import schedule_task

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(schedule_task, 'interval', seconds = 10)
    scheduler.start()
