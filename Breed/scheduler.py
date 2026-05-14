from apscheduler.schedulers.background import BackgroundScheduler
from .services import uptadeDogBreed

def start():
    scheduler = BackgroundScheduler()

    scheduler.add_job(
        uptadeDogBreed,
        'interval',
        hours=24
    )

    scheduler.start()