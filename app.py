import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# https://sandie.streamlit.app/
username = "user"
password = "password"


def authenticate(username, password):
    if username == "user" and password == "password":
        return True
    else:
        return False


def is_user_logged_in():
    if "username" in st.session_state and "password" in st.session_state:
        return authenticate(st.session_state["username"], st.session_state["password"])
    return False


if not is_user_logged_in():
    st.title("Login To View The Data")

    username_input = st.sidebar.text_input("Username")
    password_input = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if authenticate(username_input, password_input):
            st.session_state["username"] = username_input
            st.session_state["password"] = password_input
        else:
            st.error("Incorrect username or password. Please try again.")
else:
    data = {
        'Price': [250000, 300000, 350000, 400000, 450000, 500000],
        'Area': [1500, 1800, 2000, 2200, 2500, 3000],
        'House Type': ['Apartment', 'House', 'Condo', 'Townhouse', 'Duplex', 'Apartment']
    }

    df = pd.DataFrame(data)

    st.title("Housing Management Dashboard")

    st.sidebar.header("Filters")
    min_price = st.sidebar.number_input("Minimum Price", value=df['Price'].min())
    max_price = st.sidebar.number_input("Maximum Price", value=df['Price'].max())

    filtered_data = df[(df['Price'] >= min_price) & (df['Price'] <= max_price)]

    st.write("Filtered Data:")
    st.write(filtered_data)

    st.header("Data Visualization")

    st.subheader("Histogram of Prices")
    plt.figure(figsize=(10, 6))
    sns.histplot(filtered_data['Price'], kde=True)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    st.subheader("Scatter Plot: Price vs Area")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Area', y='Price', data=filtered_data)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()

    st.subheader("Bar Chart: House Type Counts")
    house_type_counts = filtered_data['House Type'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=house_type_counts.index, y=house_type_counts.values)
    plt.xticks(rotation=45)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
