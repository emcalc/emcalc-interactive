import scipy.constants as const
import scipy

led_watt = 10

lang = input("please select language (tr/en): ")

startmsg_tr = "E = mc^2 hesaplama programına hoşgeldiniz"
startmsg_en = "Welcome to the E = mc^2 calculation program"
msg2_tr = "Kütle giriniz (gram): "
msg2_en = "Enter the mass (gram): "

if lang == "tr":
    print(startmsg_tr)
    m_gram = float(input(msg2_tr))                                      
    m_kg = m_gram / 1000
    enerji = m_kg * const.c**2
    led_second = enerji / led_watt
    print(f"{m_kg} kg kütlenin enerjisi {enerji:,.2f} joule'dür. bu, {led_second} kadar saniye 10 watt'lık bir led lambanın kesintisiz yakabilir")

elif lang == "en":
    print(startmsg_en)
    m_gram = float(input(msg2_en))
    m_kg = m_gram / 1000
    enerji = m_kg * const.c
    led_second = enerji / led_watt
    print(f"{m_kg} kg mass has {enerji:,.2f} joule energy. it is {led_second} second = 10 watt led lamb gross lighting")

else:
    print("not supported language please select tr or en")
    exit()

input()
