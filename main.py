import scipy.constants as const

# Değişkenler
led_watt = 10
joule_elektrik_verimlilik_orani = 35

lang = input("Please select language (tr/en): ").lower()

# --- TURKISH ---
if lang == "tr":
    print("\nE = mc^2 Gelişmiş Enerji Hesaplayıcısına Hoşgeldiniz")
    
    # Hatalı girişe karşı programın çökmesini engelleyen try-except bloğu
    try:
        m_gram = float(input("Kütle giriniz (gram): "))
        verimlilik_yuzdesi = float(input("Bu kütlenin enerjiye dönüşüm verimliliği nedir? (% olarak, örn: 0.1): "))
    except ValueError:
        print("Hatalı giriş! Lütfen sadece sayı giriniz.")
        exit()
    
    # Hesaplamalar
    m_kg = m_gram / 1000
    teorik_enerji = m_kg * const.c**2
    verimlilik_orani = verimlilik_yuzdesi / 100
    
    # DÜZELTİLDİ: Pratik enerji hesabı çıkarma değil, çarpma olmalı.
    pratik_enerji = teorik_enerji * verimlilik_orani
    
    # LED saniyesi pratik enerjiye göre hesaplanmalı.
    elektrik_dönüşüm_verimlilik = joule_elektrik_verimlilik_orani * pratik_enerji
    led_saniye = elektrik_dönüşüm_verimlilik / led_watt

    # DÜZELTİLDİ: Çıktı, her değeri net bir şekilde gösterecek şekilde yeniden düzenlendi.
    print("\n--- SONUÇLAR ---")
    print(f"Teorik Enerji (%100 Verimle): {teorik_enerji:,.2f} Joule")
    print(f"Pratik Enerji (%{verimlilik_yuzdesi} Verimle): {pratik_enerji:,.2f} Joule")
    print(f"Bu pratik enerjinin elektriğe dönüşümü ile, {led_watt} Watt'lık bir LED lambayı aralıksız olarak yaklaşık {led_saniye:,.0f} saniye çalıştırabilir.")






# --- ENGLISH ---
elif lang == "en":
    print("\nWelcome to the Advanced E = mc^2 Energy Calculator")
    
    try:
        m_gram = float(input("Enter the mass (grams): "))
        efficiency_percentage = float(input("What is the energy conversion efficiency of this mass? (as %, e.g., 0.1): "))
    except ValueError:
        print("Invalid input! Please enter only numbers.")
        exit()

    m_kg = m_gram / 1000

    theoretical_energy = m_kg * const.c**2
    
    efficiency_ratio = efficiency_percentage / 100
    practical_energy = theoretical_energy * efficiency_ratio
    led_seconds = practical_energy / led_watt

    print("\n--- RESULTS ---")
    print(f"Theoretical Energy (at 100% efficiency): {theoretical_energy:,.2f} Joules")
    print(f"Practical Energy (at {efficiency_percentage}% efficiency): {practical_energy:,.2f} Joules")
    print(f"This practical energy to electric could power a {led_watt}-Watt LED lamp for approximately {led_seconds:,.0f} seconds.")

else:
    print("Language not supported. Please select 'tr' or 'en'.")
    exit()


input("\nÇıkmak için Enter'a basın... / Press Enter to exit...")


#THANKYOU
# 2013dogumeymen | creator
# tarik-celik 
# gemini | bugfix, localization 
