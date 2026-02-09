# Daily Mood Tracker (Python Project)

A simple yet powerful **Mini Data Science application** that helps you track your daily mood, analyze patterns, and visualize your emotional trends using Python.

This project was built to practice **CSV handling, data analysis, visualization, and basic software structure**.


🚀 Features

1️⃣ Add Daily Mood

Save your mood with today's date directly into a CSV file.

Supported moods:

* Happy 😄
* Sad 😔
* Productive 🚀
* Lazy 😴
* Stressed 😵

2️⃣ Mood History Viewer

View all previously logged moods in a clean timeline format.

Example:

```
2026-02-10 - Happy
2026-02-11 - Lazy
```

3️⃣ Mood Analysis

Counts how many times each mood appears in your data.
Example:
```
Happy : 3
Sad : 2
Lazy : 1
```

4️⃣ Mood Graph Visualization 📊

Automatically generates a bar chart showing mood distribution using **Matplotlib**.

---

5️⃣ Smart Mood Report 📝

Generates insights such as:

* Total tracked days
* Most common moods
* Least common moods (supports multiple ties)

Example:
```
Total days tracked: 12
Most common moods: Happy, Productive
Least common moods: Lazy, Stressed
```

🛠️ Tech Stack

* Python 🐍
* CSV Module
* Matplotlib 📊
* File Handling
* Dictionary-based Data Analysis

---

📂 Project Structure

```
Mood_Tracker/
│
├── mood_tracker.py
└── mood_data.csv (auto-generated)
```

---

▶️ How to Run

1. Clone the repository
```
git clone <your-repo-link>
```
2. Install matplotlib (if not installed)
```
pip install matplotlib
```
3. Run the project
```
python mood_tracker.py
```
🎯 Learning Outcomes
This project demonstrates:

* Real-world data collection
* Data analysis fundamentals
* Data visualization
* Building a menu-driven Python application

Perfect beginner **Data Science starter project**.

🔮 Future Updates (Coming Soon)

Planned upgrades for the next version:

* 🖥️ GUI Version using Tkinter
* 📅 Weekly Mood Graph only
* ⏰ Automatic reminder to log daily mood
* 📈 Export data to Excel
* 🤖 AI Mood Prediction (Machine Learning)
