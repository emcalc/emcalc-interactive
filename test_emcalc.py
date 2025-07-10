import scipy.constants as const
from random import randint
def grams_to_kg(grams):
    """Gram değerini kilograma çevirir."""
    return grams / 1000

def calculate_theoretical_energy(mass_kg):
    """Verilen kütlenin teorik E=mc^2 enerjisini hesaplar."""
    return mass_kg * const.c**2

def calculate_practical_energy(theoretical_energy, efficiency):
    """Teorik enerjiyi verimlilikle çarparak pratik enerjiyi bulur."""
    return theoretical_energy * efficiency

def convert_joules_to_electricity(practical_energy_joules, conversion_efficiency):
    """Pratik enerjinin ne kadarının elektriğe dönüştüğünü hesaplar."""
    return practical_energy_joules * conversion_efficiency

def calculate_led_on_time_seconds(electric_energy_joules, watt):
    """Elektrik enerjisiyle bir LED'in kaç saniye yanacağını hesaplar."""
    return electric_energy_joules / watt

def test_grams_to_kg():
    assert grams_to_kg(1000) == 1
    assert grams_to_kg(500) == 0.5
    assert grams_to_kg(0) == 0

def test_calculate_theoretical_energy():
    assert calculate_theoretical_energy(1) == const.c**2
    assert calculate_theoretical_energy(0) == 0

def test_calculate_practical_energy():
    assert calculate_practical_energy(100, 0.5) == 50
    assert calculate_practical_energy(200, 0.25) == 50

def test_convert_joules_to_electricity():
    assert convert_joules_to_electricity(100, 0.5) == 50
    assert convert_joules_to_electricity(200, 0.25) == 50

def test_calculate_led_on_time_seconds():
    assert calculate_led_on_time_seconds(100, 10) == 10
    assert calculate_led_on_time_seconds(50, 5) == 10
