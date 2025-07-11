import scipy.constants as const

def grams_to_kg(grams):
    """Grams to Kilogram."""
    return grams / 1000

def calculate_theoretical_energy(mass_kg):
    """calculating E=mc2 (%100 efficieny)."""
    return mass_kg * const.c**2

def calculate_practical_energy(theoretical_energy, efficiency):
    """calculating pratical energy."""
    return theoretical_energy * efficiency

def convert_joules_to_electricity(practical_energy_joules, conversion_efficiency):
    """calculating joules to watt energy."""
    return practical_energy_joules * conversion_efficiency

def calculate_led_on_time_seconds(electric_energy_joules, watt):
    """calculating watt to seconds."""
    return electric_energy_joules / watt


if __name__ == '__main__':

    print("\nWelcome to the emcalc application")

    Preset = input("[1]BWR (Fukushima)\n[*]manuel\n")

    if Preset == "*":
        j_to_electric = input("please input the jul to electric efficeny example for %5: 0.05 defualt is 0.35: ")

        one_usage_efficiency = input("please input the one usage efficieny example for %0.5: 0.005 defualt is 0.001")

        long_term_efficieny = input("please input the mass to Heat efficieny defualt 0.90: ")
        device_name = "led"
        watt = 10

        long_term_efficieny = float(input("Enter the mass-energy conversion efficiency (example: for 5%, enter 0.05): "))
    elif Preset == "1":
        j_to_electric = 0.31

        one_usage_efficiency = 0.001

        long_term_efficieny = 0.90

        device_name = "led"
        watt = 10

    else:
        exit()

    kütle_gram = float(input("Enter the mass (grams): "))

    kg = grams_to_kg(kütle_gram)
    theoretical_energy = calculate_theoretical_energy(kg)
    long_term_practical_energy = calculate_practical_energy(theoretical_energy, long_term_efficieny)
    
    one_usage_practical_energy = calculate_practical_energy(theoretical_energy, one_usage_efficiency)
    
    long_term_electric_energy = convert_joules_to_electricity(long_term_practical_energy, j_to_electric)
    
    one_usage_electric_energy = convert_joules_to_electricity(one_usage_practical_energy, j_to_electric)
    one_usage_time_seconds = calculate_led_on_time_seconds(one_usage_electric_energy, watt)
    one_usage_time_hours = one_usage_time_seconds / 3600



    print("\n--- RESULTS ---")
    print(f"Long term practical energy (at {long_term_efficieny:.2f}% efficiency): {long_term_practical_energy:.0f} Joules")
    print(f"One usage practical energy (at {one_usage_efficiency:.3f}% efficiency): {long_term_practical_energy:.0f} Joules")
    print(f"Theoretical energy (at 100% efficiency): {theoretical_energy:.0f} Joules")
    print("-" * 20)
    print(f"With the electricity generated from this energy, a {watt}-watt {device_name}:")
    print(f"Can run for approximately {one_usage_time_seconds:.0f} seconds.")
    print(f"(This is approximately {one_usage_time_hours:.0f} hours.)")

    input("for exit the program click the Enter")
