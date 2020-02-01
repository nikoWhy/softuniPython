from datetime import datetime
from datetime import timedelta

date_string = input()

date_object = datetime.strptime(date_string, "%d-%m-%Y")
future_date = date_object + timedelta(days=999)
print(future_date.strftime('%d-%m-%Y'))