# Personal Expense Tracker

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

Add screenshots inside the `screenshots/` folder.

Example:

* Main Menu
* Add Expense
* View Expenses
* Monthly Summary
* Category Report

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

GitHub: Add your GitHub profile link here.
