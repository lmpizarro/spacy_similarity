import multiprocessing
backlog = 2048

bind = "127.0.0.1:8000"
workers = 1 # multiprocessing.cpu_count() * 2 + 1
timeout=240
threads=2
worker_class="gthread"

errorlog = '-'
loglevel = 'info'
accesslog = '-'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
