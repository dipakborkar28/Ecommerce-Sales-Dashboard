import pandas as pd

def get_best_selling_product(df):
    """Find the product with the highest total quantity sold."""

    product_quantity = df.groupby("Product")["Quantity"].sum()
    best_product = product_quantity.idxmax()
    units_sold = product_quantity.max()
    return best_product, units_sold

def get_monthly_revenue(df):
    """Calculate total final revenue for each month."""
    df["Order_Date"] = pd.to_datetime(df["Order_Date"])
    months = df["Order_Date"].dt.month_name()
    monthly_revenue = df.groupby(months)["Final_Revenue"].sum()
    months_order = ["January", "February","March",
                "April","May","June","July",
                "August","September","October",
                "November","December"]
    monthly_revenue = monthly_revenue.reindex(months_order).dropna()
    return monthly_revenue


def get_top_cities(df):
    """Find the top 5 cities based on final revenue."""
    city_revenue = (
                    df.groupby("City")["Final_Revenue"]
                      .sum()
                      .sort_values(ascending=False)
                      .head(5)
                      )
    return city_revenue

def get_top_customers(df):
    """Find the top 5 customers based on final revenue."""
    top_customers = (
        df.groupby("Customer")["Final_Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )
    return top_customers

def get_category_revenue(df):
    """Calculate total final revenue for each product category."""
    category_revenue = (
    df.groupby("Category")["Final_Revenue"]
      .sum()
      .sort_values(ascending=False)
)
    return category_revenue

def get_payment_counts(df):
    """Count the number of orders for each payment method."""
    payment_count = df["Payment_Method"].value_counts()
    return payment_count


def get_order_status(df):
    """Count the number of orders for each order status."""
    order_status = df["Status"].value_counts()
    return order_status