# run_script.py
from tasks import send_email_task
import time

if __name__ == '__main__':
    print("1. Main script start hua.")
    
    # Task ko background mein bhejna (.delay use karke)
    email = "user@example.com"
    result = send_email_task.delay(email)
    
    print(f"2. Task ID: {result.id} worker ko de diya gaya hai.")
    print("3. Main script yahan khatam ho gaya (bina 5 second wait kiye).")
    
    # Optional: Agar aapko result ka wait karna hi hai to:
    # print("Result ka wait kar raha hoon...", result.get())