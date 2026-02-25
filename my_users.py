import dataiku
client = dataiku.api_client()

users = client.list_users()
    
rows = []
for u in users:
    profile = u.get("userProfile")
    login = u["login"]
    user_obj = client.get_user(login)
    activity = user_obj.get_activity().get_raw()
    rows.append({
        "login": login,
        "display_name": u["displayName"],
        "profile": profile,
        "last_successful_login": activity["lastSuccessfulLogin"],
        "last_failed_login": activity["lastFailedLogin"],
        "last_session_activity": activity["lastSessionActivity"]
    })
rows
