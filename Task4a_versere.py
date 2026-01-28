import pandas as pd
import matplotlib.pyplot as plt

# main menu options

def main_menu():
    while True:
        print("\n#############################################")
        print("############ Versere Cars Sales ############")
        print("#############################################")
        print("1. Total Sales Analysis")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice in ["1", "2"]:
            return choice
        else:
            print("Invalid choice, please try again.")

#sub-menu options 

def total_menu():
    while True:
        print("\n############ Total Sales Menu ############")
        print("1. All sales by model")
        print("2. Used vs New sales")
        print("3. Sales by salesperson")
        print("4. Back to main menu")

        choice = input("Enter your choice: ")

        if choice in ["1", "2", "3", "4"]:
            return choice
        else:
            print("Invalid choice, please try again.")


def load_data():
    df = pd.read_csv("Task4a_data.csv")
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
    return df

# processes all sales by model

def all_sales_by_model(df):
    grouped = df.groupby("Car Model")["Value"].sum()

    print("\nTotal Sales by Model:")
    for model, value in grouped.items():
        print(f"{model}: £{value:,}")

    grouped.plot(kind="bar", title="Total Sales by Car Model")
    plt.xlabel("Car Model")
    plt.ylabel("Sales Value (£)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

# processes used vs new sales

def used_vs_new_sales(df):
    sales = df.groupby("New/Used")["Value"].sum()

    used = sales.get("Used", 0)
    new = sales.get("New", 0)

    print("\nUsed vs New Sales:")
    print(f"Used Sales Total: £{used:,}")
    print(f"New Sales Total: £{new:,}")

    plt.figure(figsize=(6, 6))
    plt.pie(
        [used, new],
        labels=["Used", "New"],
        autopct="%1.1f%%",
        startangle=140,
        colors=["#ff9999", "#99ff99"]
    )
    plt.title("Used vs New Car Sales")
    plt.show()

# processes sales by salesperson

def sales_by_salesperson(df):
    grouped = df.groupby("Salesperson")["Value"].sum()

    print("\nSales by Salesperson:")
    for person, value in grouped.items():
        print(f"{person}: £{value:,}")

    grouped.plot(kind="bar", title="Sales by Salesperson", color="green")
    plt.xlabel("Salesperson")
    plt.ylabel("Sales Value (£)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

#prosseses the main menu and total sales menu

def main():
    df = load_data()

    while True:
        choice = main_menu()

        if choice == "2":
            print("Goodbye!")
            break

        while True:
            total_choice = total_menu()

            if total_choice == "1":
                all_sales_by_model(df)
            elif total_choice == "2":
                used_vs_new_sales(df)
            elif total_choice == "3":
                sales_by_salesperson(df)
            elif total_choice == "4":
                break

#running the main menu function which starts the program

main()