from car import Car

class WilloughbyEngine(Car):
    def __init__(self, last_service_date: str, current_mileage: int, last_service_mileage: int):
        super().__init__(last_service_date)
        self._current_mileage = current_mileage
        self._last_service_mileage = last_service_mileage

    @property
    def current_mileage(self) -> int:
        return self._current_mileage

    @property
    def last_service_mileage(self) -> int:
        return self._last_service_mileage

    def engine_should_be_serviced(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000
