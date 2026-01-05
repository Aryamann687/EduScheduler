import random

def generate_timetable(subjects, periods_per_day, days, subject_limits):
    periods = [f"P{i+1}" for i in range(periods_per_day)]

    remaining = subject_limits.copy()
    timetable = {}

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
            else:
                subject = random.choice(valid)
                timetable[day][p] = subject
                remaining[subject] -= 1
                used_today.add(subject)

    return timetable