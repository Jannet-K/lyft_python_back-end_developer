from engine.sternman_engine import SternmanEngine
from datetime import datetime

class Palindrome(SternmanEngine):
    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < datetime.today().date() or self.engine_should_be_serviced()
