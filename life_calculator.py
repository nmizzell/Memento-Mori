from datetime import datetime

age_at_death = 90

birthday = datetime(day=2,month=11,year=2001)
today = datetime.now()

time_alive = today - birthday
days_alive = time_alive.days
weeks_alive = int(days_alive/7)
weeks_left_to_live = (age_at_death*52)-weeks_alive


print("*"*weeks_alive+"-"*weeks_left_to_live)

print(f"you are {round(weeks_alive/(age_at_death*52)*100,2)}% through your life if you live to {age_at_death}")