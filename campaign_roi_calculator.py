import streamlit as st
import pandas as pd

# Function to calculate campaign ROI
def calculate_roi(campaign_cost, expected_patients, avg_spend_per_patient, retention_rate):
    expected_revenue = expected_patients * avg_spend_per_patient
    break_even_patients = campaign_cost / avg_spend_per_patient
    repeat_customers = expected_patients * (retention_rate / 100)
    roi = ((expected_revenue - campaign_cost) / campaign_cost) * 100
    
    return expected_revenue, break_even_patients, repeat_customers, roi

# Function to calculate co-administration impact
def calculate_coadmin_break_even(campaign_cost, avg_spend_per_patient, coadmin_vax_fee):
    break_even_without_avg_spend = campaign_cost / coadmin_vax_fee
    break_even_with_avg_spend = campaign_cost / (coadmin_vax_fee + avg_spend_per_patient)
    return break_even_without_avg_spend, break_even_with_avg_spend

# Streamlit App
st.set_page_config(page_title="Pharmacy Campaign ROI Calculator", layout="wide")
st.title("🚀 Pharmacy Campaign ROI Calculator")

# User Inputs
st.sidebar.header("📊 Campaign Inputs")
campaign_cost = st.sidebar.number_input("Campaign Cost ($)", min_value=100, value=500)
expected_patients = st.sidebar.number_input("Expected Patients", min_value=1, value=200)
avg_spend_per_patient = st.sidebar.number_input("Average Spend per Patient ($)", min_value=1, value=40)
retention_rate = st.sidebar.slider("Retention Rate (%)", min_value=0, max_value=100, value=30)

# Dropdown for co-administration vaccinations
st.sidebar.header("💉 Co-Administration Vaccinations")
coadmin_vax_type = st.sidebar.selectbox("Select Vaccine Type", ["Flu", "COVID-19", "Shingles", "Pneumococcal", "None"])
coadmin_vax_fee = st.sidebar.number_input("Co-Administration Fee per Patient ($)", min_value=0, value=20)

if st.sidebar.button("🚀 Calculate ROI"):
    expected_revenue, break_even_patients, repeat_customers, roi = calculate_roi(
        campaign_cost, expected_patients, avg_spend_per_patient, retention_rate
    )
    
    break_even_without_avg_spend, break_even_with_avg_spend = calculate_coadmin_break_even(
        campaign_cost, avg_spend_per_patient, coadmin_vax_fee
    )
    
    st.success("✅ Calculation Complete!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="💰 Expected Revenue ($)", value=f"${expected_revenue:,.2f}")
        st.metric(label="🔄 Retained Customers", value=f"{repeat_customers:.0f}")
    with col2:
        st.metric(label="📈 ROI (%)", value=f"{roi:.2f}%")
        st.metric(label="🔢 Break-Even Patients", value=f"{break_even_patients:.0f}")
    
    # Display results as a DataFrame
    df = pd.DataFrame({
        "Metric": [
            "Expected Revenue ($)", "Break-Even Patients Needed",
            "Break-Even Patients with Co-Admin Only", "Break-Even Patients with Co-Admin & Avg Spend",
            "Retained Customers", "ROI (%)"
        ],
        "Value": [
            expected_revenue, break_even_patients,
            break_even_without_avg_spend, break_even_with_avg_spend,
            repeat_customers, roi
        ]
    })
    st.table(df)

