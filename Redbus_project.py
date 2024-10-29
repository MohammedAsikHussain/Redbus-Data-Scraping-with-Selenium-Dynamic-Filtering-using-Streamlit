import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from datetime import time
import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='redbus_project'
)
mycursor = mydb.cursor(buffered=True)

#setting up streamlit page
st.set_page_config(layout="wide")
st.sidebar.title("🖥️Main Menu") 
menu_option = st.sidebar.selectbox("Menu", ["🏠 Home", "🚌 Select the Bus","📖 About Us"],index=0)

if menu_option == '🏠 Home':
    st.title("Welcome to the :red[REDBUS] Booking")
    st.logo("C:/Users/DELL/Downloads/rdc-redbus-logo.webp")
    st.subheader(":blue[Available States:]")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- Kerala 🌴 ")
        st.markdown("- Telangana 🌾")
        st.markdown("- Kadamba 🌾")
        st.markdown("- Rajasthan 🏜️")
        st.markdown("- NorthBengal 🏞️")
    with col2:
        st.markdown("- WestBengal 🐅")
        st.markdown("- Assam 🐘")
        st.markdown("- Bihar 🚜")
        st.markdown("- Punjab 🌾")
        st.markdown("- Chandigarh 🏙️")
                


if menu_option == '🚌 Select the Bus':
    selected_state = st.sidebar.selectbox('🗺️State',['Kerala','Telangana','Kadamba','Rajasthan','NorthBengal',
                                 'WestBengal','Assam','Punjab','Bihar','Chandigarh'])

    routes = []
    bus_types = []

    mycursor.execute(f"SELECT Route_name, Bus_type FROM redbus_bus_details WHERE State= '{selected_state}'")
    result = mycursor.fetchall()

    for i in result:
        routes.append(i[0])
        bus_types.append(i[1])

    unique_routes = list(set(routes))
    unique_bus_types = list(set(bus_types))
    

    col1, col2 = st.columns(2)
    with col1 :
        route = st.selectbox('📍Select Route',unique_routes,index=0)
        type = st.selectbox('🚍 Bus Type',unique_bus_types,index=0)

    with col2 :
        timing = st.slider("Bus Timings 🕒", value=(time(16, 30), time(20, 45)))
        rating = st.slider("Ratings 🌟", 0.0, 5.0, (2.0,4.0),step=1.0)
        price = st.slider("Prices 💸 ", 0.0, 5000.0, (300.0,1000.0),step=100.0) 

    start_time, end_time = timing
    min_rating, max_rating = rating
    min_price, max_price = price

    query = mycursor.execute(f''' SELECT * FROM redbus_bus_details 
                            WHERE Route_name = '{route}' 
                            AND Bus_type = '{type}' 
                            AND Ratings BETWEEN {min_rating} AND {max_rating}
                            AND Price BETWEEN {min_price} AND {max_price}
                            AND Start_time >= '{start_time}'
                            AND End_time <= '{end_time}'
                            ORDER BY Price DESC
                         ''')
   
    
    if st.button('Search Buses',type="primary"):
        mycursor.execute(query)
        out=mycursor.fetchall()
        df=pd.DataFrame(out,columns=[
                "ID","Bus_name","Bus_type","Start_time","End_time","Duration","Price",
                "Seats_Available","Ratings","Route_name","Route_link","State"
            ])
        df['Start_time'] = df['Start_time'].astype(str)
        df['Start_time'] = df['Start_time'].str.strip("0 days",)
        df['End_time'] = df['End_time'].astype(str)
        df['End_time'] = df['End_time'].str.strip("0 days",)
        
        st.write(df)
        
st.sidebar.image("C:/Users/DELL/Downloads/download.jpg",caption="www.redbus.in")


if menu_option == '📖 About Us':
    st.title("Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit")
    st.subheader(":blue[Domain:]  Transportation")
    st.subheader(":blue[Ojective:] ")
    st.markdown("The 'Redbus Data Scraping and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.")
    st.subheader(":blue[Overview:]") 
    st.markdown("Selenium: Selenium is a tool used for automating web browsers. It is commonly used for web scraping, which involves extracting data from websites. Selenium allows you to simulate human interactions with a web page, such as clicking buttons, filling out forms, and navigating through pages, to collect the desired data...")
    st.markdown('''Pandas: Use the powerful Pandas library to transform the dataset from CSV format into a structured dataframe.
                    Pandas helps data manipulation, cleaning, and preprocessing, ensuring that data was ready for analysis.''')
    st.markdown('''MySQL: With help of SQL to establish a connection to a SQL database, enabling seamless integration of the transformed dataset
                    and the data was efficiently inserted into relevant tables for storage and retrieval.''')
    st.markdown("Streamlit: Developed an interactive web application using Streamlit, a user-friendly framework for data visualization and analysis.")
    st.subheader(":blue[Skill-take:]")
    st.markdown("Selenium, Python, Pandas, MySQL,mysql-connector-python, Streamlit.")
    st.subheader(":blue[Developed-by:]  Mohammed Asik Hussain")
