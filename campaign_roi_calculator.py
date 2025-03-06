import streamlit as st
import pandas as pd

# Predefined vaccine fees
vaccine_fees = {
    "Flu ($22)": 22,
    "COVID-19 (Free)": 0,
    "Shingles ($251)": 251,
    "Pneumococcal ($180)": 180,
    "None": 0
}

# Function to calculate campaign ROI
def calculate_roi(campaign_cost, expected_patients, avg_spend_per_patient, retention_rate):
    expected_revenue = expected_patients * avg_spend_per_patient
    break_even_patients = campaign_cost / avg_spend_per_patient
    repeat_customers = expected_patients * (retention_rate / 100)
    roi = ((expected_revenue - campaign_cost) / campaign_cost) * 100
    
    return round(expected_revenue, 2), round(break_even_patients, 2), round(repeat_customers, 2), round(roi, 2)

# Function to calculate co-administration impact
def calculate_coadmin_break_even(campaign_cost, avg_spend_per_patient, primary_vax_fee, secondary_vax_fee):
    break_even_primary_only = campaign_cost / primary_vax_fee if primary_vax_fee > 0 else 0
    break_even_secondary_only = campaign_cost / secondary_vax_fee if secondary_vax_fee > 0 else 0
    break_even_combined = campaign_cost / (primary_vax_fee + secondary_vax_fee) if (primary_vax_fee + secondary_vax_fee) > 0 else 0
    break_even_with_avg_spend = campaign_cost / (primary_vax_fee + secondary_vax_fee + avg_spend_per_patient) if (primary_vax_fee + secondary_vax_fee + avg_spend_per_patient) > 0 else 0
    return round(break_even_primary_only, 2), round(break_even_secondary_only, 2), round(break_even_combined, 2), round(break_even_with_avg_spend, 2)

# Streamlit App
st.set_page_config(page_title="Pharmacy Campaign ROI Calculator", layout="wide")
st.title("🚀 Pharmacy Campaign ROI Calculator")

# User Inputs
st.sidebar.header("📊 Campaign Inputs")
campaign_cost = st.sidebar.number_input("Campaign Cost ($)", min_value=100, value=500)
expected_patients = st.sidebar.number_input("Expected Patients", min_value=1, value=200)
avg_spend_per_patient = st.sidebar.number_input("Average Spend per Patient ($)", min_value=1, value=40)
retention_rate = st.sidebar.slider("Retention Rate (%)", min_value=0, max_value=100, value=30)

# Dropdowns for primary and secondary vaccinations with automatic fee selection
st.sidebar.header("💉 Co-Administration Vaccinations")
primary_vax_type = st.sidebar.selectbox("Select Primary Vaccine", list(vaccine_fees.keys()))
primary_vax_fee = vaccine_fees[primary_vax_type]

secondary_vax_type = st.sidebar.selectbox("Select Secondary Vaccine", list(vaccine_fees.keys()))
secondary_vax_fee = vaccine_fees[secondary_vax_type]

if st.sidebar.button("🚀 Calculate ROI"):
    expected_revenue, break_even_patients, repeat_customers, roi = calculate_roi(
        campaign_cost, expected_patients, avg_spend_per_patient, retention_rate
    )
    
    break_even_primary_only, break_even_secondary_only, break_even_combined, break_even_with_avg_spend = calculate_coadmin_break_even(
        campaign_cost, avg_spend_per_patient, primary_vax_fee, secondary_vax_fee
    )
    
    st.success("✅ Calculation Complete!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="💰 Expected Revenue ($)", value=f"${expected_revenue:,.2f}")
        st.metric(label="🔄 Retained Customers", value=f"{repeat_customers:.2f}")
    with col2:
        st.metric(label="📈 ROI (%)", value=f"{roi:.2f}%")
        st.metric(label="🔢 Break-Even Patients", value=f"{break_even_patients:.2f}")
    
    # Display results as a DataFrame
    df = pd.DataFrame({
        "Metric": [
            "Expected Revenue ($)", "Break-Even Patients Needed",
            f"Break-Even Patients with {primary_vax_type} Only", 
            f"Break-Even Patients with {secondary_vax_type} Only" if secondary_vax_type != "None" else "Break-Even Patients with Secondary Vaccine Only",
            "Break-Even Patients with Both Vaccines",
            "Break-Even Patients with Both Vaccines & Avg Spend",
            "Retained Customers", "ROI (%)"
        ],
        "Value": [
            expected_revenue, break_even_patients,
            break_even_primary_only,
            break_even_secondary_only if secondary_vax_type != "None" else "N/A",
            break_even_combined,
            break_even_with_avg_spend,
            repeat_customers, roi
        ]
    })
    st.table(df)

