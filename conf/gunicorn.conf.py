from multiprocessing import cpu_count

#TO RUN GUNICORN
workers = cpu_count() * 2 + 1
bind = "0.0.0.0:8010"
worker_class = "gthread"
threads = workers + 1
# max_requests = 1000
daemon = False

#TO ENABLE LOGGING
loglevel = "debug"
capture_output = True
# log-file=-