from database import *

def print_record(r):

    print("-" * 45)

    print(f"Expense ID : {r['expense_id']}")
    print(f"User       : {r['username']}")
    print(f"Category   : {r['category_name']}")
    print(f"Amount     : ₹{r['amount']:.2f}")
    print(f"Description: {r['description']}")
    print(f"Date       : {r['expense_date']}")

    print("-" * 45)

def menu():

    print("\n========= PERSONAL EXPENSE TRACKER =========")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Search by Date Range")
    print("5. Update Expense")
    print("6. Delete Expense")
    print("7. Monthly Summary")
    print("8. Average Expense")
    print("9. Category Report")
    print("10. Top Spending Category")
    print("11. Exit")

def main():

    initialize_db()

    while True:

        menu()

        choice = input(
            "\nEnter your choice: "
        ).strip()

        # Add Expense
        if choice == "1":

            print("\nCategories:")
            print("1. Food")
            print("2. Transport")
            print("3. Utilities")
            print("4. Entertainment")

            try:

                user_id = 1

                category_id = int(
                    input("Enter Category ID: ")
                )

                if category_id not in [1, 2, 3, 4]:

                    print("\n❌ Invalid Category ID!")

                    continue

                amount = float(
                    input("Enter Amount: ")
                )

                description = input(
                    "Enter Description: "
                ).strip()

                expense_date = input(
                    "Enter Date (YYYY-MM-DD): "
                ).strip()

                add_expense(
                    user_id,
                    category_id,
                    amount,
                    description,
                    expense_date
                )

            except ValueError:

                print("\n❌ Invalid Input!")

        # View Expenses
        elif choice == "2":

            records = view_expenses()

            if records:

                for r in records:
                    print_record(r)

            else:

                print("\nNo expenses found!")

        # Search Expense
        elif choice == "3":

            keyword = input(
                "Enter keyword/category: "
            ).strip()

            results = search_expense(keyword)

            if results:

                for r in results:
                    print_record(r)

            else:

                print("\nNo matching records!")

        # Search by Date
        elif choice == "4":

            start_date = input(
                "Enter Start Date (YYYY-MM-DD): "
            ).strip()

            end_date = input(
                "Enter End Date (YYYY-MM-DD): "
            ).strip()

            results = search_by_date(
                start_date,
                end_date
            )

            if results:

                for r in results:
                    print_record(r)

            else:

                print("\nNo records found!")

        # Update Expense
        elif choice == "5":

            try:

                expense_id = int(
                    input("Enter Expense ID: ")
                )

                amount = float(
                    input("Enter New Amount: ")
                )

                description = input(
                    "Enter New Description: "
                ).strip()

                update_expense(
                    expense_id,
                    amount,
                    description
                )

            except ValueError:

                print("\n❌ Invalid Input!")

        # Delete Expense
        elif choice == "6":

            try:

                expense_id = int(
                    input("Enter Expense ID: ")
                )

                delete_expense(expense_id)

            except ValueError:

                print("\n❌ Invalid ID!")

        # Monthly Summary
        elif choice == "7":

            total = monthly_summary()

            print(
                f"\nTotal Monthly Expense: ₹{total:.2f}"
            )

        # Average Expense
        elif choice == "8":

            avg = average_expense()

            print(
                f"\nAverage Expense: ₹{avg:.2f}"
            )

        # Category Report
        elif choice == "9":

            report = category_report()

            if report:

                print("\nCategory Report")

                for r in report:

                    print(
                        f"{r['category_name']} : ₹{r['total']:.2f}"
                    )

            else:

                print("\nNo records found!")

        # Top Category
        elif choice == "10":

            result = top_category()

            if result:

                print(
                    f"\nTop Spending Category: "
                    f"{result['category_name']}"
                )

                print(
                    f"Total: ₹{result['total']:.2f}"
                )

            else:

                print("\nNo data available!")

        # Exit
        elif choice == "11":

            print("\nGoodbye 👋")

            break

        else:

            print("\n❌ Invalid Choice!")

if __name__ == "__main__":
    main()