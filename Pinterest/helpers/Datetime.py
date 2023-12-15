import pytz
from datetime import datetime, timedelta

class Datetime:
    def __init__(self) -> None:
        self.__format = "%Y-%m-%dT%H:%M:%S"
    def execute(self, text: str) -> str:
        try:
            return (datetime.strptime(text, "%a, %d %b %Y %H:%M:%S %z") + timedelta(hours=7)).strftime(self.__format)
    
        except Exception as e:
            return text;

    def now(self) -> str:
        tz = pytz.timezone("Asia/Jakarta")
        date = datetime.now(tz).strftime(self.__format)
        return date