from rq import Queue
from time import sleep
from redis import Redis
from worker import test

redis_conn=Redis(host='localhost',port=6379)
q = Queue(connection=redis_conn)
job = q.enqueue(test, 'Hello')
print('Job id: %s' % job.id)
sleep(6)
print(job.result)