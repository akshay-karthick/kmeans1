# BDA Lab – K-Means Clustering Assignment
## Created by : AKSHAY KARTHICK ASR
## Reg.no : 212224230015

This repository contains the dataset and starter code for the **K-Means Clustering Lab Exercise**.

## Objective

Perform clustering on customer data using **K-Means algorithm** and visualize the clusters.

## Dataset

customers_large_dataset.csv

Columns used:

* AnnualIncome
* SpendingScore

## Program Steps

1. Load dataset using pandas
2. Select required columns
3. Apply K-Means clustering
4. Plot clusters using matplotlib

## Submission Instructions

### Step 1 – Fork Repository

Click **Fork** on the top-right of this repository.

### Step 2 – Clone Repository

```
git clone https://github.com/YOUR-USERNAME/BDA-KMeans-Clustering-Lab.git
```

### Step 3 – Create Submission Folder

Inside the `submissions` folder create a folder:

```
submissions/YourName_RegisterNumber
```

Example:

```
submissions/Ravi_21CS101
```

### Step 4 – Upload Files

Upload:

* Python code
* Output screenshot

Example:

```
submissions/Ravi_21CS101/kmeans.py
submissions/Ravi_21CS101/output.png
```

### Step 5 – Push and Create Pull Request

```
git add .
git commit -m "KMeans Lab Submission"
git push origin main
```

Then create a **Pull Request**.

## Important Rules

* Do not edit other folders
* Upload only inside your folder
* Follow naming format

### Python code
```
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
```

### Output

![alt text](<submissions/AKSHAY KARTHICK ASR 212224230015/Screenshot 2026-03-24 at 11.03.33 AM.png>)