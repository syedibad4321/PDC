# tasks.py
import time
from celery import Celery

app = Celery('my_app', broker='amqp://guest@localhost//', backend='rpc://')

@app.task
def send_email_task(email_address):
    print(f"--> Sending email to {email_address}...")
    
    
    time.sleep(5)
    
    return f"Email successfully sent to {email_address}!"