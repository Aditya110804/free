import streamlit as st

def show():
    st.title("🚗 Welcome to Smart Ride Pooling")

    st.markdown("""
        <h4 style='color:#444;'>Find or offer rides easily. Save time, money, and fuel.</h4>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔐 Login"):
            st.session_state.page = "login"
            st.rerun()

    with col2:
        if st.button("📝 Register"):
            st.session_state.page = "register_user"
            st.rerun()
