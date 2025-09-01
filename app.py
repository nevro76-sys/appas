import streamlit as st

# Initialize connection.
conn = st.connection('mysql', type='sql')

# Perform query.
df = conn.query('SELECT * from dataset_analisis;', ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.id_dataset} has a :{row.text}:")