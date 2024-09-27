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

kerala=[]
bus_type_kerala=[]
df_kearala=pd.read_csv("F:\df_kerala.csv")
for i,r in df_kearala.iterrows():  #traverse through each row
    kerala.append(r['Route_name'])  
    bus_type_kerala.append(r['Bus_type']) 
Kerala =list(set(kerala))
Type_kerala =list(set(bus_type_kerala))

telangana=[]
bus_type_telangana=[]
df_telangana=pd.read_csv("F:\df_telangana.csv")
for i,r in df_telangana.iterrows():  #traverse through each row
    telangana.append(r['Route_name']) 
    bus_type_telangana.append(r['Bus_type']) 
Telangana =list(set(telangana))
Type_telangana =list(set(bus_type_telangana))

kadamba=[]
bus_type_kadamba=[]
df_kadamba=pd.read_csv("F:\df_kadamba.csv")
for i,r in df_kadamba.iterrows():  #traverse through each row
    kadamba.append(r['Route_name']) 
    bus_type_kadamba.append(r['Bus_type']) 
Kadamba =list(set(kadamba))
Type_kadamba =list(set(bus_type_kadamba))

rajasthan=[]
bus_type_rajasthan=[]
df_rajasthan=pd.read_csv("F:\df_rajasthan.csv")
for i,r in df_rajasthan.iterrows():  #traverse through each row
    rajasthan.append(r['Route_name']) 
    bus_type_rajasthan.append(r['Bus_type']) 
Rajasthan =list(set(rajasthan))
Type_rajasthan =list(set(bus_type_rajasthan))

northbengal=[]
bus_type_northbengal=[]
df_northbengal=pd.read_csv("F:\df_northbengal.csv")
for i,r in df_northbengal.iterrows():  #traverse through each row
    northbengal.append(r['Route_name']) 
    bus_type_northbengal.append(r['Bus_type']) 
NorthBengal =list(set(northbengal))
Type_northbengal =list(set(bus_type_northbengal))

westbengal=[]
bus_type_westbengal=[]
df_westbengal=pd.read_csv("F:\df_westbengal.csv")
for i,r in df_westbengal.iterrows():  #traverse through each row
    westbengal.append(r['Route_name']) 
    bus_type_westbengal.append(r['Bus_type']) 
WestBengal =list(set(westbengal))
Type_westbengal =list(set(bus_type_westbengal))

assam=[]
bus_type_assam=[]
df_assam=pd.read_csv("F:\df_Assam.csv")
for i,r in df_assam.iterrows():  #traverse through each row
    assam.append(r['Route_name']) 
    bus_type_assam.append(r['Bus_type']) 
Assam =list(set(assam))
Type_assam =list(set(bus_type_assam))

punjab=[]
bus_type_punjab=[]
df_punjab=pd.read_csv("F:\df_punjab.csv")
for i,r in df_punjab.iterrows():  #traverse through each row
    punjab.append(r['Route_name']) 
    bus_type_punjab.append(r['Bus_type']) 
Punjab =list(set(punjab))
Type_punjab =list(set(bus_type_punjab))

bihar=[]
bus_type_bihar=[]
df_bihar=pd.read_csv("F:\df_bihar.csv")
for i,r in df_bihar.iterrows():  #traverse through each row
    bihar.append(r['Route_name']) 
    bus_type_bihar.append(r['Bus_type']) 
Bihar =list(set(bihar))
Type_bihar =list(set(bus_type_bihar))

chandigarh=[]
bus_type_chandigarh=[]
df_chandigarh=pd.read_csv("F:\df_chandigarh.csv")
for i,r in df_chandigarh.iterrows():  #traverse through each row
    chandigarh.append(r['Route_name']) 
    bus_type_chandigarh.append(r['Bus_type']) 
Chandigarh =list(set(chandigarh))
Type_chandigarh =list(set(bus_type_chandigarh))


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
    state = st.sidebar.selectbox('🗺️State',['Kerala','Telangana','Kadamba','Rajasthan','NorthBengal',
                                 'WestBengal','Assam','Punjab','Bihar','Chandigarh'])
    col1, col2 = st.columns(2)
    with col1 :
        if state == 'Kerala':
            route = st.selectbox('📍Select Route',Kerala,index=0)
            type = st.selectbox('🚍 Bus Type',Type_kerala,index=0)
        elif state == 'Telangana':
            route = st.selectbox('📍Select Route',Telangana,index=0)
            type = st.selectbox('🚍 Bus Type',Type_telangana,index=0)
        elif state == 'Kadamba':
            route = st.selectbox('📍Select Route',Kadamba,index=0)
            type = st.selectbox('🚍 Bus Type',Type_kadamba,index=0)
        elif state == 'Rajasthan':
            route = st.selectbox('📍Select Route',Rajasthan,index=0)
            type = st.selectbox('🚍 Bus Type',Type_rajasthan,index=0)
        elif state == 'NorthBengal':
            route = st.selectbox('📍Select Route',NorthBengal,index=0)
            type = st.selectbox('🚍 Bus Type',Type_northbengal,index=0)
        elif state == 'WestBengal':
            route = st.selectbox('📍Select Route',WestBengal,index=0)
            type = st.selectbox('🚍 Bus Type',Type_westbengal,index=0)
        elif state == 'Assam':
            route = st.selectbox('📍Select Route',Assam,index=0)
            type = st.selectbox('🚍 Bus Type',Type_assam,index=0)
        elif state == 'Punjab':
            route = st.selectbox('📍Select Route',Punjab,index=0)
            type = st.selectbox('🚍 Bus Type',Type_punjab,index=0)
        elif state == 'Bihar':
            route = st.selectbox('📍Select Route',Bihar,index=0)
            type = st.selectbox('🚍 Bus Type',Type_bihar,index=0)
        elif state == 'Chandigarh':
            route = st.selectbox('📍Select Route',Chandigarh,index=0)
            type = st.selectbox('🚍 Bus Type',Type_chandigarh,index=0)

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
                "Seats_Available","Ratings","Route_name","Route_link"
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
