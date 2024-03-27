from datetime import datetime
import time


datetime_unixtime = datetime.now().timestamp()
time_unixtime = time.time()
timezone_aware_unixtime = datetime.now().astimezone().timestamp()

print(
    f"""
{datetime_unixtime       = }
{time_unixtime           = }
{timezone_aware_unixtime = }
"""
)
