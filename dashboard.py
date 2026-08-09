# ==========================================
# E-Commerce Sales Dashboard
# Author: Dipak
# Description:
# This project analyzes e-commerce sales data
# and creates business insights and visualizations.
# ==========================================


from src.data_processing import load_data, clean_data, calculate_revenue
from src.analysis import (
    get_best_selling_product,
    get_monthly_revenue,
    get_top_cities,
    get_top_customers,
    get_category_revenue,
    get_payment_counts,
    get_order_status
)


from src.visualization import create_dashboard
def main():
    # Phase 1: Load Dataset

    df = load_data("data/Ecommerce_Sales_Project.xlsx")
    

    print("Dataset loaded successfully!")

        # Phase 2: Data Exploration
    print("\nDataset shape:")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nDataset information:")
    df.info()

    print("\nStatistical Summary:")
    print(df.describe())

    # Phase 3: Data Cleaning

    missing_before = df.isnull().sum().sum()


    duplicate_before = df.duplicated().sum()

    df= clean_data(df)

    missing_after  = df.isnull().sum().sum()

    duplicate_after = df.duplicated().sum()

    print("\n======================================================================================================")
    print("                    Data Cleaning Report                                                                ")
    print("========================================================================================================")

    print(f"Missing Values before: {missing_before}")
    print(f"Missing Values After: {missing_after}")

    print(f"\nDuplicate Rows Before: {duplicate_before}")
    print(f"Duplicate Rows After: {duplicate_after}")

    print("               ✅ Data Cleaning  Completed Successfully!                                                     ")

    # Phase 4: Business Analysis

    df = calculate_revenue(df)

    total_final_revenue = df["Final_Revenue"].sum()

    print("\n=====================================================================================")
    print("                      Revenue Analysis!")
    print("=======================================================================================")

    print(f"Total Final Revenue: ₹{total_final_revenue:,.2f}")

    print("\n====================================================================================")
    print("                     Best Selling Producct!")
    print("======================================================================================")

    best_product, units_sold = get_best_selling_product(df)

    print("\nBest Selling Product")
    print(f"Product: {best_product}")
    print(f"Units Sold: {units_sold}")

    monthly_revenue = get_monthly_revenue(df)

    print("\n==============================================================================")
    print("              Best Sales Month")
    print("================================================================================")

    print(f"month : {monthly_revenue.idxmax()}")
    print(f"Revenue : ₹{monthly_revenue.max():,.2f}")

    city_revenue = get_top_cities(df)

    print("\n==============================================================================")
    print("                Top 5 Revenue Cities ")
    print("================================================================================")

    print(city_revenue)

    top_customers = get_top_customers(df)

    print("\n======================================")
    print("      Top 5 Customers")
    print("======================================")

    print(top_customers)

    category_revenue = get_category_revenue(df)

    print("\n======================================")
    print("      Revenue by Category")
    print("======================================")

    print(category_revenue)


    payment_count = get_payment_counts(df)
        
    print("\n======================================")
    print("    Most Preferred Payment Method")
    print("======================================")

    print(f"Payment Method : {payment_count.idxmax()}")
    print(f"Orders         : {payment_count.max()}")

    order_status = get_order_status(df)

    print("\n======================================")
    print("        Order Status Report")
    print("======================================")

    print(order_status)


    # Phase 5: Data Visualization

    create_dashboard(
        monthly_revenue,
        category_revenue,
        city_revenue,
        payment_count,
        order_status,
        df
    )
if __name__ == "__main__":
    main()

