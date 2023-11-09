import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import mysql.connector

# Connect to the MySQL database
db_connection = mysql.connector.connect(
  host="hostname",
  user="username",
  passwd="password",
  database="ecommerce_db"
)

# Query to extract necessary data
query = """
SELECT UserID, COUNT(OrderID) as OrderCount, AVG(TotalAmount) as AvgOrderValue
FROM Orders
GROUP BY UserID;
"""

# Load data into a Pandas DataFrame
df = pd.read_sql(query, con=db_connection)

# Preprocess the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[['OrderCount', 'AvgOrderValue']])

# Perform K-means clustering
kmeans = KMeans(n_clusters=3)  # Example with 3 clusters
df['Cluster'] = kmeans.fit_predict(scaled_data)

# Plot the results (as an example)
plt.scatter(df['OrderCount'], df['AvgOrderValue'], c=df['Cluster'])
plt.xlabel('Order Count')
plt.ylabel('Average Order Value')
plt.show()
