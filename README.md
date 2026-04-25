# 📅 EduScheduler – Intelligent Timetable Generator

EduScheduler is a **constraint-based timetable generation system** that automatically creates valid schedules for educational institutions. It uses **backtracking + heuristics** to satisfy real-world constraints like teacher availability, subject limits, and fixed slots.

---

## 🚀 Features

* 🧠 **Smart Scheduling Engine**

  * Constraint Satisfaction Problem (CSP) based
  * Backtracking algorithm with pruning
  * MRV (Minimum Remaining Values) heuristic

* 👨‍🏫 **Teacher Constraints**

  * Daily workload limits enforced
  * Avoids teacher conflicts

* 📚 **Subject Management**

  * Weekly subject limits
  * Dynamic subject distribution

* 📌 **Fixed Slot Support**

  * Pre-assign specific subjects to slots

* ⚡ **Efficient & Safe**

  * Time-limited execution (prevents infinite loops)
  * Early pruning of impossible states

* 🌐 **Web Interface**

  * Built with Flask
  * Simple UI for input and visualization

* 📤 **Export Ready**

  * Timetable output structured for export (PDF/Excel ready)

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Algorithm:** Backtracking + Heuristics (CSP)
* **Frontend:** HTML/CSS
* **Libraries:** Flask, JSON

---

## 🧠 How It Works

1. Input data (subjects, teachers, constraints)
2. Apply fixed slots
3. Use backtracking to fill timetable:

   * Select valid subjects
   * Check constraints
   * Place subject
   * Backtrack if conflict occurs
4. Return valid timetable or error

---

## 📂 Project Structure

```
EduScheduler/
│
├── app.py              # Flask app
├── scheduler.py        # Core scheduling algorithm
├── data.py             # (Optional) Data definitions
├── templates/
│   └── index.html      # Frontend UI
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/Aryamann687/eduscheduler.git
cd eduscheduler
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app.py
```

4. Open in browser:

```
http://127.0.0.1:5000
```

---

## 🧪 Sample Input Format

### Subjects & Teachers

```
Math:Mr. Rao
Physics:Dr. Stone
English:Mr. John
```

### Weekly Limits

```
Math:3
Physics:3
English:2
```

---

## ⚠️ Limitations

* Does not yet support:

  * Multi-class scheduling
  * Room allocation
  * Advanced optimization (genetic algorithms)

---

## 🔮 Future Improvements

* 🏫 Multi-class timetable generation
* 🧪 Lab handling (multi-slot allocation)
* 🏢 Room allocation system
* ⚡ Performance optimization (hybrid greedy + backtracking)

---

## 💡 Key Learning

This project demonstrates:

* Constraint Satisfaction Problems (CSP)
* Backtracking algorithms
* Heuristic optimization
* Real-world system design

---

## 👨‍💻 Author

**Aryamann Srivastava**
Computer Science Engineering Student (DSCE)

---

## ⭐ If you like this project

Give it a star ⭐ and share it!
