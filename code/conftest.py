import pytest


class Settings:
    URL: str = 'https://jsonplaceholder.typicode.com/'


@pytest.fixture(scope='function')
def config() -> Settings:
    settings = Settings()
    return settings
