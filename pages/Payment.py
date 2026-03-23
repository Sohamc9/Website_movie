import streamlit as st

st.title("💳 Payment Page")

movie = st.session_state.get("selected_movie","")
plan = st.session_state.get("selected_plan", "")    

st.write(f"You have selected: **{movie}**")
st.write(f"Your chosen plan: **{plan}**")

if st.button("Pay Now"):
    st.session_state.payment_status = "Success"
    st.subheader("Payment Successful! 🎉")
    st.write("Thank you for your purchase. Enjoy your movie!")
