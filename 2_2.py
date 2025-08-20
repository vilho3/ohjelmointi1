#"Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
import math
säde = float(input("anna ympyrän säde: "))
#ympyrän pinta-ala on pi r^2
ala = (math.pi)*säde**2
print(f"ympyrän pinta-ala on: {ala:.2f}")