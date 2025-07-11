# logic.py (add at bottom)

def update_driver_route(username, new_route):
    """
    Update only route details for a driver identified by username.
    new_route should be a dict with keys: from, to, date, time.
    """
    drivers = load_drivers()
    updated = False
    for d in drivers:
        if d["username"] == username:
            # update only the route fields
            d["from"] = new_route["from"]
            d["to"]   = new_route["to"]
            d["date"] = new_route["date"]
            d["time"] = new_route["time"]
            updated = True
            break

    if updated:
        save_json(DRIVERS_FILE, drivers)
    return updated
