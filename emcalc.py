# region ---imports---
from scipy.constants import c
# endregion


langs = (
    "\n\n---Languages---"
    "\n[tr]Türkçe"
    "\n[en]English")

# region ---functions---
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
    return grams / 1000
def calculate_theoretical_energy(mass_kg):
    """calculating E=mc2 (%100 efficiency)."""
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
def _calculations(mass_gram):
    kg = grams_to_kg(mass_gram)
    theoretical_energy = calculate_theoretical_energy(kg)
    long_term_practical_energy = calculate_practical_energy(theoretical_energy, long_term_efficiency)
    one_usage_practical_energy = calculate_practical_energy(theoretical_energy, one_usage_efficiency)
    long_term_electric_energy = convert_joules_to_electricity(long_term_practical_energy, j_to_electric)
    one_usage_electric_energy = convert_joules_to_electricity(one_usage_practical_energy, j_to_electric)
    one_usage_time_seconds = calculate_led_on_time_seconds(one_usage_electric_energy, watt)
    one_usage_time_hours = one_usage_time_seconds / 3600
    return (long_term_efficiency, long_term_practical_energy,
            one_usage_efficiency, one_usage_practical_energy,
            theoretical_energy, watt, device_name,
            one_usage_time_seconds, one_usage_time_hours)
def _results(lang, long_term_efficiency, long_term_practical_energy, one_usage_efficiency, one_usage_practical_energy, theoretical_energy, watt, device_name, one_usage_time_seconds, one_usage_time_hours):
    
    if lang == "tr":
        print("\n--- SONUÇLAR ---")
        print(f"Uzun vadeli pratik enerji (verimlilik: {long_term_efficiency:.2f}%): {long_term_practical_energy:.0f} Joule")
        print(f"Tek kullanım pratik enerji (verimlilik: {one_usage_efficiency:.3f}%): {one_usage_practical_energy:.0f} Joule")
        print(f"Teorik enerji (verimlilik: %100): {theoretical_energy:.0f} Joule")
        print("-" * 20)
        print(f"Bu enerjiden üretilen elektrikle, {device_name} ({watt} watt):")
        print(f"Yaklaşık olarak {one_usage_time_seconds:.0f} saniye çalışabilir.")
        print(f"(Bu yaklaşık olarak {one_usage_time_hours:.0f} saat.)")
        # translated with github copilot
    else:
        print("\n--- RESULTS ---")
        print(f"Long term practical energy (at {long_term_efficiency:.2f}% efficiency): {long_term_practical_energy:.0f} Joules")
        print(f"One usage practical energy (at {one_usage_efficiency:.3f}% efficiency): {one_usage_practical_energy:.0f} Joules")
        print(f"Theoretical energy (at 100% efficiency): {theoretical_energy:.0f} Joules")
        print("-" * 20)
        print(f"With the electricity generated from this energy, a {watt}-watt {device_name}:")
        print(f"Can run for approximately {one_usage_time_seconds:.0f} seconds.")
        print(f"(This is approximately {one_usage_time_hours:.0f} hours.)")
# endregion



if __name__ == '__main__':
    
    # region welcome screen
    print("\n" * 100)
    print("Welcome to the emcalc application")
    # endregion

    # region input
    lang = input(langs + "\nSelect: ").strip().lower()

    if lang == "tr":
        Presets =(
        "\n\n---Ön Ayarlar---"
        "\n[1]PWR (Gravelines NGS,Ringhals-2-3-4,Kori 1-2-3-4)"
        "\n[1]BWR (Fukuşima, Ringhals-1)"
        "\n[3]PHWR (Bruce NGS, Olkiluoto NGS 1-2)"
        "\n[4]EPR (Olkiluoto NGS 3)"
        "\n[5]APR1400 (Shin-Kori 3-4-5-6)"
        "\n[*]elle")
    else:
        Presets =(
        "\n\n---Presets---"
        "\n[1]PWR (Gravelines NGS,Ringhals-2-3-4,Kori 1-2-3-4)"
        "\n[1]BWR (Fukushima, Ringhals-1)"
        "\n[3]PHWR (Bruce NGS, Olkiluoto NGS 1-2)"
        "\n[4]EPR (Olkiluoto NGS 3)"
        "\n[5]APR1400 (Shin-Kori 3-4-5-6)"
        "\n[*]manuel")

    Preset = input(Presets + "\nSelect: ")

    if Preset == "1":
        j_to_electric = 0.33

        one_usage_efficiency = 0.001

        long_term_efficiency = 0.90

        device_name = "led"
        watt = 10
    elif Preset == "2":
        j_to_electric = 0.31

        one_usage_efficiency = 0.001

        long_term_efficiency = 0.90

        device_name = "led"
        watt = 10
    elif Preset == "3":
        j_to_electric = 0.30

        one_usage_efficiency = 0.001

        long_term_efficiency = 0.85

        device_name = "led"
        watt = 10
    elif Preset == "4":
        j_to_electric = 0.38

        one_usage_efficiency = 0.001

        long_term_efficiency = 0.93

        device_name = "led"
        watt = 10
    elif Preset == "5":
        j_to_electric = 0.38

        one_usage_efficiency = 0.001

        long_term_efficiency = 0.92

        device_name = "led"
        watt = 10
    elif Preset == "3.14":
        easter_egg()
    elif  Preset == "3,14":
        easter_egg()
    else:
        if lang == "tr":
            j_to_electric = input("Lütfen jul'den elektrik verimliliğini giriniz örnek %5: 0.05 varsayılan 0.35: ")

            one_usage_efficiency = 0.001

            long_term_efficiency = input("Lütfen kütleden ısıya verimliliğini giriniz varsayılan 0.90: ")
            device_name = "led"
            watt = 10

            long_term_efficiency = float(input("Kütle-enerji dönüşüm verimliliğini giriniz (örnek: %5 için, 0.05 giriniz): "))
        else:
            j_to_electric = input("please input the jul to electric efficeny example for %5: 0.05 defualt is 0.35: ")

            one_usage_efficiency = 0.001

            long_term_efficiency = input("please input the mass to Heat efficieny defualt 0.90: ")
            device_name = "led"
            watt = 10

            long_term_efficiency = float(input("Enter the mass-energy conversion efficiency (example: for 5%, enter 0.05): "))
    
    if lang == "tr":
        mass_gram = float(input("Lütfen kütleyi giriniz (gram): "))
    else:
        mass_gram = float(input("Enter the mass (grams): "))
    # endregion
    
    results = _calculations(mass_gram)

    _results(lang, *results)

    input()