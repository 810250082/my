# from datetime import datetime , timedelta , timezone
from datetime import datetime, timedelta, timezone
str = '2015-1-21 9:01:30'
date = datetime.strptime(str , '%Y-%m-%d %H:%M:%S')
tz = timezone(timedelta(hours=5))
dt = date.replace(tzinfo=tz)
stamp = dt.timestamp()
print(stamp)
