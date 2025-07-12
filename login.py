import streamlit as st
import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auth import validate_credentials

def show():
    st.header("🔐 Login")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            user = validate_credentials(username.strip(), password.strip())
            if user:
                st.success(f"Welcome, {username}!")

                st.session_state.username = username.strip()
                st.session_state.role = user["role"]
                st.session_state.logged_in = True

                if user["role"] == "driver":
                    st.session_state.page = "driver_route_selection"
                else:
                    st.session_state.page = "route_selection"
                st.rerun()
            else:
                st.error("Invalid credentials.")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📝 New user? Register"):
            st.session_state.page = "register_user"
            st.rerun()
    with col2:
        if st.button("🏠 Back to Home"):
            st.session_state.page = "home"
            st.rerun()
