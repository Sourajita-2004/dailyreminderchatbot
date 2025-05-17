from datetime import datetime, timedelta

def generate_routine(profession):
    routines = {
        "software engineer": [
            "09:00 AM - Standup meeting",
            "10:00 AM - Code review",
            "12:00 PM - Lunch",
            "01:00 PM - Development time",
            "03:00 PM - Team collaboration",
            "05:00 PM - End of workday"
        ],
        "student": [
            "08:00 AM - Class",
            "10:00 AM - Study",
            "12:00 PM - Lunch",
            "01:00 PM - Study group",
            "04:00 PM - Gym",
            "06:00 PM - Review notes"
        ]
    }
    return routines.get(profession, [])

def create_schedule(fixed_tasks, flexible_tasks):
    schedule = []
    current_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    # Schedule fixed tasks
    for task in fixed_tasks:
        schedule.append((task['due_time'], task['task_description']))

    # Schedule flexible tasks
    scheduled_times = {t[0] for t in schedule}  # Use a set for faster lookup
    for task in flexible_tasks:
        while current_time in scheduled_times:  # Avoid conflict with fixed tasks
            current_time += timedelta(minutes=30)  # Adjust interval as needed
        schedule.append((current_time, task['task_description']))
        scheduled_times.add(current_time)  # Add to scheduled times
        current_time += timedelta(minutes=30)  # Adjust interval for the next task

    # Sort tasks in the schedule by time
    schedule.sort(key=lambda x: x[0])
    return schedule

def create_reminders(tasks):
    reminders = []
    for task in tasks:
        reminder_time = task['due_time'] - timedelta(minutes=30)  # Set reminder 30 min before
        reminders.append({
            'task_id': task['task_id'],
            'reminder_time': reminder_time
        })
    return reminders

def suggest_task(user_id, user_tasks, current_time, free_time_duration):
    prioritized_tasks = [task for task in user_tasks if not task['is_fixed']]
    # Sort by urgency or another metric
    prioritized_tasks.sort(key=lambda x: x['urgency'], reverse=True)

    available_suggestions = []
    for task in prioritized_tasks:
        if task['estimated_time'] <= free_time_duration:  # check if it fits in the available time
            available_suggestions.append(task)

    return available_suggestions[:3]  # Returning top 3 suggestions