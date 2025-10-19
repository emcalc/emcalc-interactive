#!/usr/bin/env python3
"""emcalc: energy-mass calculator with a single-file CLI."""

import argparse
import sys
from dataclasses import dataclass
from typing import Dict, Optional

C = 299792458

WARNING_TEXT = (
    "\nWarning!\n"
    "Warning! Please comply with the laws of your country. Disclaimer: This program was not "
    "written with malicious intent by the authors, and any failure by users to comply with the laws "
    "of their country does not affect the program developers.\n\n"
    "To continue, please type 'I HAVE READ AND ACCEPT'. For more information: https://www.un.org/en\n"
)

LANG_PROMPT = (
    "\n\n---Languages---"
    "\n[tr]Türkçe"
    "\n[en]English"
)

PRESET_PROMPTS = {
    "tr": (
        "\n\n---Ön Ayarlar---"
        "\n[1]PWR (Gravelines NGS,Ringhals-2-3-4,Kori 1-2-3-4, Akkuyu Nükleer)"
        "\n[2]BWR (Fukuşima, Ringhals-1)"
        "\n[3]PHWR (Bruce NGS, Olkiluoto NGS 1-2)"
        "\n[4]EPR (Olkiluoto NGS 3)"
        "\n[5]APR1400 (Shin-Kori 3-4-5-6)"
        "\n[*]elle"
    ),
    "en": (
        "\n\n---Presets---"
        "\n[1]PWR (Gravelines NGS,Ringhals-2-3-4,Kori 1-2-3-4, Akkuyu Nuclear)"
        "\n[2]BWR (Fukushima, Ringhals-1)"
        "\n[3]PHWR (Bruce NGS, Olkiluoto NGS 1-2)"
        "\n[4]EPR (Olkiluoto NGS 3)"
        "\n[5]APR1400 (Shin-Kori 3-4-5-6)"
        "\n[*]manual"
    ),
}


@dataclass
class CalculationConfig:
    j_to_electric: float
    one_usage_efficiency: float
    long_term_efficiency: float
    device_name: str
    watt: float


PRESETS: Dict[str, CalculationConfig] = {
    "1": CalculationConfig(0.33, 0.001, 0.90, "ampul", 100),
    "2": CalculationConfig(0.31, 0.001, 0.90, "ampul", 100),
    "3": CalculationConfig(0.30, 0.001, 0.85, "ampul", 100),
    "4": CalculationConfig(0.38, 0.001, 0.93, "ampul", 100),
    "5": CalculationConfig(0.38, 0.001, 0.92, "ampul", 100),
}


def grams_to_kg(grams: float) -> float:
    return grams / 1000


def calculate_theoretical_energy(mass_kg: float) -> float:
    return mass_kg * C**2


def calculate_practical_energy(theoretical_energy: float, efficiency: float) -> float:
    return theoretical_energy * efficiency


def convert_joules_to_electricity(practical_energy_joules: float, conversion_efficiency: float) -> float:
    return practical_energy_joules * conversion_efficiency


def calculate_led_on_time_seconds(electric_energy_joules: float, watt: float) -> float:
    return electric_energy_joules / watt


def easter_egg() -> None:
    print("\nπ mode unlocked. Nothing special here... yet :)")


def _default_config(lang: str) -> CalculationConfig:
    device_name = "ampul" if lang == "tr" else "bulb"
    return CalculationConfig(0.35, 0.001, 0.90, device_name, 100)


def _build_config(
    lang: str,
    preset_key: Optional[str],
    j_to_electric: Optional[float],
    one_usage_efficiency: Optional[float],
    long_term_efficiency: Optional[float],
    device_name: Optional[str],
    watt: Optional[float],
) -> CalculationConfig:
    config = _default_config(lang)

    if preset_key:
        if preset_key in ("3.14", "3,14"):
            easter_egg()
            sys.exit(0)
        preset = PRESETS.get(preset_key)
        if preset is None:
            raise ValueError("Unknown preset selected.")
        config = CalculationConfig(
            j_to_electric=preset.j_to_electric,
            one_usage_efficiency=preset.one_usage_efficiency,
            long_term_efficiency=preset.long_term_efficiency,
            device_name=preset.device_name if lang == "tr" else "bulb",
            watt=preset.watt,
        )

    if j_to_electric is not None:
        config.j_to_electric = j_to_electric
    if one_usage_efficiency is not None:
        config.one_usage_efficiency = one_usage_efficiency
    if long_term_efficiency is not None:
        config.long_term_efficiency = long_term_efficiency
    if device_name is not None:
        config.device_name = device_name
    if watt is not None:
        config.watt = watt

    return config


def _perform_calculations(mass_gram: float, config: CalculationConfig):
    kg = grams_to_kg(mass_gram)
    theoretical_energy = calculate_theoretical_energy(kg)
    long_term_practical_energy = calculate_practical_energy(theoretical_energy, config.long_term_efficiency)
    one_usage_practical_energy = calculate_practical_energy(theoretical_energy, config.one_usage_efficiency)
    one_usage_electric_energy = convert_joules_to_electricity(one_usage_practical_energy, config.j_to_electric)
    one_usage_time_seconds = calculate_led_on_time_seconds(one_usage_electric_energy, config.watt)
    one_usage_time_hours = one_usage_time_seconds / 3600
    return {
        "long_term_efficiency": config.long_term_efficiency,
        "long_term_practical": long_term_practical_energy,
        "one_usage_efficiency": config.one_usage_efficiency,
        "one_usage_practical": one_usage_practical_energy,
        "theoretical": theoretical_energy,
        "device_name": config.device_name,
        "watt": config.watt,
        "seconds": one_usage_time_seconds,
        "hours": one_usage_time_hours,
    }


def _print_results(lang: str, data: Dict[str, float]) -> None:
    if lang == "tr":
        print("\n--- SONUÇLAR ---")
        print(f"Uzun vadeli pratik enerji (verimlilik: {data['long_term_efficiency']*100:.2f}%): {data['long_term_practical']:.0f} Joule")
        print(f"Tek kullanım pratik enerji (verimlilik: {data['one_usage_efficiency']*100:.3f}%): {data['one_usage_practical']:.0f} Joule")
        print(f"Teorik enerji (verimlilik: %100): {data['theoretical']:.0f} Joule")
        print("-" * 20)
        print(f"Bu enerjiden üretilen elektrikle, {data['device_name']} ({data['watt']} watt):")
        print(f"Yaklaşık olarak {data['seconds']:.0f} saniye çalışabilir.")
        print(f"(Bu yaklaşık olarak {data['hours']:.0f} saat.)")
        print(f"(Bu yaklaşık olarak {data['hours']/24:.2f} gün.)")
        print(f"(Bu yaklaşık olarak {data['hours']/24/365:.2f} yıl.)")
    else:
        print("\n--- RESULTS ---")
        print(f"Long term practical energy (at {data['long_term_efficiency']*100:.2f}% efficiency): {data['long_term_practical']:.0f} Joules")
        print(f"One usage practical energy (at {data['one_usage_efficiency']*100:.3f}% efficiency): {data['one_usage_practical']:.0f} Joules")
        print(f"Theoretical energy (at 100% efficiency): {data['theoretical']:.0f} Joules")
        print("-" * 20)
        print(f"With the electricity generated from this energy, a {data['watt']}-watt {data['device_name']}:")
        print(f"Can run for approximately {data['seconds']:.0f} seconds.")
        print(f"(This is approximately {data['hours']:.0f} hours.)")
        print(f"(This is approximately {data['hours']/24:.2f} days.)")
        print(f"(This is approximately {data['hours']/24/365:.2f} years.)")


def _prompt_acceptance() -> bool:
    print(WARNING_TEXT)
    response = input("Write: ").strip()
    allowed = response == "I HAVE READ AND ACCEPT"
    if allowed:
        print("Opening the program...")
    else:
        print("You can't use it")
    return allowed


def _interactive_flow() -> int:
    if not _prompt_acceptance():
        return 1

    print("\n" * 2 + "Welcome to the emcalc application")
    _lang_in = input(LANG_PROMPT + "\nSelect: ").strip().lower()
    lang = _lang_in if _lang_in in ("tr", "en") else "en"

    preset_choice = input(PRESET_PROMPTS[lang] + "\nSelect: ").strip()
    if preset_choice in ("3.14", "3,14"):
        easter_egg()
        return 0

    try:
        config = _build_config(
            lang,
            preset_choice if preset_choice in PRESETS else None,
            None,
            None,
            None,
            None,
            None,
        )
    except ValueError:
        print("Invalid preset! Exiting program.")
        return 1

    if preset_choice not in PRESETS:
        try:
            if lang == "tr":
                _j_in = input("Lütfen joule'den elektriğe verimliliği giriniz (örnek %5 için 0.05). Varsayılan 0.35 için Enter'a basın: ").strip()
            else:
                _j_in = input("Please enter the joule-to-electricity efficiency (e.g., 0.05 for 5%). Press Enter for default 0.35: ").strip()
            if _j_in:
                config.j_to_electric = float(_j_in)
        except ValueError:
            print("Geçersiz giriş! Program sonlandırılıyor." if lang == "tr" else "Invalid input! Exiting program.")
            return 1

        try:
            if lang == "tr":
                _eff_in = input("Kütle-enerji dönüşüm verimliliğini giriniz (örnek: %5 için 0.05). Varsayılan 0.90 için Enter'a basın: ").strip()
            else:
                _eff_in = input("Enter the mass-energy conversion efficiency (e.g., 0.05 for 5%). Press Enter for default 0.90: ").strip()
            if _eff_in:
                config.long_term_efficiency = float(_eff_in)
        except ValueError:
            print("Geçersiz giriş! Program sonlandırılıyor." if lang == "tr" else "Invalid input! Exiting program.")
            return 1

        if lang == "tr":
            config.device_name = "ampul"
        else:
            config.device_name = "bulb"
        config.watt = 100

    try:
        if lang == "tr":
            mass_text = input("Lütfen kütleyi giriniz (gram): ").strip()
        else:
            mass_text = input("Enter the mass (grams): ").strip()
        mass_gram = float(mass_text)
        if mass_gram <= 0:
            raise ValueError
    except ValueError:
        print("Geçersiz giriş! Kütle 0'dan büyük bir sayı olmalıdır. Program sonlandırılıyor." if lang == "tr" else "Invalid input! Mass must be a number greater than 0. Exiting program.")
        return 1

    data = _perform_calculations(mass_gram, config)
    _print_results(lang, data)
    input("\nPress Enter to exit.")
    return 0


def _parse_args(argv: Optional[list] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Energy-mass calculator (E=mc^2) CLI.")
    parser.add_argument("--mass", type=float, help="Mass in grams (required unless --interactive).")
    parser.add_argument("--lang", choices=("en", "tr"), default="en", help="Language for output.")
    parser.add_argument("--preset", choices=tuple(PRESETS.keys()) + ("3.14",), help="Preset configuration (use 3.14 for the easter egg).")
    parser.add_argument("--j-to-electric", type=float, help="Joule to electric efficiency (0-1).")
    parser.add_argument("--one-usage-efficiency", type=float, help="One usage efficiency (0-1).")
    parser.add_argument("--long-term-efficiency", type=float, help="Long term efficiency (0-1).")
    parser.add_argument("--device-name", help="Device name used for output.")
    parser.add_argument("--watt", type=float, help="Device watt value.")
    parser.add_argument("--accept-warning", action="store_true", help="Confirm that you have read the warning text.")
    parser.add_argument("--interactive", action="store_true", help="Launch the interactive prompts.")
    return parser.parse_args(argv)


def main(argv: Optional[list] = None) -> int:
    args = _parse_args(argv)

    if args.interactive or args.mass is None:
        return _interactive_flow()

    if not args.accept_warning:
        print(WARNING_TEXT)
        print("Re-run the command with --accept-warning after reading the warning.")
        return 1

    if args.mass <= 0:
        print("Mass must be greater than 0.")
        return 1

    try:
        config = _build_config(
            args.lang,
            args.preset,
            args.j_to_electric,
            args.one_usage_efficiency,
            args.long_term_efficiency,
            args.device_name,
            args.watt,
        )
    except ValueError as exc:
        print(str(exc))
        return 1

    data = _perform_calculations(args.mass, config)
    _print_results(args.lang, data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
