user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
#this line optimize the execution time}
    return {key:value for key, value in user_pref.items() if value is not None}
#    updated_preferencs = {}
#    for key,value in user_pref.items():
#        if value is not None:
#            updated_preferencs[key] = value
#    return updated_preferencs


print(update_preferences(user_preferences))
