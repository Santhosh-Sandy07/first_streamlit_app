import streamlit
streamlit.title("My healthy Dinner")
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg') 
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import streamlit as st
import pandas as pd

# Load the menu data (replace "your_menu_data.csv" with the actual file path or URL)
menu_data = pd.read_csv("your_menu_data.csv")

# Sidebar title and subtitle
st.sidebar.title("Hotel Menu")
st.sidebar.subheader("Explore our delightful offerings")

# Display menu items
st.title("Menu")

# Display menu items in a table
st.table(menu_data)

# Filter menu by category
categories = menu_data['Category'].unique()
selected_category = st.sidebar.selectbox('Select a category', categories)
filtered_menu = menu_data[menu_data['Category'] == selected_category]

# Display filtered menu items
st.subheader(f"{selected_category} Items")
st.table(filtered_menu)

# Filter menu by price range
price_range = st.sidebar.slider('Select price range', float(menu_data['Price'].min()), float(menu_data['Price'].max()), (float(menu_data['Price'].min()), float(menu_data['Price'].max())))
price_filtered_menu = menu_data[(menu_data['Price'] >= price_range[0]) & (menu_data['Price'] <= price_range[1])]

# Display price-filtered menu items
st.subheader('Items in Selected Price Range')
st.table(price_filtered_menu)
