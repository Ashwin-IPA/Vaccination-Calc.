import streamlit as st
import pandas as pd
import plotly.express as px

# Function to calculate campaign ROI
def calculate_roi(campaign_type, campaign_cost, expected_patients, avg_spend_per_patient, retention_rate, sms_boost, digital_boost):
    expected_revenue = expected_patients * avg_spend_per_patient
    break_even_patients = campaign_cost / avg_spend_per_patient
    repeat_customers = expected_patients * (retention_rate / 100)
    sms_addon_revenue = expected_patients * sms_boost
    digital_addon_revenue = expected_patients * digital_boost
    total_revenue = expected_revenue + sms_addon_revenue + digital_addon_revenue
    roi = ((total_revenue - campaign_cost) / campaign_cost) * 100
    
    return {
        "Campaign Type": campaign_type,
        "Campaign Cost ($)": campaign_cost,
        "Expected Patients": expected_patients,
        "Expected Revenue ($)": expected_revenue,
        "Break-Even Patients Needed": break_even_patients,
        "Retention Rate (%)": retention_rate,
        "Repeat Customers": repeat_customers,
        "SMS Add-On Revenue Boost ($)": sms_addon_revenue,
        "Digital Add-On Revenue Boost ($)": digital_addon_revenue,
        "Total Revenue ($)": total_revenue,
        "ROI (%)": roi
    }

# Streamlit App
st.set_page_config(page_title="Pharmacy Campaign ROI Calculator", layout="wide")
st.title("🚀 Pharmacy Campaign ROI & Performance Calculator")
st.subheader("Maximize Your Campaign Success with Data-Driven Insights")

st.markdown("""
💡 **Why Use This Calculator?**
- Get an instant estimate of your campaign's potential revenue 📈
- See how quickly you'll break even 💰
- Understand the impact of SMS and Digital Ad add-ons ✉️📊
- Compare different campaigns to choose the best fit for your pharmacy 🏥
""")

# User Inputs
st.sidebar.header("📊 Campaign Inputs")
campaign_type = st.sidebar.selectbox("Select Campaign Type", ["Vaccination", "Pain Management", "Mental Health", "Travel Health"])
campaign_cost = st.sidebar.number_input("Campaign Cost ($)", min_value=100, value=500)
expected_patients = st.sidebar.number_input("Expected Patients", min_value=1, value=200)
avg_spend_per_patient = st.sidebar.number_input("Average Spend per Patient ($)", min_value=1, value=40)
retention_rate = st.sidebar.slider("Retention Rate (%)", min_value=0, max_value=100, value=30)
sms_boost = st.sidebar.number_input("SMS Revenue Boost per Patient ($)", min_value=0, value=2)
digital_boost = st.sidebar.number_input("Digital Ad Revenue Boost per Patient ($)", min_value=0, value=3)

if st.sidebar.button("🚀 Calculate ROI"):
    result = calculate_roi(campaign_type, campaign_cost, expected_patients, avg_spend_per_patient, retention_rate, sms_boost, digital_boost)
    df = pd.DataFrame([result])
    
    st.success("✅ Calculation Complete! Here are your results:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="💰 Total Revenue ($)", value=f"${result['Total Revenue ($)']:.2f}")
        st.metric(label="🔄 Retained Customers", value=f"{result['Repeat Customers']:.0f}")
    with col2:
        st.metric(label="📈 ROI (%)", value=f"{result['ROI (%)']:.2f}%")
        st.metric(label="🔢 Break-Even Patients", value=f"{result['Break-Even Patients Needed']:.0f}")
    
    # Visualizations
    fig = px.bar(df.melt(id_vars=["Campaign Type"], value_vars=["Expected Revenue ($)", "Total Revenue ($)"]), 
                 x="Campaign Type", y="value", color="variable", 
                 title="📊 Revenue Breakdown", text_auto=True)
    st.plotly_chart(fig, use_container_width=True)
    
    st.dataframe(df.style.format({
        "Campaign Cost ($)": "${:,.2f}",
        "Expected Revenue ($)": "${:,.2f}",
        "Break-Even Patients Needed": "{:.0f}",
        "Retention Rate (%)": "{:.1f}%",
        "Repeat Customers": "{:.0f}",
        "SMS Add-On Revenue Boost ($)": "${:,.2f}",
        "Digital Add-On Revenue Boost ($)": "${:,.2f}",
        "Total Revenue ($)": "${:,.2f}",
        "ROI (%)": "{:.2f}%"
    }))
    
st.markdown("---")
st.markdown("💡 **Next Steps**: Use these insights to optimize your campaign strategy and increase pharmacy sign-ups!")
