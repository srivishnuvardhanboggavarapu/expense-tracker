import sqlite3
import os

DB_PATH = "data/expense_tracker.db"

# Database Connection
def get_connection():

    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    return conn

# Initialize Database
def initialize_db():

    conn = get_connection()

    cursor = conn.cursor()

    with open("schema.sql", "r") as f:
        cursor.executescript(f.read())

    # Default User
    try:
        cursor.execute(
            """
            INSERT INTO users (username)
            VALUES (?)
            """,
            ("Admin",)
        )

    except sqlite3.IntegrityError:
        pass

    # Default Categories
    categories = [
        "Food",
        "Transport",
        "Utilities",
        "Entertainment"
    ]

    for category in categories:

        try:

            cursor.execute(
                """
                INSERT INTO categories (category_name)
                VALUES (?)
                """,
                (category,)
            )

        except sqlite3.IntegrityError:
            pass

    conn.commit()

    conn.close()

# Add Expense
def add_expense(
    user_id,
    category_id,
    amount,
    description,
    expense_date
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO expenses
        (
            user_id,
            category_id,
            amount,
            description,
            expense_date
        )

        VALUES (?, ?, ?, ?, ?)
        """,

        (
            user_id,
            category_id,
            amount,
            description,
            expense_date
        )
    )

    conn.commit()

    conn.close()

    print("\n✅ Expense added successfully!")

# View Expenses
def view_expenses():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            expense_id,
            username,
            category_name,
            amount,
            description,
            expense_date

        FROM expenses

        JOIN users

        ON expenses.user_id =
        users.user_id

        JOIN categories

        ON expenses.category_id =
        categories.category_id

        ORDER BY expense_date DESC
        """
    )

    records = cursor.fetchall()

    conn.close()

    return records

# Search by Category
def search_expense(keyword):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            expense_id,
            username,
            category_name,
            amount,
            description,
            expense_date

        FROM expenses

        JOIN users

        ON expenses.user_id =
        users.user_id

        JOIN categories

        ON expenses.category_id =
        categories.category_id

        WHERE category_name LIKE ?
        OR description LIKE ?
        """,

        (
            f"%{keyword}%",
            f"%{keyword}%"
        )
    )

    results = cursor.fetchall()

    conn.close()

    return results

# Search by Date Range
def search_by_date(start_date, end_date):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            expense_id,
            username,
            category_name,
            amount,
            description,
            expense_date

        FROM expenses

        JOIN users

        ON expenses.user_id =
        users.user_id

        JOIN categories

        ON expenses.category_id =
        categories.category_id

        WHERE expense_date
        BETWEEN ? AND ?

        ORDER BY expense_date DESC
        """,

        (start_date, end_date)
    )

    results = cursor.fetchall()

    conn.close()

    return results

# Update Expense
def update_expense(
    expense_id,
    amount,
    description
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE expenses

        SET
            amount=?,
            description=?

        WHERE expense_id=?
        """,

        (
            amount,
            description,
            expense_id
        )
    )

    conn.commit()

    if cursor.rowcount > 0:

        print("\n✅ Expense updated successfully!")

    else:

        print("\n❌ Expense not found!")

    conn.close()

# Delete Expense
def delete_expense(expense_id):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM expenses
        WHERE expense_id=?
        """,

        (expense_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:

        print("\n✅ Expense deleted successfully!")

    else:

        print("\n❌ Expense not found!")

    conn.close()

# Monthly Summary
def monthly_summary():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT SUM(amount) AS total
        FROM expenses
        """
    )

    row = cursor.fetchone()

    conn.close()

    return row["total"] if row["total"] else 0.0

# Average Expense
def average_expense():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT AVG(amount) AS average
        FROM expenses
        """
    )

    row = cursor.fetchone()

    conn.close()

    return row["average"] if row["average"] else 0.0

# Category Report
def category_report():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            categories.category_name,
            SUM(expenses.amount) AS total

        FROM expenses

        JOIN categories

        ON expenses.category_id =
        categories.category_id

        GROUP BY categories.category_name

        ORDER BY total DESC
        """
    )

    report = cursor.fetchall()

    conn.close()

    return report

# Top Spending Category
def top_category():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            categories.category_name,
            SUM(expenses.amount) AS total

        FROM expenses

        JOIN categories

        ON expenses.category_id =
        categories.category_id

        GROUP BY categories.category_name

        ORDER BY total DESC

        LIMIT 1
        """
    )

    result = cursor.fetchone()

    conn.close()

    return result