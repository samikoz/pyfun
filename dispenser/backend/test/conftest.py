import pytest

from notes import NotePLN
from dispenser import SingleCurrencyDispenser


@pytest.fixture()
def unlimited_dispenser():
    return SingleCurrencyDispenser({
        NotePLN(10): 10**5,
        NotePLN(20): 10**5,
        NotePLN(50): 10**5,
        NotePLN(100): 10**5
    })
