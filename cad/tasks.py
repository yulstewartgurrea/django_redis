import time
from redis import Redis
from rq import Queue
from rq.registry import StartedJobRegistry

import django
django.setup()

from count_words import count_words_at_url

# Tell RQ what Redis connection to use
REDIS_PORT = 6379
REDIS_HOST = '127.0.0.1'

redis_conn = Redis(host=REDIS_HOST, port=REDIS_PORT)
queue = Queue(connection=redis_conn)  # no args implies the default queue

# Delay execution of count_words_at_url('http://nvie.com')
# job = q.enqueue(count_words_at_url, 'http://heroku.com')
# print(job)
# print(job.result)   # => None

# Now, wait a while, until the worker is finished
# time.sleep(2)
# print(job.result)   # => 889

# get StartedJobRegistry by queue
# registry = StartedJobRegistry(queue=queue)

# or get StartedJobRegistry by queue name and connection
# registry2 = StartedJobRegistry(name='my_queue', connection=redis_conn)

# sleep for a moment while job is taken off the queue
# time.sleep(0.1)

# print('Queue associated with the registry: %s' % registry.get_queue())
# print('Number of jobs in registry %s' % registry.count)

# get the list of ids for the jobs in the registry
# print('IDs in registry %s' % registry.get_job_ids())

# test if a job is in the registry using the job instance or job id
# print('Job in registry %s' % (job in registry))
# print('Job in registry %s' % (job.id in registry))