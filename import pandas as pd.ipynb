
import pandas as pd

# Load data
<<<<<<< HEAD
df = pd.read_csv('client_dataset.csv')
df.head()
=======
file_path = 'Resources/client_dataset.csv'
df = pd.read_csv(resources/clent_dataset.csv)
>>>>>>> e43380b21f4ba474f537bd1bef12c916a88025d5

# View the column names in the data
print("Column Names:", df.columns.tolist())

# Use the describe function to gather some basic statistics
description = df.describe()
print("Basic Statistics:\n", description)

# Use this space to do any additional research
# and familiarize yourself with the data.
# Top 3 item categories by entries
top_categories = df['category'].value_counts().head(3)
print("Top 3 Categories by Entries:\n", top_categories)

# For the category with the most entries, which subcategory had the most entries?
top_category = top_categories.index[0]
top_subcategory = df[df['category'] == top_category]['subcategory'].value_counts().head(1)
print(f"Subcategory with most entries in '{top_category}':\n", top_subcategory)

# Which five clients had the most entries in the data?
top_clients = df['client_id'].value_counts().head(5)
top_clients_list = top_clients.index.tolist()
print("Top 5 Clients by Entries:\n", top_clients)
print("Top 5 Client IDs:", top_clients_list)

# How many total units (the qty column) did the client with the most entries order?
top_client_units = df[df['client_id'] == top_clients_list[0]]['qty'].sum()
print("Total Units Ordered by Top Client:", top_client_units)

# Create a column that calculates the subtotal for each line using the unit_price and the qty
df['line_subtotal'] = df['unit_price'] * df['qty']

# Create a column for shipping price.
# Assume a shipping price of $7 per pound for orders over 50 pounds and $10 per pound for items 50 pounds or under.
def calculate_shipping(row):
    total_weight = row['unit_weight'] * row['qty']
    if total_weight > 50:
        return total_weight * 7
    else:
        return total_weight * 10

df['total_weight'] = df['unit_weight'] * df['qty']
df['shipping_price'] = df.apply(calculate_shipping, axis=1)

# Create a column for the total price using the subtotal and the shipping price along with a sales tax of 9.25%
df['line_price'] = (df['line_subtotal'] + df['shipping_price']) * 1.0925

# Create a column for the cost of each line using unit cost, qty, and
# shipping price (assume the shipping cost is exactly what is charged to the client).
df['line_cost'] = df['unit_cost'] * df['qty'] + df['shipping_price']

# Create a column for the profit of each line using line cost and line price
df['line_profit'] = df['line_price'] - df['line_cost']

# Check your work using the totals above
receipts = {
    2742071: 152811.89,
    2173913: 162388.71,
    6128929: 923441.25
}
for order_id, expected_total in receipts.items():
    calculated_total = df[df['order_id'] == order_id]['line_price'].sum()
    print(f"Order {order_id} total: ${calculated_total:.2f} (Expected: ${expected_total})")

# How much did each of the top 5 clients by quantity spend? Check your work from Part 1 for client ids.
top_clients_summary = df[df['client_id'].isin(top_clients_list)].groupby('client_id').agg({
    'qty': 'sum',
    'shipping_price': 'sum',
    'line_price': 'sum',
    'line_cost': 'sum',
    'line_profit': 'sum'
}).reset_index()

# Create a summary DataFrame showing the totals for the for the top 5 clients with the following information:
# total units purchased, total shipping price, total revenue, and total profit.
# Define a function that converts a dollar amount to millions.
def to_millions(value):
    return value / 1_000_000

# Apply the currency_format_millions function to only the money columns.
columns_to_format = ['shipping_price', 'line_price', 'line_cost', 'line_profit']
top_clients_summary[columns_to_format] = top_clients_summary[columns_to_format].applymap(to_millions)

# Format the data and rename the columns to names suitable for presentation.
top_clients_summary.rename(columns={
    'client_id': 'Client ID',
    'qty': 'Units',
    'shipping_price': 'Shipping (millions)',
    'line_price': 'Total Revenue (millions)',
    'line_cost': 'Total Cost (millions)',
    'line_profit': 'Total Profit (millions)'
}, inplace=True)

# Sort the updated data by "Total Profit (millions)" form highest to lowest and assign the sort to a new DataFrame.
top_clients_summary = top_clients_summary.sort_values('Total Profit (millions)', ascending=False)

# Display results
print("\nTop 5 Clients Summary:")
print(top_clients_summary)

# Summary of findings
summary = """
The client with the highest total profit is Client ID {client_id} with a profit of ${profit:.2f} million.
Other clients show significant spending and profitability trends, with notable shipping costs contributing to profit margins.
""".format(
    client_id=top_clients_summary.iloc[0]['Client ID'],
    profit=top_clients_summary.iloc[0]['Total Profit (millions)']
)
print(summary)
