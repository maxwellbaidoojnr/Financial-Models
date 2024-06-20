import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import warnings 

# Declares warnings
warnings.filterwarnings("ignore")
# Reading dataset
credit_card = pd.read_csv("Credit_Card.csv")
# print(credit_card.head)
df = credit_card.copy()
print(df.describe())
print(df.corr())
print(df.isnull().sum())
print(df["LIMIT_BAL"].std())

# Visualisation of data
plt.figure(figsize=(10,6))
sns.histplot(df["LIMIT_BAL"], bins=30, kde=True)
plt.title("Histogram of Balance Limit")
plt.xlabel("Credit Limit")
plt.ylabel("Frequency")
plt.show()

# Scatter diagram to show relationship between age and  balance limit
plt.figure(figsize=(10,6))
sns.scatterplot(x="AGE", y="LIMIT_BAL", data=df)
plt.title ("Scatter Diagram of Age  against  Balance Limit")
plt.xlabel("Age")
plt.ylabel("Balance Limit")
plt.show()



