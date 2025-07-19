c = 299792458
def _calte(kg):
    return kg * c**2
def _calpe(t_e, e):
    return t_e * e
one_usage_efficiency = 0.001
long_term_efficiency = float(input("long term efficiency:"))  # Düzeltildi
kg = float(input("kg: "))
theoretical_energy = _calte(kg)
long_term_practical_energy = _calpe(theoretical_energy, long_term_efficiency)
one_usage_practical_energy = _calpe(theoretical_energy, one_usage_efficiency)
print("\nRESULTS:")
print(f"Long term practical energy: efficiency:{long_term_efficiency:.2f}%  Joule:{long_term_practical_energy:.0f} ")
print(f"One usage practical energy: efficiency:{one_usage_efficiency:.3f}% Joule: {one_usage_practical_energy:.0f}")  # Düzeltildi
print(f"Theoretical energy efficiency:100 (1.0)% Joule: {theoretical_energy:.0f} ")
input()