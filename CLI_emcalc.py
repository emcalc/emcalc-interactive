import sys
import click
import emcalc

@click.command()
@click.option('--preset', default='1', prompt=emcalc.Presets, type=str, help='Select a preset for the calculation.')
@click.option('--mass', default=1000, prompt='Enter mass in grams', type=float, help='Mass in grams for the calculation.')
@click.pass_context
def main(ctx, preset, mass):
    if len(sys.argv) == 1:
        click.echo(ctx.get_help())
        ctx.exit()
    if preset == "1":
        j_to_electric = 0.33
        one_usage_efficiency = 0.001
        long_term_efficiency = 0.90
        device_name = "led"
        watt = 10
    elif preset == "2":
        j_to_electric = 0.31
        one_usage_efficiency = 0.001
        long_term_efficiency = 0.90
        device_name = "led"
        watt = 10
    elif preset == "3":
        j_to_electric = 0.30
        one_usage_efficiency = 0.001
        long_term_efficiency = 0.85
        device_name = "led"
        watt = 10
    elif preset == "4":
        j_to_electric = 0.38
        one_usage_efficiency = 0.001
        long_term_efficiency = 0.93
        device_name = "led"
        watt = 10
    elif preset == "5":
        j_to_electric = 0.38
        one_usage_efficiency = 0.001
        long_term_efficiency = 0.92
        device_name = "led"
        watt = 10
    elif preset == "3.14" or preset == "3,14":
        emcalc.easter_egg()
        return
    else:
        j_to_electric = float(input("please input the jul to electric efficeny example for %5: 0.05 defualt is 0.35: "))
        one_usage_efficiency = float(input("please input the one usage efficieny example for %0.5: 0.005 defualt is 0.001: "))
        long_term_efficiency = float(input("please input the mass to Heat efficieny defualt 0.90: "))
        device_name = "led"
        watt = 10

    kg = emcalc.grams_to_kg(mass)
    theoretical_energy = emcalc.calculate_theoretical_energy(kg)
    long_term_practical_energy = emcalc.calculate_practical_energy(theoretical_energy, long_term_efficiency)
    one_usage_practical_energy = emcalc.calculate_practical_energy(theoretical_energy, one_usage_efficiency)
    long_term_electric_energy = emcalc.convert_joules_to_electricity(long_term_practical_energy, j_to_electric)
    one_usage_time_seconds = emcalc.calculate_led_on_time_seconds(one_usage_practical_energy, watt)
    one_usage_time_hours = one_usage_time_seconds / 3600

    print("\n--- RESULTS ---")
    print(f"Long term practical energy (at {long_term_efficiency:.2f}% efficiency): {long_term_practical_energy:.0f} Joules")
    print(f"One usage practical energy (at {one_usage_efficiency:.3f}% efficiency): {long_term_practical_energy:.0f} Joules")
    print(f"Theoretical energy (at 100% efficiency): {theoretical_energy:.0f} Joules")
    print("-" * 20)
    print(f"With the electricity generated from this energy, a {watt}-watt {device_name}:")
    print(f"Can run for approximately {one_usage_time_seconds:.0f} seconds.")
    print(f"(This is approximately {one_usage_time_hours:.0f} hours.)")
    
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("No arguments provided.\n")
        with click.Context(main) as ctx:
            print(main.get_help(ctx))
        sys.exit()
    main()