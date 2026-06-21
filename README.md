# pythondemo 
This is my first repo
This is my first repo. It is a python based project.
# Expense Tracker 💰

A simple command-line Expense Tracker built using Python.  
This project allows users to add expenses, save them into a CSV file, and summarize stored expenses.

---

## Features 🚀

- Add new expenses
- Select expense categories
- Save expenses to a CSV file
- Read and summarize saved expenses
- Handles UTF-8 characters and emojis
- Skips empty or invalid rows safely

---

## Technologies Used 🛠️

- Python 3
- CSV Module
- File Handling

---

## Project Structure 📂

```bash
pythondemo/
│
├── expense_tracker.py
├── expenses.csv
├── README.md
```

---

## How It Works ⚙️

1. User enters:
   - Expense name
   - Expense amount
   - Expense category

2. The program:
   - Creates an Expense object
   - Saves data into `expenses.csv`
   - Reads the file
   - Displays all stored expenses

---

## Example Output 🖥️

```bash
🎯 Running Expense Tracker

Enter expense name: Coffee
Enter expense amount: 5

Select a category:
1. 🍔 Food
2. 🏡 Home
3. 💼 Work
4. 🎉 Fun
5. 🤷 Misc

Enter a category number [1 - 5]: 5

< Expense: Coffee, 🤷 Misc, $5.00 >

🎯 Saving user Expense
🎯 Summarizing user Expense
Coffee 5.0 🤷 Misc
```

---

## CSV Format 📄

Expenses are stored in this format:

```csv
Coffee,5.0,🤷 Misc
Gas,70.0,💼 Work
```

---

## Learning Outcomes 📚

This project helped me learn:

- Python classes and objects
- Functions
- Loops and conditionals
- File handling
- CSV file operations
- Error handling
- UTF-8 encoding

---

## Future Improvements 🔥

- Monthly expense summary
- Expense filtering by category
- Data visualization using graphs
- GUI version using Tkinter
- Database integration

---

## Author 👨‍💻

Created by [Tanmay M Katakol]
