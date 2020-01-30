from redistimeseries.client import Client
from redis.exceptions import ResponseError
from random import randint
import argparse
from time import time,sleep
parser = argparse.ArgumentParser()
parser.add_argument("key", help="Time Series Key",type=str)
parser.add_argument("retention", help="Time series retention periods in ms",type=int)
args = parser.parse_args()
rts = Client(host='localhost',port=6379)
try:
    rts.create(args.key,retention_msecs=args.retention)
except ResponseError as e:
    s = str(e)
    print(s)
    pass
if __name__=="__main__":
    while(True):
        v=randint(0,10)
        t=rts.add(args.key, value=v,timestamp=int(time()))
        print('INSERT: ({},{}) AT {}, SUCCESS'.format(args.key,v,t))
        sleep(60)

