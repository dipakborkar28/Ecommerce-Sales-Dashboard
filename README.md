# E-Commerce Sales Dashboard

## 📊 Project Description

This project analyzes e-commerce sales data using Python and creates an interactive-style dashboard with Seaborn and Matplotlib.

The project performs data cleaning, revenue analysis, business analysis, and data visualization to generate useful business insights.

## 🚀 Features

- Load e-commerce sales data from Excel
- Explore dataset structure and statistics
- Handle missing values and duplicate records
- Calculate revenue and final revenue after discounts
- Find the best-selling product
- Analyze monthly revenue
- Identify top 5 revenue-generating cities
- Identify top 5 customers
- Analyze revenue by category
- Analyze preferred payment methods
- Analyze order status
- Create an E-Commerce Executive Dashboard

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Excel

## 📁 Project Structure

```text
Ecommerce-Sales-Dashboard/
│
├── data/
│   └── Ecommerce_Sales_Project.xlsx
│
├── src/
│   ├── data_processing.py
│   ├── analysis.py
│   └── visualization.py
│
├── dashboard.py
├── requirements.txt
└── README.md


## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/dipakborkar28/Ecommerce-Sales-Dashboard.git
cd Ecommerce-Sales-Dashboard



## 💡 Business Insights

The analysis provides insights into:

- Total final revenue generated
- Best-selling product based on units sold
- Best-performing month by revenue
- Top 5 cities by revenue
- Top 5 customers by revenue
- Revenue contribution by product category
- Most preferred payment method
- Distribution of order statuses
- Distribution of product prices


## 🧹 Data Processing

The project performs the following data-processing steps:

- Loads the sales dataset from an Excel file.
- Checks the dataset for missing values and duplicate records.
- Fills missing discount values with `0`.
- Fills missing city values with `"Unknown"`.
- Removes duplicate rows.
- Calculates gross revenue using quantity and price.
- Calculates final revenue after applying discounts.
- Converts order dates into a proper datetime format for monthly analysis.

## 🔄 How It Works

The project follows a simple data-analysis workflow:

```text
Load Data
    ↓
Explore Data
    ↓
Clean Data
    ↓
Calculate Revenue
    ↓
Perform Business Analysis
    ↓
Create Visualizations
    ↓
Display Executive Dashboard


## 👨‍💻 Author

**Dipak Borkar**

This project was created as part of my journey in learning Python, Pandas, Seaborn, Matplotlib, and data analysis.