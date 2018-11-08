from flask import Flask
from apscheduler.schedulers.blocking import BlockingScheduler
import time

app = Flask(__name__)
def my_job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

sched = BlockingScheduler()
sched.add_job(my_job, 'interval', seconds=3, id='123')

# for i in sched.get_jobs():
#     i.remove()

sched.start()
#
# if __name__ == '__main__':
#     app.run()