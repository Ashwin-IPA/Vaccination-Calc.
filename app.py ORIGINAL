import streamlit as st

def calculate_revenue(clients, base_vaccine=20, coadmin_extra=30):
    base_revenue = clients * base_vaccine
    coadmin_revenue = clients * (base_vaccine + coadmin_extra)
    return base_revenue, coadmin_revenue

st.title("💉 Vaccination Revenue Calculator")

clients = st.number_input("Enter the number of clients", min_value=1, step=1, value=10)
base_revenue, coadmin_revenue = calculate_revenue(clients)

st.metric(label="Base Vaccination Revenue ($20 each)", value=f"${base_revenue}")
st.metric(label="Co-administration Revenue ($50 each)", value=f"${coadmin_revenue}")

st.write("Use this tool to quickly estimate potential earnings from vaccinations!")
