# Student-Result-Management-System-Full-CRUD-
A terminal-based Python + MySQL to manage student records with full CRUD support, automatic result calculation, and CSV export

## ✅ Features

- Add new student with marks (Maths, Science, Social)
- Auto calculate average & pass/fail status
- View result, average, or subject-wise marks
- Update ID, name, or individual subject marks (auto-recalculates result)
- Delete student by ID
- View all student records
- Export full table as CSV
- Display exported CSV in terminal

## 💻 Tech Stack

- Python
- MySQL
- CSV module

## 🚀 How to Run

1. Make sure MySQL server is running.
2. Update DB credentials inside the script:
```python
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)
