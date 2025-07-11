import streamlit as st
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic import load_drivers, load_bookings, update_driver_route

def show():
    st.header("🚗 Driver Dashboard")
    username = st.session_state.get("username")

    # Load driver profile
    drivers = load_drivers()
    driver = next((d for d in drivers if d.get("username") == username), None)
    if not driver:
        st.error("something went wrong. Please try logging in again.")
        st.session_state.page = "login"
        st.rerun()
    return
    
    driver = next((d for d in drivers if d.get("username") == username),none)

    ## 1) Show static profile info
    st.subheader("👤 Your Profile")
    st.write(f"**Name:** {driver['name']}")
    st.write(f"**Contact:** {driver['contact']}")
    st.write(f"**Vehicle No:** {driver['vehicle_no']}")
    st.write(f"**License No:** {driver['license_no']}")

    st.markdown("---")

    ## 2) Ride details form
    st.subheader("🗺️ Update Your Next Ride")
    with st.form("ride_form"):
        from_loc = st.text_input("From", value=driver.get("from",""))
        to_loc   = st.text_input("To",   value=driver.get("to",""))
        date     = st.date_input("Date",  value=driver.get("date"))
        time     = st.time_input("Time",  value=st.session_state.get("time_obj",
                              # parse driver['time'] if needed
                              __import__('datetime').datetime.strptime(driver.get("time","00:00"), "%H:%M").time()
                         ))
        submitted = st.form_submit_button("Save Ride Details")

        if submitted:
            new_route = {
                "from": from_loc.strip(),
                "to":   to_loc.strip(),
                "date": str(date),
                "time": time.strftime("%H:%M")
            }
            if update_driver_route(username, new_route):
                st.success("Ride details updated!")
                st.session_state.time_obj = time  # persist for next form load
            else:
                st.error("Failed to update ride. Try again.")

    st.markdown("---")

    # Show bookings
    st.subheader("📋 Your Bookings")
    bookings = load_bookings()
    your = [b for b in bookings if b["driver"]["username"] == username]
    if your:
        for b in your:
            p = b["passenger"]
            st.markdown(f"""
                **Passenger:** {p['name']}  
                **Contact:** {p['contact']}  
                **Route:** {p['from']} → {p['to']}  
                **When:** {p['date']} at {p['time']}
                ---
            """)
    else:
        st.info("No bookings yet.")

  
