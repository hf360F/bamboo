'''
Subscripts:
    0 - Stagnation condition
    c - Chamber condition (should be the same as stagnation conditions)
    t - At the throat
    e - At the nozzle exit plane
    amb - Atmopsheric/ambient condition
'''
import bamboo as bam
import numpy as np
import time
import matplotlib.pyplot as plt

'''Gas properties - obtained from ProPEP 3'''
gamma = 1.264               #Ratio of specific heats cp/cv
molecular_weight = 21.627   #Molecular weight of the exhaust gas (kg/kmol) (only used to calculate R, and hence cp)

'''Chamber conditions'''
pc = 10e5           #Chamber pressure (Pa)
Tc = 2458.89        #Chamber temperature (K) - obtained from ProPEP 3
mdot = 4.757        #Mass flow rate (kg/s)
p_amb = 1.01325e5   #Ambient pressure (Pa). 1.01325e5 is sea level atmospheric.

'''Create the engine object'''
perfect_gas = bam.PerfectGas(gamma = gamma, molecular_weight = molecular_weight)
chamber = bam.ChamberConditions(pc, Tc, mdot)
nozzle = bam.Nozzle.from_engine_components(perfect_gas, chamber, p_amb, type = "rao", length_fraction = 0.8)
engine = bam.Engine(perfect_gas, chamber, nozzle)

print(nozzle)
print(f"Sea level thrust = {engine.thrust(1e5)/1000} kN")
print(f"Sea level Isp = {engine.isp(1e5)} s")

nozzle.plot_nozzle()
plt.show()

#Estimate apogee based on apprpoximate Martlet 4 vehicle mass and cross sectional area
'''
apogee_estimate = bam.estimate_apogee(dry_mass = 60, 
                                      propellant_mass = 50, 
                                      engine = engine, 
                                      cross_sectional_area = 0.03, 
                                      show_plot = False)

print(f"Apogee estimate = {apogee_estimate/1000} km")

#Run an optimisation program to change the nozzle area ratio, to maximise the apogee obtained (I'm not sure if this is working correctly right now).
engine.optimise_for_apogee(dry_mass = 60, propellant_mass = 50, cross_sectional_area = 0.03)

print(engine.nozzle)
'''