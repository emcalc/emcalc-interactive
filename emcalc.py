import scipy.constants as const

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


if __name__ == '__main__':
    j_to_electric = 0.35
    device_name = "led"
    watt = 10

    lang = input("Select a Language (tr/en): ")
    
    if lang == "tr":
        print("\nemcalc uygulamasına hoş geldiniz")
        kütle_gram = float(input("Kütle giriniz (gram): "))
        verimlilik = float(input("Kütle-enerji dönüşüm verimliliğini giriniz (örnek: %5 için 0.05): "))
    elif lang == "en":
        print("\nWelcome to the emcalc application")
        kütle_gram = float(input("Enter the mass (grams): "))
        verimlilik = float(input("Enter the mass-energy conversion efficiency (example: for 5%, enter 0.05): "))
    else:
        print("Geçersiz dil seçimi. / Invalid language selection.")
        exit() 

    kg = grams_to_kg(kütle_gram)
    theoretical_energy = calculate_theoretical_energy(kg)
    practical_energy = calculate_practical_energy(theoretical_energy, verimlilik)
    electric_energy = convert_joules_to_electricity(practical_energy, j_to_electric)
    on_time_seconds = calculate_led_on_time_seconds(electric_energy, watt)
    on_time_hours = on_time_seconds / 3600

    
    if lang == "tr":
        print("\n--- SONUÇLAR ---")
        print(f"Pratik enerji ({verimlilik*100:.0f}% verimlilikle): {practical_energy:.0f} Joule")
        print(f"Teorik enerji (%100 verimlilikle): {theoretical_energy:.0f} Joule")
        print("-" * 20)
        print(f"Bu enerjiden elde edilen elektrikle {watt} Watt'lık {device_name}:")
        print(f"Yaklaşık {on_time_seconds:.0f} saniye boyunca yanabilir.")
        print(f"(Bu süre yaklaşık {on_time_hours:.0f} saattir.)")

    elif lang == "en":
        print("\n--- RESULTS ---")
        print(f"Practical energy (at {verimlilik*100:.0f}% efficiency): {practical_energy:.0f} Joules")
        print(f"Theoretical energy (at 100% efficiency): {theoretical_energy:.0f} Joules")
        print("-" * 20)
        print(f"With the electricity generated from this energy, a {watt}-watt {device_name}:")
        print(f"Can run for approximately {on_time_seconds:.0f} seconds.")
        print(f"(This is approximately {on_time_hours:.0f} hours.)")

    input("")