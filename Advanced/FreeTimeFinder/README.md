# 🕒 FreeTimeFinder

**FreeTimeFinder** is a project that helps find common free time slots among multiple people based on their busy schedules.  
It takes `Friend` objects with one or more `TimeRange` objects representing when each person is busy, and then computes shared available time ranges for meetings or events.

---

## Overview

The project simulates an automated way to find **mutually available meeting times** among a group of people.  
Each person can have multiple busy time ranges during a 24-hour day, and the script calculates **all free time slots** when everyone is available.

For simplicity, the project assumes:
- Time is represented in **24-hour format (`HH:MM`)**.
- A full day has **1440 minutes** (from `00:00` to `23:59`).

---

## ⚙️ Features

✅ Convert time strings (`HH:MM`) into minutes and back.  
✅ Represent time ranges using a clean `TimeRange` dataclass.  
✅ Store multiple friends’ busy schedules using a `Friend` dataclass.  
✅ Efficiently remove busy minutes using a custom list class.  
✅ Display readable free time slots in `HH:MM - HH:MM` format.

---

## 📁 Project Structure

```
FreeTimeFinder/
│
├── helpers.py # Utility functions for time conversion and formatting
├── timerange.py # Defines the TimeRange class representing a busy time slot
├── friend.py # Defines the Friend class and manages all busy minutes
├── custom_list.py # Custom list class with safe element removal
├── main.py # Entry point - defines friends, busy slots, and prints free times
└── README.md # Project documentation
```

---


---

## 🔍 How It Works

1. **Convert Time Ranges:**  
   - Each busy range (`HH:MM - HH:MM`) is converted into a range of minutes (e.g., `120` to `360`).

2. **Store Busy Times:**  
   - Each `Friend` adds their `TimeRange` objects, and all busy minute ranges are stored in a class-level list (`Friend.all_busy_minutes_range`).

3. **Calculate Free Minutes:**  
   - The program begins with all minutes in a day (`0–1439`), then removes minutes that fall into any friend’s busy ranges.

4. **Format Free Ranges:**  
   - The helper function `prettify_available_minutes()` converts contiguous minute ranges back into readable time intervals.

5. **Output Free Slots:**  
   - The final output lists all the time ranges when everyone is available.

---

## ▶️ Running the Project

Simply run the main file:
```
python main.py
```

You can edit main.py to add or modify friends and their busy time ranges.

### Example snippet in main.py:
```
f1 = Friend("Tejas")
f1.add_busy_range(TimeRange("02:00", "06:00"))
f1.add_busy_range(TimeRange("08:00", "10:00"))

f2 = Friend("Chris")
f2.add_busy_range(TimeRange("08:00", "14:00"))
f2.add_busy_range(TimeRange("18:00", "23:30"))

f3 = Friend("Tarun")
f3.add_busy_range(TimeRange("17:00", "23:00"))
```

### Example Output
```
You can meet in 00:00 - 01:59
You can meet in 06:00 - 07:59
You can meet in 14:00 - 16:59
You can meet in 23:30 - 23:59
```

(Output may vary depending on your input data.)
