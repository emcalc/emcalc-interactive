from lib_Grams_to_KG import grams_to_kg as g2kg

c = 299792458 

def easter_egg():
    """Easter egg function."""
    print("\nEaster Egg:\nIt is the e=mc2 calculator, not pi calculator.")
    print("If you want to calculate pi, use the 'pi' command in Python.\nOr use the 'math' module: import math\nprint(math.pi)\n")
    print("\n THANKS FOR USING EMCALC!")
    print("Createors and Supporters:\n 1. eymndev 2. tarik celik 3. Gemini 4. ChatGPT and You :) \n")

    input("\nfor exit the program click the Enter")
    exit()

def grams_to_kg(grams):
    """Grams to Kilogram."""
    return g2kg(grams)

def calculate_theoretical_energy(mass_kg):
    """calculating E=mc2 (%100 efficieny)."""
    return mass_kg * c**2

def calculate_practical_energy(theoretical_energy, efficiency):
    """calculating pratical energy."""
    return theoretical_energy * efficiency

def convert_joules_to_electricity(practical_energy_joules, conversion_efficiency):
    """calculating joules to watt energy."""
    return practical_energy_joules * conversion_efficiency

def calculate_led_on_time_seconds(electric_energy_joules, watt):
    """calculating watt to seconds."""
    return electric_energy_joules / watt

def test_grams_to_kg():
    assert grams_to_kg(1000) == 1 # kilograms
    assert grams_to_kg(543) == 0.543 # kilograms
    assert grams_to_kg(3.142) == 0.003142 # kilograms
    assert grams_to_kg(0) == 0 #kilograms

def test_calculate_theoretical_energy():
    assert calculate_theoretical_energy(1) == c**2
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
