from libemcalc import *
import math

WORLD_POWER_W = 2.0e13  # ~20 TW, küresel ortalama güç varsayımı

langs = (
    "\n\n---Languages---"
    "\n[tr]Türkçe"
    "\n[en]English")

# region ---functions---
def easter_egg():
    print("\nπ mode unlocked. Nothing special here… yet :)")

def _calculations(mass_gram, long_term_efficiency, one_usage_efficiency, j_to_electric, watt, device_name):
    kg = grams_to_kg(mass_gram)
    theoretical_energy = calculate_theoretical_energy(kg)
    long_term_practical_energy = calculate_practical_energy(theoretical_energy, long_term_efficiency)
    one_usage_practical_energy = calculate_practical_energy(theoretical_energy, one_usage_efficiency)
    # long_term_electric_energy = convert_joules_to_electricity(long_term_practical_energy, j_to_electric) - comming soon
    one_usage_electric_energy = convert_joules_to_electricity(one_usage_practical_energy, j_to_electric)
    one_usage_time_seconds = calculate_led_on_time_seconds(one_usage_electric_energy, watt)
    one_usage_time_hours = one_usage_time_seconds / 3600

    # Additional calculations for Kardashev scale
    p_added_year = one_usage_electric_energy / (365 * 24 * 3600)  # power added averaged over a year
    K_world = math.log10(WORLD_POWER_W) / 10
    K_new = math.log10(WORLD_POWER_W + p_added_year) / 10
    deltaK = K_new - K_world

    return (long_term_efficiency, long_term_practical_energy,
            one_usage_efficiency, one_usage_practical_energy,
            theoretical_energy, watt, device_name,
            one_usage_time_seconds, one_usage_time_hours,
            p_added_year, K_world, K_new, deltaK)

def _results(lang, long_term_efficiency, long_term_practical_energy, one_usage_efficiency, one_usage_practical_energy, theoretical_energy, watt, device_name, one_usage_time_seconds, one_usage_time_hours, p_added_year, K_world, K_new, deltaK):
    
    if lang == "tr":
        print("\n--- SONUÇLAR ---")
        print(f"Uzun vadeli pratik enerji (verimlilik: {long_term_efficiency*100:.2f}%): {long_term_practical_energy:.0f} Joule")
        print(f"Tek kullanım pratik enerji (verimlilik: {one_usage_efficiency*100:.3f}%): {one_usage_practical_energy:.0f} Joule")
        print(f"Teorik enerji (verimlilik: %100): {theoretical_energy:.0f} Joule")
        print("-" * 20)
        print(f"Bu enerjiden üretilen elektrikle, {device_name} ({watt} watt):")
        print(f"Yaklaşık olarak {one_usage_time_seconds:.0f} saniye çalışabilir.")
        print(f"(Bu yaklaşık olarak {one_usage_time_hours:.0f} saat.)")
        print(f"(Bu yaklaşık olarak {one_usage_time_hours/24:.2f} gün.)")
        print(f"(Bu yaklaşık olarak {one_usage_time_hours/24/365:.2f} yıl.)")
        print(f"(Bu yaklaşık olarak {one_usage_time_hours/24/365/100:.4f} asır.)")
        print(f"(Bu yaklaşık olarak {one_usage_time_hours/24/365/1000:.2f} bin yıl.)")
        print("=" * 20 + " KARDASHEV " + "=" * 20)
        print(f"Dünya (varsayım): P≈{WORLD_POWER_W:.2e} W → K≈{K_world:.6f}")
        print(f"Senin katkın (1 yıla yayılmış): +{p_added_year:.2e} W")
        print(f"Yeni K ≈ {K_new:.6f}  |  ΔK ≈ {deltaK:.2e}")
    else:
        print("\n--- RESULTS ---")
        print(f"Long term practical energy (at {long_term_efficiency*100:.2f}% efficiency): {long_term_practical_energy:.0f} Joules")
        print(f"One usage practical energy (at {one_usage_efficiency*100:.3f}% efficiency): {one_usage_practical_energy:.0f} Joules")
        print(f"Theoretical energy (at 100% efficiency): {theoretical_energy:.0f} Joules")
        print("-" * 20)
        print(f"With the electricity generated from this energy, a {watt}-watt {device_name}:")
        print(f"Can run for approximately {one_usage_time_seconds:.0f} seconds.")
        print(f"(This is approximately {one_usage_time_hours:.0f} hours.)")
        print(f"(This is approximately {one_usage_time_hours/24:.2f} days.)")
        print(f"(This is approximately {one_usage_time_hours/24/365:.2f} years.)")
        print(f"(This is approximately {one_usage_time_hours/24/365/100:.4f} centuries.)")
        print(f"(This is approximately {one_usage_time_hours/24/365/1000:.2f} millennia.)")
        print("=" * 20 + " KARDASHEV " + "=" * 20)
        print(f"World (assumed): P≈{WORLD_POWER_W:.2e} W → K≈{K_world:.6f}")
        print(f"Your contribution (spread over 1 year): +{p_added_year:.2e} W")
        print(f"New K ≈ {K_new:.6f}  |  ΔK ≈ {deltaK:.2e}")
# endregion

def main():
    # warning
    print("\n" * 100)
    print("Warning!")
    print("Warning! Please comply with the laws of your country. Disclaimer: This program was not written with malicious intent by the authors, and any failure by users to comply with the laws of their country does not affect the program developers.")
    print("")
    print("")
    print("To continue, please type 'I HAVE READ AND ACCEPT'. For more information: https://www.un.org/en ")
    Accept = input("Write: ")

    if Accept == "I HAVE READ AND ACCEPT":
        print("Opening the program...")
    else:
        print("You can't use it")
        while True:
            pass

    # region welcome screen
    print("\n" * 100)
    print("Welcome to the emcalc application")
    # endregion

    # region input
    _lang_in = input(langs + "\nSelect: ").strip().lower()
    lang = _lang_in if _lang_in in ("tr", "en") else "en"

    if lang == "tr":
        Presets =(
        "\n\n---Ön Ayarlar---"
        "\n[1]PWR (Gravelines NGS,Ringhals-2-3-4,Kori 1-2-3-4)"
        "\n[2]BWR (Fukuşima, Ringhals-1)"
        "\n[3]PHWR (Bruce NGS, Olkiluoto NGS 1-2)"
        "\n[4]EPR (Olkiluoto NGS 3)"
        "\n[5]APR1400 (Shin-Kori 3-4-5-6)"
        "\n[*]elle")
    else:
        Presets =(
        "\n\n---Presets---"
        "\n[1]PWR (Gravelines NGS,Ringhals-2-3-4,Kori 1-2-3-4)"
        "\n[2]BWR (Fukushima, Ringhals-1)"
        "\n[3]PHWR (Bruce NGS, Olkiluoto NGS 1-2)"
        "\n[4]EPR (Olkiluoto NGS 3)"
        "\n[5]APR1400 (Shin-Kori 3-4-5-6)"
        "\n[*]manual")

    Preset = input(Presets + "\nSelect: ")

    if Preset == "1":
        j_to_electric = 0.33

        one_usage_efficiency = 0.001

        long_term_efficiency = 0.90

        device_name = "ampul"
        watt = 100
    elif Preset == "2":
        j_to_electric = 0.31

        one_usage_efficiency = 0.001

        long_term_efficiency = 0.90

        device_name = "ampul"
        watt = 100
    elif Preset == "3":
        j_to_electric = 0.30

        one_usage_efficiency = 0.001

        long_term_efficiency = 0.85

        device_name = "ampul"
        watt = 100
    elif Preset == "4":
        j_to_electric = 0.38

        one_usage_efficiency = 0.001

        long_term_efficiency = 0.93

        device_name = "ampul"
        watt = 100
    elif Preset == "5":
        j_to_electric = 0.38

        one_usage_efficiency = 0.001

        long_term_efficiency = 0.92

        device_name = "ampul"
        watt = 100
    elif Preset == "3.14":
        easter_egg()
    elif  Preset == "3,14":
        easter_egg()
    else:
        if lang == "tr":
            try:
                _j_in = input("Lütfen joule'den elektriğe verimliliği giriniz (örnek %5 için 0.05). Varsayılan 0.35 için Enter'a basın: ").strip()
                j_to_electric = 0.35 if _j_in == "" else float(_j_in)
            except ValueError:
                print("Geçersiz giriş! Program sonlandırılıyor.")
                exit()

            one_usage_efficiency = 0.001

            try:
                _eff_in = input("Kütle-enerji dönüşüm verimliliğini giriniz (örnek: %5 için 0.05). Varsayılan 0.90 için Enter'a basın: ").strip()
                long_term_efficiency = 0.90 if _eff_in == "" else float(_eff_in)
            except ValueError:
                print("Geçersiz giriş! Program sonlandırılıyor.")
                exit()

            device_name = "ampul"
            watt = 100
        else:
            try:
                _j_in = input("Please enter the joule-to-electricity efficiency (e.g., 0.05 for 5%). Press Enter for default 0.35: ").strip()
                j_to_electric = 0.35 if _j_in == "" else float(_j_in)
            except ValueError:
                print("Invalid input! Exiting program.")
                exit()

            one_usage_efficiency = 0.001

            try:
                _eff_in = input("Enter the mass-energy conversion efficiency (e.g., 0.05 for 5%). Press Enter for default 0.90: ").strip()
                long_term_efficiency = 0.90 if _eff_in == "" else float(_eff_in)
            except ValueError:
                print("Invalid input! Exiting program.")
                exit()

            device_name = "bulb"
            watt = 100
    
    try:
        if lang == "tr":
            mass_text = input("Lütfen kütleyi giriniz (gram): ").strip()
        else:
            mass_text = input("Enter the mass (grams): ").strip()
        mass_gram = float(mass_text)
        if mass_gram <= 0:
            raise ValueError
    except ValueError:
        if lang == "tr":
            print("Geçersiz giriş! Kütle 0'dan büyük bir sayı olmalıdır. Program sonlandırılıyor.")
        else:
            print("Invalid input! Mass must be a number greater than 0. Exiting program.")
        exit()
    # endregion
    
    results = _calculations(mass_gram, long_term_efficiency, one_usage_efficiency, j_to_electric, watt, device_name)

    _results(lang, *results)

    input()

if __name__ == "__main__":
    main()