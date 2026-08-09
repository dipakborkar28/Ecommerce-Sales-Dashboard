import pandas as pd
def load_data(file_path):
    """Load the Excel dataset into a pandas DataFrame."""
    try:  
       df = pd.read_excel(file_path)
       return df
    
    except FileNotFoundError:
        print(f"Error: file not found {file_path}")
        return None

    except Exception as e:
        print(f"Error while loading file:{e}")
        return None
    


def clean_data(df):
    """Clean missing values and remove duplicate rows from the dataset."""
    if df is None:
        print("Error: No data avalible for cleaning")
        return None
    df["Discount_%"] = df["Discount_%"].fillna(0)
    df["City"] = df["City"].fillna("Unknown")
    df.drop_duplicates(inplace=True)
    return df


def calculate_revenue(df):
    """Calculate gross revenue and final revenue after applying discounts."""
    required_columns = [
        "Quantity",
        "Price",
        "Discount_%"
    ]
    for column in required_columns :
        if column not in df.columns:
            print(f"Error : Missing required columns : {column}")
            return None

    df["Revenue"] = df["Quantity"] * df["Price"]
    df["Final_Revenue"] = (
        df["Revenue"]
        - (df["Revenue"] * df["Discount_%"] / 100)
    )
   
    
    return df