import light_speed

lang = input("please select language (tr/en): ")

if lang == "tr":
    print("E = mc^2 hesaplama programına hoşgeldiniz")
else:
    print("Welcome to the E = mc^2 calculation program")

if lang == "tr":
    m_gram = float(input("Kütle giriniz (gram): "))
else:
    m_gram = float(input("Enter the mass (gram): "))

m_kg = m_gram / 1000

enerji = m_kg * light_speed.c2

if lang == "tr":
    # Buraya 'f' harfini ekledik!
    print(f"{m_kg:,} kg kütlenin enerjisi {enerji:,f} joule'dür.")
else:
    print(f"{m_kg:,} kg mass has {enerji:,f} joule energy.")