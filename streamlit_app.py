import streamlit
import pandas

streamlit.title('🥣 My Parents New Health Diner')
streamlit.header('🐔 Breakfast menu')
streamlit.text('🥗 Omega 3 & Blueberry Ouatmeal')
streamlit.text('🥑 Kamle, Spinach & Rocket Smoothie')
streamlit.text('🍞 Hard-boiled Free Range egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Avocado','strawberries'])

#display the table on the page
streamlit.dataframe(my_fruit_list)

