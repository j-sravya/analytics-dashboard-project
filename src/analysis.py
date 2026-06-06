"""E-commerce sales analytics project.

This script generates a synthetic Indian e-commerce sales dataset, performs
basic cleaning and exploratory analysis, creates KPI summaries, and saves
matplotlib charts into the visuals folder.
"""

from pathlib import Path
import random

import matplotlib
import pandas as pd


matplotlib.use("Agg")
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "ecommerce_sales_data.csv"
VISUALS_DIR = PROJECT_ROOT / "visuals"


CITIES = [
    ("Bengaluru", "Karnataka"),
    ("Hyderabad", "Telangana"),
    ("Mumbai", "Maharashtra"),
    ("Delhi", "Delhi"),
    ("Chennai", "Tamil Nadu"),
    ("Pune", "Maharashtra"),
    ("Kolkata", "West Bengal"),
    ("Ahmedabad", "Gujarat"),
    ("Jaipur", "Rajasthan"),
    ("Lucknow", "Uttar Pradesh"),
    ("Kochi", "Kerala"),
    ("Indore", "Madhya Pradesh"),
]

PRODUCTS = {
    "Electronics": [
        ("Smartphone", 22000),
        ("Bluetooth Speaker", 2800),
        ("Wireless Earbuds", 3500),
        ("Laptop", 58000),
        ("Smart Watch", 6500),
    ],
    "Fashion": [
        ("Men's Casual Shirt", 1200),
        ("Women's Kurti", 1500),
        ("Running Shoes", 3200),
        ("Denim Jeans", 2100),
        ("Ethnic Saree", 2800),
    ],
    "Home & Kitchen": [
        ("Mixer Grinder", 4200),
        ("Cookware Set", 3500),
        ("Bedsheet Set", 1800),
        ("Air Fryer", 7800),
        ("Storage Containers", 900),
    ],
    "Beauty": [
        ("Face Serum", 950),
        ("Hair Dryer", 1800),
        ("Sunscreen Lotion", 650),
        ("Makeup Kit", 2200),
        ("Shampoo Combo", 800),
    ],
    "Grocery": [
        ("Basmati Rice Pack", 1100),
        ("Cooking Oil Can", 950),
        ("Dry Fruit Box", 1400),
        ("Tea Powder Pack", 450),
        ("Snack Combo", 350),
    ],
    "Accessories": [
        ("Laptop Backpack", 1700),
        ("Phone Case", 450),
        ("Leather Wallet", 900),
        ("Sunglasses", 1300),
        ("Travel Duffel Bag", 2400),
    ],
}


def generate_sample_dataset(rows: int = 1500, seed: int = 42) -> pd.DataFrame:
    """Generate realistic synthetic e-commerce sales data."""
    random.seed(seed)
    records = []
    order_dates = pd.date_range("2024-01-01", "2025-12-31", freq="D")
    segments = ["Consumer", "Corporate", "Small Business"]
    payment_methods = ["UPI", "Credit Card", "Debit Card", "Cash on Delivery", "Net Banking"]
    shipping_types = ["Standard", "Express", "Same Day"]
    category_weights = {
        "Electronics": 0.24,
        "Fashion": 0.22,
        "Home & Kitchen": 0.17,
        "Beauty": 0.14,
        "Grocery": 0.13,
        "Accessories": 0.10,
    }

    for i in range(1, rows + 1):
        category = random.choices(
            list(category_weights.keys()), weights=list(category_weights.values()), k=1
        )[0]
        product_name, base_price = random.choice(PRODUCTS[category])
        city, state = random.choices(
            CITIES,
            weights=[13, 13, 11, 9, 8, 8, 7, 6, 6, 6, 5, 4],
            k=1,
        )[0]
        order_date = random.choice(order_dates)
        quantity = random.choices([1, 2, 3, 4, 5], weights=[45, 25, 15, 10, 5], k=1)[0]
        seasonal_multiplier = 1.18 if order_date.month in [9, 10, 11] else 1.0
        price_variation = random.uniform(0.88, 1.16)
        unit_price = round(base_price * seasonal_multiplier * price_variation, 2)
        total_sales = round(quantity * unit_price, 2)
        margin = {
            "Electronics": random.uniform(0.09, 0.18),
            "Fashion": random.uniform(0.18, 0.32),
            "Home & Kitchen": random.uniform(0.14, 0.26),
            "Beauty": random.uniform(0.22, 0.36),
            "Grocery": random.uniform(0.06, 0.14),
            "Accessories": random.uniform(0.16, 0.30),
        }[category]
        profit = round(total_sales * margin, 2)
        shipping = random.choices(shipping_types, weights=[62, 28, 10], k=1)[0]
        delivery_days = {
            "Standard": random.randint(4, 8),
            "Express": random.randint(2, 4),
            "Same Day": random.randint(0, 1),
        }[shipping]

        records.append(
            {
                "order_id": f"ORD-{100000 + i}",
                "order_date": order_date.strftime("%Y-%m-%d"),
                "customer_id": f"CUST-{random.randint(1000, 1999)}",
                "customer_segment": random.choices(segments, weights=[64, 22, 14], k=1)[0],
                "product_category": category,
                "product_name": product_name,
                "quantity": quantity,
                "unit_price": unit_price,
                "total_sales": total_sales,
                "profit": profit,
                "city": city,
                "state": state,
                "payment_method": random.choices(payment_methods, weights=[45, 20, 15, 12, 8], k=1)[0],
                "shipping_type": shipping,
                "delivery_days": delivery_days,
            }
        )

    df = pd.DataFrame(records)

    # Add a few controlled missing values to demonstrate cleaning.
    for col in ["payment_method", "shipping_type"]:
        missing_indexes = df.sample(frac=0.01, random_state=seed + len(col)).index
        df.loc[missing_indexes, col] = None

    return df


def load_or_create_dataset() -> pd.DataFrame:
    """Load the dataset if present; otherwise create it."""
    if DATA_PATH.exists():
        return pd.read_csv(DATA_PATH)

    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df = generate_sample_dataset()
    df.to_csv(DATA_PATH, index=False)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean dates, remove duplicates, and handle missing values."""
    cleaned = df.copy()
    cleaned["order_date"] = pd.to_datetime(cleaned["order_date"], errors="coerce")
    cleaned = cleaned.drop_duplicates(subset=["order_id"])
    cleaned = cleaned.dropna(subset=["order_date", "customer_id", "product_category"])
    cleaned["payment_method"] = cleaned["payment_method"].fillna("Unknown")
    cleaned["shipping_type"] = cleaned["shipping_type"].fillna("Standard")
    cleaned["quantity"] = cleaned["quantity"].fillna(1).astype(int)
    cleaned["unit_price"] = cleaned["unit_price"].fillna(cleaned["unit_price"].median())
    cleaned["total_sales"] = cleaned["quantity"] * cleaned["unit_price"]
    cleaned["profit"] = cleaned["profit"].fillna(cleaned["profit"].median())
    cleaned["month"] = cleaned["order_date"].dt.to_period("M").astype(str)
    return cleaned


def generate_kpis(df: pd.DataFrame) -> dict:
    """Calculate dashboard-level KPIs."""
    total_revenue = df["total_sales"].sum()
    total_profit = df["profit"].sum()
    total_orders = df["order_id"].nunique()
    average_order_value = total_revenue / total_orders
    return {
        "Total Revenue": total_revenue,
        "Total Profit": total_profit,
        "Total Orders": total_orders,
        "Average Order Value": average_order_value,
        "Top Category": df.groupby("product_category")["total_sales"].sum().idxmax(),
        "Best City": df.groupby("city")["total_sales"].sum().idxmax(),
        "Most Used Payment Method": df["payment_method"].mode()[0],
    }


def save_bar_chart(series: pd.Series, title: str, xlabel: str, ylabel: str, filename: str) -> None:
    """Save a clean horizontal bar chart."""
    plt.figure(figsize=(10, 6))
    series.sort_values().plot(kind="barh", color="#2f80ed")
    plt.title(title, fontsize=14, weight="bold")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(VISUALS_DIR / filename, dpi=160)
    plt.close()


def create_visualizations(df: pd.DataFrame) -> None:
    """Create and save all portfolio visuals."""
    VISUALS_DIR.mkdir(parents=True, exist_ok=True)

    monthly_sales = df.groupby("month")["total_sales"].sum()
    plt.figure(figsize=(12, 6))
    monthly_sales.plot(kind="line", marker="o", color="#0f766e", linewidth=2)
    plt.title("Monthly Sales Trend", fontsize=14, weight="bold")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(VISUALS_DIR / "monthly_sales_trend.png", dpi=160)
    plt.close()

    save_bar_chart(
        df.groupby("product_category")["total_sales"].sum(),
        "Revenue by Category",
        "Revenue",
        "Product Category",
        "revenue_by_category.png",
    )
    save_bar_chart(
        df.groupby("product_name")["total_sales"].sum().sort_values(ascending=False).head(10),
        "Top 10 Products by Revenue",
        "Revenue",
        "Product",
        "top_10_products.png",
    )
    save_bar_chart(
        df.groupby("city")["total_sales"].sum().sort_values(ascending=False).head(10),
        "Top Cities by Sales",
        "Revenue",
        "City",
        "city_wise_sales.png",
    )
    save_bar_chart(
        df.groupby("product_category")["profit"].sum(),
        "Profit by Category",
        "Profit",
        "Product Category",
        "profit_by_category.png",
    )

    for column, title, filename in [
        ("customer_segment", "Customer Segment Distribution", "customer_segment_distribution.png"),
        ("payment_method", "Payment Method Usage", "payment_method_usage.png"),
        ("shipping_type", "Shipping Type Distribution", "shipping_type_distribution.png"),
    ]:
        plt.figure(figsize=(8, 6))
        df[column].value_counts().plot(kind="bar", color="#f2994a")
        plt.title(title, fontsize=14, weight="bold")
        plt.xlabel(column.replace("_", " ").title())
        plt.ylabel("Order Count")
        plt.xticks(rotation=25, ha="right")
        plt.tight_layout()
        plt.savefig(VISUALS_DIR / filename, dpi=160)
        plt.close()


def print_business_insights(df: pd.DataFrame, kpis: dict) -> None:
    """Print concise business insights for terminal output."""
    top_product = df.groupby("product_name")["total_sales"].sum().idxmax()
    top_segment = df["customer_segment"].value_counts().idxmax()
    top_month = df.groupby("month")["total_sales"].sum().idxmax()
    avg_delivery = df["delivery_days"].mean()

    print("\nE-Commerce Sales Analytics Summary")
    print("=" * 42)
    for key, value in kpis.items():
        if isinstance(value, float):
            print(f"{key}: Rs. {value:,.2f}")
        else:
            print(f"{key}: {value}")

    print("\nKey Business Insights")
    print("-" * 24)
    print(f"1. {kpis['Top Category']} is the highest revenue-generating category.")
    print(f"2. {kpis['Best City']} contributes the strongest city-level sales performance.")
    print(f"3. {top_segment} customers place the largest number of orders.")
    print(f"4. {kpis['Most Used Payment Method']} is the most preferred payment method.")
    print(f"5. {top_product} is the best-performing product by revenue.")
    print(f"6. Sales peaked in {top_month}, indicating seasonal demand patterns.")
    print(f"7. Average delivery time is {avg_delivery:.1f} days across all orders.")


def main() -> None:
    raw_df = load_or_create_dataset()
    cleaned_df = clean_data(raw_df)
    cleaned_df.to_csv(DATA_PATH, index=False)
    kpis = generate_kpis(cleaned_df)
    create_visualizations(cleaned_df)
    print_business_insights(cleaned_df, kpis)


if __name__ == "__main__":
    main()
