import streamlit as st
from sqlalchemy import text


# bikin koneksi
conn = st.connection("mysql", type="sql")

# bikin tabel contoh kalau belum ada



# tampilkan data
rows = conn.query("SELECT * FROM dataset_analisis;", ttl=0)
st.dataframe(rows)

conn.session.commit()