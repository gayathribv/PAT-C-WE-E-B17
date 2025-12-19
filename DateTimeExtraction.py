# Create a lambda function to extract date and time from datetime object
from datetime import datetime
now=datetime.now()
yr = lambda x: x.year
mnth= lambda x:x.month
tme= lambda x:x.time()
print(f"The year of today's date is {yr(now)}, month is {mnth(now)} and time now is {tme(now)}")