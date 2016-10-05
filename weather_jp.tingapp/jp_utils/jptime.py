from pytz import timezone
from datetime import datetime

def now():
    return datetime.now(timezone('UTC')).astimezone(timezone('Asia/Tokyo'))