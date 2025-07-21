import click
import sys
import emcalc

@click.command()
@click.option('--mass', default=1000, help='Mass in grams')
@click.option('--j-to-electric', default=0.35, help='Joule to electric efficiency (0-1)')
@click.option('--one-usage-efficiency', default=0.001, help='One usage efficiency (0-1)')
@click.option('--long-term-efficiency', default=0.90, help='Long term efficiency (0-1)')
@click.option('--device-name', default='led', help='Device name')
@click.option('--watt', default=10, help='Device power in watts')
def main(mass, j_to_electric, one_usage_efficiency, long_term_efficiency, device_name, watt):
    """Calculate energy conversion and device runtime from mass."""
    kg = emcalc.grams_to_kg(mass)
    theoretical_energy = emcalc.calculate_theoretical_energy(kg)
    long_term_practical_energy = emcalc.calculate_practical_energy(theoretical_energy, long_term_efficiency)
    one_usage_practical_energy = emcalc.calculate_practical_energy(theoretical_energy, one_usage_efficiency)
    long_term_electric_energy = emcalc.convert_joules_to_electricity(long_term_practical_energy, j_to_electric)
    one_usage_time_seconds = emcalc.calculate_led_on_time_seconds(one_usage_practical_energy, watt)
    one_usage_time_hours = one_usage_time_seconds / 3600

    print("\n--- RESULTS ---")
    print(f"Long term practical energy (at {long_term_efficiency:.2f} efficiency): {long_term_practical_energy:.0f} Joules")
    print(f"One usage practical energy (at {one_usage_efficiency:.3f} efficiency): {one_usage_practical_energy:.0f} Joules")
    print(f"Theoretical energy (at 100% efficiency): {theoretical_energy:.0f} Joules")
    print("-" * 20)
    print(f"With the electricity generated from this energy, a {watt}-watt {device_name}:")
    print(f"Can run for approximately {one_usage_time_seconds:.0f} seconds.")
    print(f"(This is approximately {one_usage_time_hours:.0f} hours.)")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        with click.Context(main) as ctx:
            print(main.get_help(ctx))
    else:
        main()