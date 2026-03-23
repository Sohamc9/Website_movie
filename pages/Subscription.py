import streamlit as st

st.title("Subscription Page")

movie = st.session_state.get("selected_movie", "No movie selected")

st.write(f"You have selected: **{movie}**")

plan = st.radio("Choose a plan",
                ["Basic - ₹100", "Premium - ₹200", "VIP - ₹300"])


if st.button("Proceed to Payment"):
    st.session_state.selected_plan = plan
    st.switch_page("pages/payment.py")