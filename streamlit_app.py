import streamlit
import pandas

streamlit.title('New healthy Menu')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and blueberry Oatmeal')
streamlit.text('🥗 Spinach and rocket smothie')
streamlit.text('🐔 Hard boiled free-range eggs')
streamlit.text('🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# Display the table on the page.
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
