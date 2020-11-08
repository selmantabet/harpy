import datetime
now = datetime.datetime.now()
 
print("now =", now)

two_weeks_from_now = now + datetime.timedelta(days=7)
print("2w = ", two_weeks_from_now)
stored_time = now.isoformat()
print(stored_time, " Stored.")
parsed_time = datetime.datetime.fromisoformat(stored_time)
print(type(parsed_time))
print(parsed_time, " Parsed")

print((two_weeks_from_now - parsed_time).days)