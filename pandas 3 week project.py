import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_data(file_path):
    """Load CSV data with error handling."""
    try:
        data = pd.read_csv(file_path)
        print("✅ Data loaded successfully.")
        return data
    except FileNotFoundError:
        print("❌ Error: File not found.")
    except pd.errors.EmptyDataError:
        print("❌ Error: File is empty.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    return None


def clean_data(data):
    """Clean and prepare dataset."""
    try:
        # Convert Date column (DD/MM/YYYY format)
        data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)

        # Remove missing values
        data = data.dropna()

        # Ensure numeric columns are numeric
        data['Units Sold'] = pd.to_numeric(data['Units Sold'])
        data['Price (£)'] = pd.to_numeric(data['Price (£)'])
        data['Total Revenue (£)'] = pd.to_numeric(data['Total Revenue (£)'])

        print("✅ Data cleaned successfully.")
        return data

    except KeyError as e:
        print(f"❌ Missing column: {e}")
        return None
    except Exception as e:
        print(f"❌ Data cleaning error: {e}")
        return None


def generate_statistics(data):
    """Generate summary statistics using NumPy."""
    try:
        total_revenue = np.sum(data['Total Revenue (£)'])
        average_revenue = np.mean(data['Total Revenue (£)'])
        total_units = np.sum(data['Units Sold'])
        max_sale = np.max(data['Total Revenue (£)'])
        min_sale = np.min(data['Total Revenue (£)'])

        print("\n📊 ===== SUMMARY STATISTICS =====")
        print(f"Total Revenue: £{total_revenue:,.2f}")
        print(f"Average Revenue per Sale: £{average_revenue:,.2f}")
        print(f"Total Units Sold: {total_units}")
        print(f"Highest Single Sale Revenue: £{max_sale:,.2f}")
        print(f"Lowest Single Sale Revenue: £{min_sale:,.2f}")

    except Exception as e:
        print(f"❌ Statistics error: {e}")


def create_bar_chart(data):
    """Create bar chart showing revenue by category."""
    try:
        revenue_by_category = data.groupby('Category')['Total Revenue (£)'].sum()

        revenue_by_category.plot(kind='bar')
        plt.title("Total Revenue by Game Category")
        plt.xlabel("Category")
        plt.ylabel("Revenue (£)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"❌ Bar chart error: {e}")


def create_line_chart(data):
    """Create line chart showing monthly revenue trend."""
    try:
        data['Month'] = data['Date'].dt.to_period('M')
        monthly_revenue = data.groupby('Month')['Total Revenue (£)'].sum()

        monthly_revenue.plot(kind='line', marker='o')
        plt.title("Monthly Revenue Trend (2024)")
        plt.xlabel("Month")
        plt.ylabel("Revenue (£)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"❌ Line chart error: {e}")


def create_pie_chart(data):
    """Create pie chart showing sales distribution by game."""
    try:
        units_by_game = data.groupby('Game Title')['Units Sold'].sum()

        units_by_game.plot(kind='pie', autopct='%1.1f%%')
        plt.title("Sales Distribution by Game Title")
        plt.ylabel("")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"❌ Pie chart error: {e}")


def main():
    """Main program execution."""
    file_path = "GAME_SHOP_SALES_300_ROWS.CSV"

    data = load_data(file_path)

    if data is not None:
        data = clean_data(data)

        if data is not None:
            generate_statistics(data)
            create_bar_chart(data)
            create_line_chart(data)
            create_pie_chart(data)


if __name__ == "__main__":
    main()