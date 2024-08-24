import pytest
import allure

@pytest.mark.smoke
def test_sub0():
    assert 2 - 2 == 0


@pytest.mark.regression
def test_sub1():
    assert 3 - 3 == 0

