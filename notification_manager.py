import sched
import time
from datetime import datetime, timedelta
from plyer import notification

# Initialize the scheduler
scheduler = sched.scheduler(time.time, time.sleep)

def notify(event_name, event_time):
    """ Send a desktop notification about the event. """
    notification.notify(
        title='Event Reminder',
        message=f'Remember your event: {event_name} at {event_time}',
        app_icon=None,  # Path to an .ico file can be added here
        timeout=10,  # Notification duration in seconds
    )

def schedule_notification(event_name, event_time):
    """ Schedule a notification for the event. """
    event_time_datetime = datetime.strptime(event_time, "%Y-%m-%d %H:%M")
    current_time = datetime.now()
    delay = (event_time_datetime - current_time).total_seconds()
    if delay > 0:
        print(f"Scheduling notification for: {event_name} at {event_time}")
        scheduler.enter(delay, 1, notify, argument=(event_name, event_time_datetime))
    else:
        print("Event time has already passed")

def set_reminders(event_name, event_time, reminders):
    """ Set multiple reminders for an event. """
    for reminder_delta in reminders:
        reminder_time = datetime.strptime(event_time, "%Y-%m-%d %H:%M") - timedelta(minutes=reminder_delta)
        schedule_notification(f"Reminder for {event_name}", reminder_time.strftime("%Y-%m-%d %H:%M"))

# Example usage
event_name = "Team Meeting"
event_time = "2024-04-15 14:00"  # Date format: YYYY-MM-DD HH:MM
reminders = [15, 60, 120]  # Reminders in minutes before the event

set_reminders(event_name, event_time, reminders)

# Start the scheduler to execute planned notifications
scheduler.run()
