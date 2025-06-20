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
    # Verimlilik 0 ile 1 arasında olmalı (örn: 0.35)
    converted_electric_joules = practical_energy_joules * conversion_efficiency
    return converted_electric_joules

def calculate_led_on_time_seconds(electric_energy_joules, led_power_watts):
    """Elektrik enerjisiyle bir LED'in kaç saniye yanacağını hesaplar."""
    # Zaman (saniye) = Enerji (Joule) / Güç (Watt)
    seconds = electric_energy_joules / led_power_watts
    return seconds


if __name__ == '__main__':
    #veriables | değişkenler
    j_to_electric = 0.35
    
    device_name = "led"
    watt = 10

    lang = input("Select a Language (tr/en):")
    
    # --TURKISH--
    if lang == "tr" :
        
        # Queries
        kg = grams_to_kg(float(input("kütle giriniz (gram):")))
        efficiency = float(input("verimlilik oranı veriniz (örnek %5 için 0.5) :"))
        
        # Calculating
        theoretical_energy = calculate_theoretical_energy(kg)
        practical_energy = calculate_practical_energy(theoretical_energy, efficiency)

        electric_energy = convert_joules_to_electricity(practical_energy, j_to_electric)

        yanma_suresi = calculate_led_on_time_seconds(electric_energy, 10)

        # Result
        print(f"%{efficiency} (0'ı saymayınız) verimlilik ile")
        print("pratik enerji {practical_energy} joule'dur")
        print(f"%100 verimlilik olsaydı {theoretical_energy} joule olurdu")
        print(f"{kg} kilogram kütleden elde edilen elektrikle {watt} watt'lık {device_name} ,")
        print(f"Yaklaşık {yanma_suresi:.2f} saniye boyunca yanabilir.")
        print(f"(Bu süre yaklaşık {yanma_suresi / 3600:.2f} saattir.)")

    elif lang == "en" :
        
        # Queries
        kg = grams_to_kg(float(input("Enter the mass (grams) :")))
        efficiency = float(input("Enter the efficiency rate (example: for 5%, enter 0.5) :"))
        
        # Calculating
        theoretical_energy = calculate_theoretical_energy(kg)
        practical_energy = calculate_practical_energy(theoretical_energy, efficiency)

        electric_energy = convert_joules_to_electricity(practical_energy, j_to_electric)

        burn_time = calculate_led_on_time_seconds(electric_energy, 10)

        #Result
        print(f"with {efficiency}% (never mind 0) efficiency")
        print("pratik energy is {practical_energy} joule'")
        print(f"With 100% efficiency, it would be {theoretical_energy} joules.")
        print(f"The electricity generated from {kg} kg of mass could **run** a {watt}-watt {device_name}")
        print(f"It can burn for approximately {burn_time:.2f} seconds.")
        print(f"(it is approximately {burn_time / 3600:.2f} hour.)")
    
# Thank You
# 2013dogumeymen | creator
# tarikcelik
# gemini | bugfix, localization, library connections