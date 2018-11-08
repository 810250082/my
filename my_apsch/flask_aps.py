from flask_apscheduler import APScheduler
from flask import Flask

class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'my_jobs:job1',
            # 'args': (1, 2),
            'trigger': 'interval',
            'seconds': 5
        }
    ]

    SCHEDULER_API_ENABLED = True

app = Flask(__name__)
sche = APScheduler()
@app.route('/')
def hello():
    return "hello world"

@app.route('/add')
def add_myjob():
    app.apscheduler.add_job(func='my_jobs:job2', id='job2', trigger='interval', seconds=2)
    return 'add success'

@app.route('/add-cron')
def add_cron_job():
    app.apscheduler.add_job(func='my_jobs:job3', id='job3', trigger='cron', minute='*/3')
    return 'add success'

if __name__ == '__main__':
    print('Let us run out of the loop')
    app.config.from_object(Config())
    sche.init_app(app)
    sche.start()

    app.run(host='0.0.0.0', debug=True)