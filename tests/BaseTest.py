import pytest


@pytest.mark.usefixtures("driver", "log_on_failure", "logs_for_tests")
class BaseTest:
    pass