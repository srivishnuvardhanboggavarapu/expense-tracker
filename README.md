<img width="960" height="540" alt="Monthly Summary" src="https://github.com/user-attachments/assets/47e25b7b-8229-4458-89f0-5f8a1c171db6" /># Personal Expense Tracker

## Project Overview

The Personal Expense Tracker is a Python and SQLite-based mini project designed to help users manage and monitor their daily expenses efficiently.
Users can record expenses, categorize spending, search expense history, update records, and generate useful financial reports.

This project demonstrates CRUD operations, SQL queries, reporting, and menu-driven programming concepts.

---

## Features

* Add Expenses
* View Expenses
* Search Expenses
* Search by Date Range
* Update Expenses
* Delete Expenses
* Monthly Summary
* Average Expense Calculation
* Category-wise Expense Report
* Top Spending Category
* Error Handling for Invalid Inputs

---

## Technologies Used

* Python 3
* SQLite
* SQL
* VS Code
* Git
* GitHub

---

## Project Structure

```text id="vzhd9t"
expense-tracker/
│
├── main.py
├── database.py
├── schema.sql
├── README.md
├── requirements.txt
├── .gitignore
├── screenshots/
└── data/
```

---

## Database Tables

### 1. users

Stores user information.

| Column Name | Type    |
| ----------- | ------- |
| user_id     | INTEGER |
| username    | TEXT    |

---

### 2. categories

Stores expense categories.

| Column Name   | Type    |
| ------------- | ------- |
| category_id   | INTEGER |
| category_name | TEXT    |

---

### 3. expenses

Stores all expense records.

| Column Name  | Type    |
| ------------ | ------- |
| expense_id   | INTEGER |
| user_id      | INTEGER |
| category_id  | INTEGER |
| amount       | REAL    |
| description  | TEXT    |
| expense_date | TEXT    |

---

## SQL Concepts Used

* INSERT
* UPDATE
* DELETE
* SELECT
* SUM()
* AVG()
* GROUP BY
* ORDER BY
* INNER JOIN
* Date Filtering

---

## Features Explanation

### Add Expense

Users can add daily expenses with:

* Category
* Amount
* Description
* Date

### View Expenses

Displays all recorded expenses from the database.

### Search Expense

Allows searching expenses using:

* Category name
* Description keyword

### Search by Date Range

Displays expenses between selected dates.

### Update Expense

Updates existing expense records.

### Delete Expense

Deletes unwanted expense records.

### Monthly Summary

Calculates total monthly expenses using SQL SUM() function.

### Average Expense

Calculates average expense amount using SQL AVG() function.

### Category Report

Displays total spending for each category using GROUP BY.

### Top Spending Category

Displays the category with highest spending.

---

## How to Run

### Step 1 — Open Terminal

Navigate to project folder:

```bash id="i11d0u"
cd expense-tracker
```

### Step 2 — Run Project

```bash id="m3q2wz"
python main.py
```

---

## Example Menu

```text id="a4p9xo"
========= PERSONAL EXPENSE TRACKER =========

1. Add Expense
2. View Expenses
3. Search Expense
4. Search by Date Range
5. Update Expense
6. Delete Expense
7. Monthly Summary
8. Average Expense
9. Category Report
10. Top Spending Category
11. Exit
```

---

## Screenshots
* Main Menu
<img width="960" height="540" alt="Main Menu" src="https://github.com/user-attachments/assets/8606c9d8-c075-4c2a-9ff4-80d3594c031c" />
* Add Expense
<img width="960" height="540" alt="Add Expense_1" src="https://github.com/user-attachments/assets/245ad986-f42b-4d4e-b501-a4b591d55e89" />
* View Expenses
<img width="960" height="540" alt="View Expenses" src="https://github.com/user-attachments/assets/ffc03b51-6c7e-429f-921b-f4b73d4a518a" />
* Monthly Summary
<img width="960" height="540" alt="Monthly Summary" src="https://github.com/user-attachments/assets/ae1af7fc-4dfd-45b8-a911-902f1715e4d2" />
* Category Report
<img width="960" height="540" alt="Category Report" src="https://github.com/user-attachments/assets/d78b89ee-b956-496e-a199-0cfd61633e83" />
* date Search
<img width="960" height="540" alt="Date Search" src="https://github.com/user-attachments/assets/ee47ee11-16d6-441c-8423-33407b8b579e" />
* Average Expense
<img width="960" height="540" alt="Average Expense" src="https://github.com/user-attachments/assets/a047de23-d1d6-482a-980c-92edb61a100a" />
* Delete Expense
<img width="960" height="540" alt="Delete Expense" src="https://github.com/user-attachments/assets/cb1fc8a9-171b-4659-a748-05a27015c9a5" />
* Top Category
<img width="960" height="540" alt="Top Category" src="https://github.com/user-attachments/assets/53734cfd-bf61-44e5-b6a7-45a3f8a842e7" />
* Exit
<img width="960" height="540" alt="Exit" src="https://github.com/user-attachments/assets/e978f2de-eafe-4f6b-9084-9b89217ef2c5" />

---

## Future Improvements

* Budget Tracking
* Export Reports to CSV
* Expense Charts using Matplotlib
* Multiple User Support
* Password Authentication

---

## Author

Vishnu Boggavarapu

GitHub: https://github.com/srivishnuvardhanboggavarapu
