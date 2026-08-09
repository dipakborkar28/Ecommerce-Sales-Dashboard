
import matplotlib.pyplot as plt
import seaborn as sns



def create_dashboard(
    monthly_revenue,
    category_revenue,
    city_revenue,
    payment_count,
    order_status,
    df
):
    """Create and display the E-Commerce Executive Dashboard."""

    sns.set_theme(style="darkgrid")

    fig, axes = plt.subplots(
        3,
        2,
        figsize=(18, 16),
        constrained_layout=True
    )

    fig.suptitle(
        "E-Commerce Executive Dashboard",
        fontsize=20,
        fontweight="bold"
    )

    # Monthly Revenue
    sns.lineplot(
        x=monthly_revenue.index,
        y=monthly_revenue.values,
        marker="o",
        linewidth=2.5,
        color="royalblue",
        ax=axes[0,0]
    )

    axes[0,0].set_title("Monthly Revenue Trend")
    axes[0,0].set_xlabel("Months")
    axes[0,0].set_ylabel("Final Revenue (₹)")
    plt.setp(
        axes[0,0].get_xticklabels(),
        rotation=45
    )

    # Category Revenue
    sns.barplot(
        x=category_revenue.index,
        y=category_revenue.values,
        hue=category_revenue.index,
        palette="Blues_r",
        legend=False,
        ax=axes[0,1]
    )

    axes[0,1].set_title("Category Wise Revenue")
    axes[0,1].set_ylabel("Revenue (₹)")

    # Top Cities
    sns.barplot(
        x=city_revenue.index,
        y=city_revenue.values,
        hue=city_revenue.index,
        palette="Greens_r",
        legend=False,
        ax=axes[1,0]
    )

    axes[1,0].set_title("Top 5 Revenue Cities")
    axes[1,0].set_xlabel("Revenue (₹)")
    axes[1,0].set_ylabel("City")

    # Payment Method
    sns.barplot(
        x=payment_count.index,
        y=payment_count.values,
        hue=payment_count.index,
        palette="Purples_r",
        legend=False,
        ax=axes[1,1]
    )

    axes[1,1].set_title("Payment Method")
    axes[1,1].set_ylabel("Number of Orders")
    axes[1,1].tick_params(axis="x", rotation=20)

    # Order Status
    sns.barplot(
        x=order_status.index,
        y=order_status.values,
        hue=order_status.index,
        palette="Set2",
        legend=False,
        ax=axes[2,0]
    )

    axes[2,0].set_title("Order Status")
    axes[2,0].set_ylabel("Number of Orders")
    axes[2,0].tick_params(axis="x", rotation=20)

    # Price Distribution
    sns.histplot(
        data=df,
        x="Price",
        bins=10,
        kde=True,
        ax=axes[2,1]
    )

    axes[2,1].set_title("Price Distribution")
    axes[2,1].set_xlabel("Price (₹)")
    axes[2,1].set_ylabel("Number of Products")
    # plt.savefig("images/dashboard.png", dpi=300, bbox_inches="tight")

    plt.show()