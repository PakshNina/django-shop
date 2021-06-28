# bind = '0.0.0.0:80'
# preload = True
# workers = 3


bind = '0.0.0.0:80'
max_requests = 100
max_requests_jitter = 5
preload = True
workers = 8
threads = 2
worker_class = 'gthread'
worker_tmp_dir = '/tmp'
errorlog = '-'
accesslog = '-'
