import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load JSON data
file_path = '/Users/ashishbarwa/Desktop/Inlighn Tech/Portfolio Project 2/zomato_data.csv'  # Update with the actual file path
data = pd.read_csv(file_path)

#display all the columns
pd.set_option("display.max_columns", None)

#clean 'rate' column
data["rate"] = data["rate"].astype(str).str.replace("/5","",regex=True).replace("Nan",None)
data["rate"] = pd.to_numeric(data["rate"], errors="coerce")

#check data type
print("Columns Data Types:\n", data.dtypes)

#check for missing/null values
print("\nMissing Values in Each Column:\n", data.isnull().sum())

#plot count plot
plt.figure(figsize =(12,6))
sns.countplot(
    y=data["listed_in(type)"],
    order=data["listed_in(type)"].value_counts().index,
    hue=data["listed_in(type)"],  # Assign hue to avoid the deprecation warning
    legend=False,  # Disable legend since hue is the same as y
    palette="viridis"
)

#add labels and title
plt.xlabel("count")
plt.ylabel("Restaurant Type")
plt.title("Distribution of Restaurant Types")
plt.show()

# Group by 'listed_in(type)' and sum votes
votes_per_type = data.groupby("listed_in(type)")["votes"].sum().reset_index()

# Sort by total votes for better visualization
votes_per_type = votes_per_type.sort_values(by="votes", ascending=False)

# Plot the total votes per restaurant type
plt.figure(figsize=(12, 6))
sns.barplot(
    y=votes_per_type["listed_in(type)"],
    x=votes_per_type["votes"],
    hue=data["listed_in(type)"],  # Assign hue to avoid the deprecation warning
    legend=False,
    palette="magma"
)

# Add labels and title
plt.xlabel("Total Votes")
plt.ylabel("Restaurant Type")
plt.title("Total Votes per Restaurant Type")
plt.show()

# Plot histogram
plt.figure(figsize=(10, 6))
sns.histplot(data["rate"], bins=20, kde=True, color="teal")

# Add labels and title
plt.xlabel("Rating")
plt.ylabel("Count")
plt.title("Distribution of Restaurant Ratings")
plt.xticks([1, 2, 3, 4, 5])  # Ensure proper tick marks
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Plot count plot
plt.figure(figsize=(12, 6))
sns.countplot(
    y=data["approx_cost(for two people)"],
    order=data["approx_cost(for two people)"].value_counts().index,
    hue=data["listed_in(type)"],  # Assign hue to avoid the deprecation warning
    legend=False,
    palette="coolwarm"
)

# Add labels and title
plt.xlabel("Count")
plt.ylabel("Approximate Cost (for Two People)")
plt.title("Distribution of Approximate Cost for Two People")
plt.show()

# Drop missing values in 'rate' and 'online_order' columns
data = data.dropna(subset=["rate", "online_order"])

# Create box plot
plt.figure(figsize=(8, 6))
sns.boxplot(x=data["online_order"], y=data["rate"],
            hue=data["listed_in(type)"],  # Assign hue to avoid the deprecation warning
            legend=False,
            palette="coolwarm")

# Add labels and title
plt.xlabel("Online Order Availability")
plt.ylabel("Restaurant Rating")
plt.title("Comparison of Ratings: Online vs. Offline Orders")
plt.show()

# Create a pivot table: Count of restaurants by 'listed_in(type)' and 'online_order'
pivot_table = data.pivot_table(
    index="listed_in(type)",
    columns="online_order",
    values="name",  # 'name' column counts unique restaurants
    aggfunc="count",
    fill_value=0
)

# Plot heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_table, annot=True, fmt="d", cmap="coolwarm", linewidths=0.5)

# Add labels and title
plt.xlabel("Online Order Availability")
plt.ylabel("Restaurant Type")
plt.title("Number of Restaurants Offering Online vs. Offline Orders")
plt.show()


# Display the first few rows
print(data.head(1))
ß