import streamlit as st

# Vaccine prices in AUD
vaccine_prices = {
    'Influenza': 25,
    'COVID-19': 0,
    'DTPa (Diphtheria, Tetanus, Pertussis)': 43,
    'Pneumococcal': 120,
    'RSV': 350
}

# Streamlit UI setup
st.set_page_config(page_title="Vaccine Add-on Calculator", page_icon="💉", layout="centered")
st.title("Vaccine Add-on Revenue Calculator")
st.write("Select the base vaccine, any additional co-administered vaccines, and the number of people receiving vaccinations to calculate potential revenue.")

# User inputs
base_vaccine = st.selectbox("Select Base Vaccine:", list(vaccine_prices.keys()))
co_vaccine = st.selectbox("Select Co-Administered Vaccine (Optional):", ["None"] + list(vaccine_prices.keys()))
num_people = st.number_input("Number of People:", min_value=1, value=1, step=1)

# Calculation logic
base_cost = vaccine_prices[base_vaccine] * num_people
co_cost = vaccine_prices[co_vaccine] * num_people if co_vaccine != "None" else 0
total_cost = base_cost + co_cost
addon_revenue = co_cost

# Display results
st.markdown("### Calculation Results")
st.write(f"**Total Cost:** ${total_cost:.2f} AUD")
st.write(f"**Revenue from Add-ons:** ${addon_revenue:.2f} AUD")

# Aesthetic enhancements
st.markdown("---")
st.info("💡 Tip: Offering co-administered vaccines increases revenue while providing added protection for patients.")
