#This process is call data preprocess in ML
import pandas as pd

data = pd.read_csv("Dataset.csv")
#Show first 5 rows
print (data.head())
print(data.describe())
print(data["workingday"])

#Basic financial matrix
mean_data = data["registered"].mean()
median_data = data["registered"].median()
print (mean_data)
print (median_data)

#Visualisation
import matplotlib.pyplot as plt
plt.plot(data['registered'], data['workingday'])
plt.xlabel("registered")
plt.ylabel("workingday")
plt.title("Scatter Graph")
plt.show()


#Visualisation 2
import matplotlib.pyplot as plt
plt.plot(data['workingday'], data['registered'])
plt.xlabel("workingday")
plt.ylabel("registered")
plt.title("Scatter Graph")
plt.show()