import dataiku
client = dataiku.api_client()

users = client.list_users()
    
rows = []
index = 10
for u in users:
    login = u["login"]
    user_obj = client.get_user(login)
    activity = user_obj.get_activity().get_raw()
    rows.append({
        "index": index
        "login": login,
        "display_name": u["displayName"],
        "last_successful_login": activity["lastSuccessfulLogin"],
        "last_failed_login": activity["lastFailedLogin"],
        "last_session_activity": activity["lastSessionActivity"]
    })
    index = index + 1
rows
