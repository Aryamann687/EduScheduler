import random  # Fixed case sensitivity

def generate_timetable(data):
    # Ensure data is parsed correctly; frontend might send strings instead of ints
    try:
        subject_teachers = data.get("subject_teachers", {})
        subject_weekly_limits = {k: int(v) for k, v in data.get("subject_weekly_limits", {}).items()}
        periods_per_day = int(data.get("periods_per_day", 4))
    except (ValueError, TypeError) as e:
        return {"error": "Invalid data format", "reason": str(e)}

    if not subject_teachers:
        return {"error": "No subjects/teachers provided"}

    subjects = list(subject_teachers.keys())
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    periods = [f"P{i+1}" for i in range(periods_per_day)]

    total_slots = len(days) * periods_per_day
    required_classes = sum(subject_weekly_limits.values())

    if required_classes > total_slots:
        return {
            "error": "Constraints impossible",
            "reason": f"Required ({required_classes}) exceeds available ({total_slots})"
        }

    timetable = {}
    remaining = subject_weekly_limits.copy()
    teacher_week_count = {}
    subject_week_count = {}

    for day in days:
        timetable[day] = {}
        used_today = set()

        for p in periods:
            # Check which subjects still need classes and haven't been taught today
            valid = [
                s for s in subjects
                if remaining.get(s, 0) > 0 and s not in used_today
            ]

            if not valid:
                timetable[day][p] = {"subject": "FREE", "teacher": "-"}
                continue

            # Pick subject with most remaining classes to balance the load
            subject = max(valid, key=lambda s: remaining[s])
            teacher = subject_teachers.get(subject, "Unknown")

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
