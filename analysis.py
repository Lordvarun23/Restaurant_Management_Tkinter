import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv(r"Dataset.csv")

sum_fries=df['Fries'].sum()
sum_burger=df['Burger'].sum()
sum_pizza=df['Pizza'].sum()
sum_ice=df['Ice Cream'].sum()
sum_drinks=df['Drinks'].sum()

y=np.array([sum_fries,sum_burger,sum_pizza,sum_ice,sum_drinks])
labels=["Fries","Burger","Pizza","Ice Cream","Drinks"]
plt.pie(y,labels=labels)
plt.show()