import pytz
from datetime import datetime, timedelta

class Datetime:
    def execute(self, text: str) -> str:
        try:
            date = datetime.strptime(text, "%a, %d %b %Y %H:%M:%S %z") + timedelta(hours=7)
            return date.strftime("%Y-%m-%dT%H:%M:%S");
        except Exception as e:
            return text;

    def now(self) -> str:
        tz = pytz.timezone("Asia/Jakarta")
        date = datetime.now(tz).strftime("%Y-%m-%dT%H:%M:%S")
        return date