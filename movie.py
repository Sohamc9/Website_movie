import streamlit as st
import pandas as pd 

st.title("YuHas movies")
st.header("Welcome to HomePage")
st.subheader("This is a website to showcase different Movies")
st.write("\n")
st.write("\n")


genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Sci-fi :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == ":rainbow[Comedy]":
    col1, col2 = st.columns(2)

    col1.subheader("The Mask")
    col1.image("artifacts/images2/The Mask.jpg")
    col1.write("📅 Release Date: 1994")
    col1.write("🎬 Director: Chuck Russell")
    col1.write("⭐ Rating: 7.0/10") 
    col1.button("❤️ Like", key="mask_like")
    
    col2.subheader("The Hangover")
    col2.image("artifacts/images2/The hangover.jpg")
    col2.write("📅 Release Date: 2009")
    col2.write("🎬 Director: Todd Phillips")
    col2.write("⭐ Rating: 7.7/10")
    col2.button("❤️ Like", key="hangover_like")

    movies_to_rent = st.selectbox("🎬 Select a movie to rent",
 ["None", "The mask", "The Hangover",])

elif genre == "***Drama***":
    col1, col2 = st.columns(2)

    col1.subheader("The Godfather")
    col1.image("artifacts/images2/The Godfather.jpg")
    col1.write("📅 Release Date: 1972")
    col1.write("🎬 Director: Francis Ford Coppola")
    col1.write("⭐ Rating: 9.2/10")
    col1.button("❤️ Like", key="godfather_like")

    col2.subheader("Casablanca")
    col2.image("artifacts/images2/Casablanca.jpg")
    col2.write("📅 Release Date: 1942")
    col2.write("🎬 Director: Michael Curtiz")
    col2.write("⭐ Rating: 8.5/10")
    col2.button("❤️ Like", key="casablanca_like")

    movies_to_rent = st.selectbox("🎬 Select a movie to rent",
 ["None","The Godfather", "Casablanca"])

elif genre == "Sci-fi :movie_camera:":
    col1, col2 = st.columns(2)
    
    col1.subheader("Interstellar")
    col1.image("artifacts/images2/interstellar.jpg")
    col1.write("📅 Release Date: 2014")
    col1.write("🎬 Director: Christopher Nolan")
    col1.write("⭐ Rating: 8.6/10")
    col1.button("❤️ Like", key="interstellar_like")

    col2.subheader("Inception")
    col2.image("artifacts/images2/Inception.jpg")
    col2.write("📅 Release Date: 2010")
    col2.write("🎬 Director: Christopher Nolan")
    col2.write("⭐ Rating: 8.8/10")
    col2.button("❤️ Like", key="inception_like")

    movies_to_rent = st.selectbox("🎬 Select a movie to rent",
 ["None", "Interstellar", "Inception"])



if st.button("Rent Movie"):
    if movies_to_rent != "None":
        st.session_state.selected_movie = movies_to_rent
        st.switch_page("pages/subscription.py")
    else:
        st.warning("Please select a movie to rent.")

