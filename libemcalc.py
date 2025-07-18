from scipy.constants import c

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
if __name__ == "__main__":
    import time
    print("licansed under the GNU General Public License v3.0"
          " (https://www.gnu.org/licenses/gpl-3.0.en.html)")
    
    exit()