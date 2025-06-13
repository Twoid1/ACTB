from datetime import datetime

def get_session_multiplier():
utc_hour = datetime.utcnow().hour
if 0 <= utc_hour < 8: # Asian session
return 0.85
elif 8 <= utc_hour < 16: # European session
return 1.05
else: # US session (16-24)
return 1.25
