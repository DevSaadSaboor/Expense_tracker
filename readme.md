# Expense Tracker (Python CLI)

A simple **Command Line Expense Tracker** built with Python.  
This project helps track daily expenses by category, date, and amount while following **clean architecture principles**.

---

## 📌 Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Data persistence using file storage (CSV / JSON)
- Input validation and error handling
- Clean separation of concerns

---

## 🏗 Project Structure

expense_tracker/
│
├── main.py # User input & output only
│
├── services/
│ └── expense_service.py # Business logic
│
├── storage/
│ └── expense_storage.py # Load / Save data
│
├── utils/
│ └── validators.py # Input validation
│
├── data/
│ └── expenses.csv # Stored expenses (auto-created)
│
├── .giti
└── README.md


---

## 🧠 Architecture Rules (Important)

- `main.py`  
  → Handles **input / print only**

- `service`  
  → Business logic only  
  → Returns `(bool, message, data)`

- `storage`  
  → File read/write only  
  → No logic

- `utils`  
  → Validation and helpers

- **No direct file access in `main.py`**

---

## 📝 Expense Data Format

Each expense is stored as a dictionary:

```python
{
    "id": 1,
    "amount": 250,
    "category": "Food",
    "date": "2025-01-01",
    "note": "Lunch"
}

🚀 How to Run
python main.py
Make sure Python 3.8+ is installed.

📚 Concepts Practiced

Python fundamentals
Functions and modular code
File handling (CSV / JSON)
Input validation
Clean architecture
CLI-based application design

🎯 Learning Goal

This project is part of my backend learning roadmap to build strong Python + SQL + Django skills for real-world applications.

📌 Future Improvements

Edit / from
Monthly summary
Category analytics
Database (SQLite) integration
Web version (Django)

🧑‍💻 Author
Saad Saboor