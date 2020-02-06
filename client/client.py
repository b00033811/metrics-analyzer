''' The role of the client is to sched. jobs for a redis worker and
 log the state of the state of the last consumed messege from the API'''

import redis
import sys
from random import randint
from time import sleep
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
stream=sys.stdout)
rc=redis.Redis('localhost',port=6379)
key='mystream'
while (True):
    v=dict(dummy=randint(0,10))
    result=rc.xadd(key,v)
    logging.debug('{0}'.format(result))
    print(result)
    sleep(1)
    




