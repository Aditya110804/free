import streamlit as st
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from logic import load_bookings

def show():
    st.header("📋 Driver Dashboard")

    username = st.session_state.get("username")
    if not username:
        st.warning("Please log in.")
        st.session_state.page = "login"
        st.rerun()
        return

    bookings = load_bookings()
    my_bookings = [b for b in bookings if b["driver"].get("username") == username]

    if not my_bookings:
        st.info("No passenger bookings yet.")
        return

    st.success(f"You have {len(my_bookings)} booking(s):")

    for idx, booking in enumerate(my_bookings):
        passenger = booking["passenger"]
        st.markdown(f"""
        ---
        **Booking {idx+1}**
        - 👤 Passenger: `{passenger['username']}`
        - 🗺️ Route: `{passenger['from']} → {passenger['to']}`
        - 📅 Date: `{passenger['date']}`
        - ⏰ Time: `{passenger['time']}`
        """)
