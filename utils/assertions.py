from src.base.BrowserSetup import logger


class Assertions:
    """Class contains all assertions with log messages"""

    def __init__(self, driver):
        self.driver = driver

    def assert_equal(self, expected_value, actual_value):
        assert (str(expected_value).upper()) == (str(actual_value).upper()),\
            f"{expected_value} is not equal to {actual_value}"
        logger.info(f"Expected value and actual value are equal")

    def assert_contains(self, expected_value, actual_value):
        assert str(expected_value).upper().__contains__(str(actual_value).upper()),\
            f"{expected_value} is not equal to {actual_value}"
        logger.info(f"Expected value Contains actual value")

    def assert_not_equal(self, expected_value, actual_value):
        assert (str(expected_value).upper()) != (str(actual_value).upper()),\
            f"{expected_value} is not equal to {actual_value}"
        logger.info(f"Expected value and actual value not are equal")
