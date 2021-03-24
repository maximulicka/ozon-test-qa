import pytest
from conftest import Settings


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config: Settings):
        self.config = config
