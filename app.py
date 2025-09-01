import streamlit as st
import mysql.connector

@st.cache_resource

def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()


@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
    
rows = run_query("SELECT * from dataset_analisis;")

for row in rows:
    st.write("f{row[0]} has a :{row[1]}:")

