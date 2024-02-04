user_preferences = {
    "language": "English",
    "font_size": "14px",
    "timezone": "GMT",
    "currency": "USD",
    "enable_location": False,
    "volume_level": 80,
    "date_format": "MM/DD/YYYY"
}

user_preferences["language"] = "Spanish" #overwride the value
user_preferences["volume_level"] = 50
user_preferences["highlight_color"] = "yellow" #add new value

#to delete a value without retrive the item
del user_preferences["currency"]

#to delete a value retriving the item
#"N/A" prevent an error if the key doesn't exist in the dictionary
removed_item = user_preferences.pop("date_format","N/A") 

print(user_preferences)