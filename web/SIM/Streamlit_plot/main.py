import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

st.title ('BORMA Sales Data')

df = pd.read_csv ('./Data/dago.csv')
st.dataframe(df)

plt.figure(figsize=(15, 8))
sns.lineplot(x='tanggal', y='sales', data=df, marker='o',markersize=20)
 
# Set plot labels and title
plt.xlabel('Tanggal')
plt.ylabel('Sales')
plt.title('Sales for All Stores (Grouped by Date)')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
plt.legend(title='Store')  # Add a legend with a title
plt.tight_layout()
st.pyplot(plt)