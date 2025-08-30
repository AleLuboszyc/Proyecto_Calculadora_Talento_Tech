import pytest

@pytest.fixture
def enteros():
    return (10, 5)

@pytest.fixture
def flotantes():
    return (10.5, 2.5)