import unittest
from datetime import datetime
from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

class TestEngine(unittest.TestCase):
    def run_engine_tests(self, engine, last_service_date, current_mileage, last_service_mileage, engine_should_be_serviced_expected):
        car = engine(last_service_date, current_mileage, last_service_mileage)
        self.assertEqual(car.needs_service(), engine_should_be_serviced_expected)

    def test_calliope(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        self.run_engine_tests(Calliope, last_service_date, current_mileage, last_service_mileage, True)
        last_service_date = today.replace(year=today.year - 1)
        self.run_engine_tests(Calliope, last_service_date, current_mileage, last_service_mileage, False)
        current_mileage = 30001
        self.run_engine_tests(Calliope, today, current_mileage, last_service_mileage, True)
        current_mileage = 30000
        self.run_engine_tests(Calliope, today, current_mileage, last_service_mileage, False)

    def test_glissade(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        self.run_engine_tests(Glissade, last_service_date, current_mileage, last_service_mileage, True)
        last_service_date = today.replace(year=today.year - 1)
        self.run_engine_tests(Glissade, last_service_date, current_mileage, last_service_mileage, False)
        current_mileage = 60001
        self.run_engine_tests(Glissade, today, current_mileage, last_service_mileage, True)
        current_mileage = 60000
        self.run_engine_tests(Glissade, today, current_mileage, last_service_mileage, False)

    def test_palindrome(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False

        self.run_engine_tests(Palindrome, last_service_date, warning_light_is_on, False)
        last_service_date = today.replace(year=today.year - 3)
        self.run_engine_tests(Palindrome, last_service_date, warning_light_is_on, False)
        self.run_engine_tests(Palindrome, today, True, True)
        self.run_engine_tests(Palindrome, today, False, False)

    def test_rorschach(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        self.run_engine_tests(Rorschach, last_service_date, current_mileage, last_service_mileage, True)
        last_service_date = today.replace(year=today.year - 3)
        self.run_engine_tests(Rorschach, last_service_date, current_mileage, last_service_mileage, False)
        current_mileage = 60001
        self.run_engine_tests(Rorschach, today, current_mileage, last_service_mileage, True)
        current_mileage = 60000
        self.run_engine_tests(Rorschach, today, current_mileage, last_service_mileage, False)

    def test_thovex(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        self.run_engine_tests(Thovex, last_service_date, current_mileage, last_service_mileage, True)
        last_service_date = today.replace(year=today.year - 3)
        self.run_engine_tests(Thovex, last_service_date, current_mileage, last_service_mileage, False)
        current_mileage = 30001
        self.run_engine_tests(Thovex, today, current_mileage, last_service_mileage, True)
        current_mileage = 30000
        self.run_engine_tests(Thovex, today, current_mileage, last_service_mileage, False)

if __name__ == '__main':
    unittest.main()
