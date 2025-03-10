import streamlit as st
import pandas as pd
import urllib.parse

# Title with Emoji
st.title("💉 Vaccination Potential Earnings Calculator")

# Default vaccine pricing
vaccine_prices = {
    "Influenza": 19.32,
    "COVID-19": 27.35,
    "COVID-19 (site visit)": 122.4,
    "Pneumococcal": 19.32,
    "Respiratory Syncytial Virus (RSV)": 19.32,
    "Measles, mumps, rubella": 19.32,
    "Diphtheria, tetanus, pertussis": 19.32,
    "Shingles": 19.32,
    "Hepatitis A": 19.32,
    "Hepatitis B": 19.32,
    "Typhoid": 19.32,
    "Human papillomavirus": 19.32,
    "Japanese encephalitis": 19.32,
    "Meningococcal ACWY": 19.32,
    "Meningococcal B": 19.32,
    "Meningococcal C": 19.32,
    "Mpox (Monkeypox)": 19.32,
    "Poliomyelitis": 19.32,
    "Varicella": 19.32,
    "Rabies": 19.32
}

# User input: Editable vaccine pricing
st.sidebar.header("🎯 Customize Vaccine Pricing")
custom_prices = {}
for vaccine, price in vaccine_prices.items():
    custom_prices[vaccine] = st.sidebar.number_input(f"{vaccine} Price ($)", value=price, min_value=0.0)

# Main vaccine selection
st.header("1️⃣ Choose Your Main Vaccine")
main_vaccine = st.selectbox("Select a main vaccine:", list(vaccine_prices.keys()))

# Optional co-administration vaccine
st.header("2️⃣ Optional Co-administration Vaccine")
coadmin_vaccine = st.selectbox("Select a secondary vaccine (optional):", ["None"] + list(vaccine_prices.keys()))

# Campaign cost
include_campaign_cost = st.checkbox("📢 Include program cost")
campaign_cost = st.number_input("Program Cost ($)", min_value=0.0, value=0.0 if not include_campaign_cost else 100.0)

# Set targets
target_vaccinations = st.number_input("🎯 Target Number of Vaccinations", min_value=0, value=100)

# Basket size (optional)
include_basket_size = st.checkbox("🛒 Include basket size")
basket_size = st.number_input("Basket Size ($ per patient)", min_value=0.0, value=10.0) if include_basket_size else 0.0

# Calculation of potential earnings
def calculate_potential_earnings():
    main_vaccine_price = custom_prices.get(main_vaccine, 0)
    coadmin_vaccine_price = custom_prices.get(coadmin_vaccine, 0) if coadmin_vaccine != "None" else 0
    total_earnings = (main_vaccine_price + coadmin_vaccine_price) * target_vaccinations + campaign_cost + (basket_size * target_vaccinations)
    return total_earnings

total_earnings = calculate_potential_earnings()
st.subheader(f"💰 Estimated Potential Earnings: **${total_earnings:,.2f}**")

# Mailto link generation
recipient_email = st.text_input("📧 Enter recipient email:")
if st.button("🚀 Generate Report"):
    subject = "Vaccination Earnings Report"
    body = f"""
Vaccination Earnings Report:

Main Vaccine: {main_vaccine}
Secondary Vaccine: {coadmin_vaccine if coadmin_vaccine != 'None' else 'N/A'}
Target Vaccinations: {target_vaccinations}
Program Cost: ${campaign_cost:,.2f}
Basket Size: ${basket_size:,.2f if include_basket_size else 'N/A'}

Estimated Potential Earnings: ${total_earnings:,.2f}
"""
    mailto_link = f"mailto:{recipient_email}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
    st.markdown(f"[📨 Click here to send email]({mailto_link})")

# Financial disclaimer
st.markdown("""⚠️ **Financial Disclaimer:** This is an estimation tool and does not guarantee actual earnings. Prices and costs should be verified before implementation.""")
