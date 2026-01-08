import random

def generate_timetable(data):
    # --- Input Parsing ---
    subject_teachers = data.get("subject_teachers", {})
    subject_weekly_limits = {k: int(v) for k, v in data.get("subject_weekly_limits", {}).items()}
    periods_per_day = int(data.get("periods_per_day", 4))
    lab_subjects = data.get("lab_subjects", [])  # List of strings
    fixed_slots = data.get("fixed_slots", [])    # List of dicts: {"day": "Monday", "period": "P1", "subject": "Math"}
    teacher_daily_limit = int(data.get("teacher_daily_limit", 8))

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    periods = [f"P{i+1}" for i in range(periods_per_day)]
    total_slots = len(days) * periods_per_day
    
    # Validation: Labs count as 2 classes
    required_classes = sum(subject_weekly_limits.values())
    if required_classes > total_slots:
        return {"error": "Impossible Constraints", "reason": "Total classes exceed slots."}

    # Initialize empty timetable and trackers
    timetable = {d: {p: None for p in periods} for d in days}
    remaining = subject_weekly_limits.copy()
    teacher_load_today = {d: {} for d in days} # {Day: {Teacher: Count}}

    # --- Step A: Apply Fixed Slots ---
    for slot in fixed_slots:
        d, p, s = slot['day'], slot['period'], slot['subject']
        if d not in timetable or p not in timetable[d]:
            continue
        
        teacher = subject_teachers.get(s)
        if not teacher or remaining.get(s, 0) <= 0:
            return {"error": "Fixed Slot Error", "reason": f"Invalid subject or limit exceeded for {s}"}
        
        # Check Teacher Daily Limit for Fixed Slot
        current_load = teacher_load_today[d].get(teacher, 0)
        if current_load >= teacher_daily_limit:
            return {"error": "Fixed Slot Error", "reason": f"{teacher} exceeds daily limit on {d} via fixed slots."}

        timetable[d][p] = {"subject": s, "teacher": teacher}
        remaining[s] -= 1
        teacher_load_today[d][teacher] = current_load + 1

    # --- Step B: Logic Loop ---
    for d in days:
        used_today = set()
        # Refresh used_today with fixed slots already placed
        for p in periods:
            if timetable[d][p]:
                used_today.add(timetable[d][p]['subject'])

        for idx, p in enumerate(periods):
            if timetable[d][p]: continue # Skip if fixed slot exists

            # Rule: Labs cannot be first or last periods ideally, and need P+1 available
            can_do_lab = (idx < periods_per_day - 1) and (timetable[d][periods[idx+1]] is None)
            
            # Filter valid subjects
            valid = [s for s in subject_teachers.keys() 
                     if remaining.get(s, 0) > 0 and s not in used_today]
            
            # Check Teacher Load
            valid = [s for s in valid if teacher_load_today[d].get(subject_teachers[s], 0) < teacher_daily_limit]

            if not valid:
                timetable[d][p] = {"subject": "FREE", "teacher": "-"}
                continue

            # Prioritize Labs if space allows
            potential_labs = [s for s in valid if s in lab_subjects and remaining[s] >= 2 and can_do_lab]
            
            if potential_labs:
                sub = random.choice(potential_labs)
                teacher = subject_teachers[sub]
                # Place in current and next period
                timetable[d][p] = {"subject": sub + " (Lab)", "teacher": teacher}
                timetable[d][periods[idx+1]] = {"subject": sub + " (Lab)", "teacher": teacher}
                remaining[sub] -= 2
                used_today.add(sub)
                teacher_load_today[d][teacher] = teacher_load_today[d].get(teacher, 0) + 2
            else:
                # Place normal subject
                # Filter out labs that can't fit here
                normal_valid = [s for s in valid if s not in lab_subjects or (s in lab_subjects and remaining[s] == 1)]
                if not normal_valid:
                    timetable[d][p] = {"subject": "FREE", "teacher": "-"}
                    continue
                
                sub = max(normal_valid, key=lambda s: remaining[s])
                teacher = subject_teachers[sub]
                timetable[d][p] = {"subject": sub, "teacher": teacher}
                remaining[sub] -= 1
                used_today.add(sub)
                teacher_load_today[d][teacher] = teacher_load_today[d].get(teacher, 0) + 1

    # Format output for frontend
    return {"timetable": timetable, "summary": {"subject_per_week": subject_weekly_limits}}


