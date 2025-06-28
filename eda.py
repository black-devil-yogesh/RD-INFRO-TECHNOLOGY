import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 
df = pd.read_excel("phones.xlsx")
plt.figure(figsize=(8, 5))
sns.histplot(df['Selling Price'], bins=20, kde=True, color='teal')
plt.title('Distribution of Selling Prices')
plt.xlabel('Selling Price (₹)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 6))
brand_rating = df.groupby('Brands')['Rating'].mean().sort_values(ascending=False).reset_index()
sns.barplot(data=brand_rating, x='Rating', y='Brands', hue='Brands',
             dodge=False, palette='mako', legend=False)
plt.title('Average Rating by Brand')
plt.xlabel('Average Rating')
plt.ylabel('Brand')
plt.tight_layout()
plt.show()
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df,
                 x='Original Price',
                 y='discount percentage', 
                 hue='Brands', 
                 palette='Set2')
plt.title('Discount vs Original Price')
plt.xlabel('Original Price (₹)')
plt.ylabel('Discount Percentage')
plt.tight_layout()
plt.show()
fig = px.scatter(
    df,
    x="Selling Price",
    y="Rating",
    color="Brands",
    hover_data=["Models", "Memory", "Storage"],
    title="Rating vs Selling Price by Brand",)
fig.show()