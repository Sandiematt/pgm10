import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Price': [250000, 300000, 350000, 400000, 450000,500000],
    'Area': [1500, 1800, 2000, 2200, 2500,3000],
    'House Type': ['Apartment', 'House', 'Condo', 'Townhouse', 'Duplex','Apartment']
}


df = pd.DataFrame(data)


df.to_csv("housing_data.csv", index=False)


@st.cache_data
def load_data():
    return pd.read_csv("housing_data.csv")

data = load_data()

st.title("Housing Management Dashboard")


st.sidebar.header("Filters")
min_price = st.sidebar.number_input("Minimum Price", value=data['Price'].min())
max_price = st.sidebar.number_input("Maximum Price", value=data['Price'].max())


filtered_data = data[(data['Price'] >= min_price) & (data['Price'] <= max_price)]


st.write("Filtered Data:")
st.write(filtered_data)


st.header("Data Visualization")


st.subheader("Histogram of Prices")
plt.figure(figsize=(10, 6))
sns.histplot(data['Price'], kde=True)
st.pyplot()


st.subheader("Scatter Plot: Price vs Area")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Area', y='Price', data=data)
st.pyplot()


st.subheader("Bar Chart: House Type Counts")
house_type_counts = data['House Type'].value_counts()
plt.figure(figsize=(10, 6))
sns.barplot(x=house_type_counts.index, y=house_type_counts.values)
plt.xticks(rotation=45)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

