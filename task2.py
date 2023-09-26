import json

# Initialize the budget.
budget_list = {
    "income": 0,
    "expenses": []
}

# Function to add income
def add_income(amount):
    budget_list["income"] += amount

# Function to add an expense
def add_expense(category, amount):
    budget_list["expenses"].append({"category": category, "amount": amount})

# Function to calculate remaining budget
def calculate_remaining_budget():
    total_expenses = sum(item["amount"] for item in budget_list["expenses"])
    remaining_budget = budget_list["income"] - total_expenses
    return remaining_budget

# Function to categorize expenses and display spending trends
def analyze_expenses():
    expense_categories = {}
    for expense in budget_list["expenses"]:
        category = expense["category"]
        amount = expense["amount"]
        if category in expense_categories:
            expense_categories[category] += amount
        else:
            expense_categories[category] = amount
    return expense_categories

# Function to save budget data to a file
def save_budget_data(filename):
    try:
        with open(filename, "w") as file:
            json.dump(budget_list, file)
        print("Budget data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")

# Function to load budget data from a file
def load_budget_data(filename):
    try:
        with open(filename, "r") as file:
            loaded_budget = json.load(file)
            return loaded_budget
    except FileNotFoundError:
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Function to reset the budget
def reset_budget():
    budget_list["income"] = 0
    budget_list["expenses"] = []

# Function to display the current budget details
def display_budget_details():
    print("\nCurrent Budget Details:")
    print(f"Income: {budget['income']}")
    remaining_budget = calculate_remaining_budget()
    print(f"Remaining Budget: {remaining_budget}")

# Main program loop
while True:
    print("\nBudget Tracker Menu:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Calculate Remaining Budget")
    print("4. Analyze Expenses")
    print("5. Save Budget Data")
    print("6. Load Budget Data")
    print("7. Reset Budget")
    print("8. View Current Budget Details")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            amount = float(input("Enter the income amount: "))
            add_income(amount)
        except ValueError:
            print("Invalid input. Please enter a numeric value for income.")
    elif choice == "2":
        category = input("Enter the expense category: ")
        try:
            amount = float(input("Enter the expense amount: "))
            add_expense(category, amount)
        except ValueError:
            print("Invalid input. Please enter a numeric value for expenses.")
    elif choice == "3":
        remaining_budget = calculate_remaining_budget()
        print(f"Remaining Budget: {remaining_budget}")
    elif choice == "4":
        expense_categories = analyze_expenses()
        for category, amount in expense_categories.items():
            print(f"{category}: {amount}")
    elif choice == "5":
        filename = input("Enter the filename to save budget data: ")
        save_budget_data(filename)
    elif choice == "6":
        filename = input("Enter the filename to load budget data: ")
        loaded_budget = load_budget_data(filename)
        if loaded_budget:
            budget = loaded_budget
            print("Budget data loaded successfully.")
    elif choice == "7":
        reset_budget()
        print("Budget reset successfully.")
    elif choice == "8":
        display_budget_details()
    elif choice == "9":
        break
    else:
        print("Invalid choice. Please try again.")
