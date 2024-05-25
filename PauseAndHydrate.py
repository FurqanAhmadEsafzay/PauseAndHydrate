import time
from plyer import notification

def send_notification():
    notification.notify(
        title="Hydration Reminder",
        message="Time to drink water!",
        timeout=10  # Notification stays for 10 seconds
    )


while True:
    send_notification()
    time.sleep(7200)  # Wait for 2hrs (7200) seconds before sending the next notification