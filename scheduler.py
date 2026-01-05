import random

def generate_timetable(data):
    subject_teachers = data.get("subject_teachers", {})
    subject_weekly_limits = data.get("subject_weekly_limits", {})
    periods_per_day = data.get("periods_per_day", 4)

    if not subject_teachers:
        return {"error": "No subjects/teachers provided"}

    if not subject_weekly_limits:
        return {
            "error": "Subjects weekly limits missing",
            "reason": "Please enter weekly class count for each subject"
        }

    subjects = list(subject_teachers.keys())
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    periods = [f"P{i+1}" for i in range(periods_per_day)]

    total_slots = len(days) * periods_per_day
    required_classes = sum(subject_weekly_limits.values())

    if required_classes > total_slots:
        return {
            "error": "Constraints impossible",
            "reason": "Total required classes exceed available slots"
        }

    timetable = {}
    remaining = subject_weekly_limits.copy()

    teacher_week_count = {}
    subject_week_count = {}

    for day in days:
        timetable[day] = {}
        used_today = set()

        for p in periods:
            valid = [
                s for s in subjects
                if remaining.get(s, 0) > 0 and s not in used_today
            ]

            if not valid:
                timetable[day][p] = "FREE"
                continue

            subject = random.choice(valid)
            teacher = subject_teachers[subject]

            timetable[day][p] = {
                "subject": subject,
                "teacher": teacher
            }

            remaining[subject] -= 1
            used_today.add(subject)

            teacher_week_count[teacher] = teacher_week_count.get(teacher, 0) + 1
            subject_week_count[subject] = subject_week_count.get(subject, 0) + 1

    return {
        "timetable": timetable,
        "summary": {
            "teacher_per_week": teacher_week_count,
            "subject_per_week": subject_week_count
        }
    }
