from datetime import datetime
from .jobs import schedule_key_deletion
from apscheduler.schedulers.background import BackgroundScheduler
def schedule_jobs():
    scheduler = BackgroundScheduler()
    # run every time it hits 00:00
    scheduler.add_job(schedule_key_deletion, 'cron', hour=0, minute=0)
    
    
    scheduler.start()#