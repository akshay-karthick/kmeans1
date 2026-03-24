import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv("customers_large_dataset.csv")

x = data[['AnnualIncome', 'SpendingScore']]

kmeans = KMeans(n_clusters=5)
y = kmeans.fit_predict(x)

plt.scatter(x['AnnualIncome'], x['SpendingScore'], c=y)
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("K-Means Clustering")

plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=200)

plt.show()