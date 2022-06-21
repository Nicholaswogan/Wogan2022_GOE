from PhotochemPy import PhotochemPy
import numpy as np
from pathos.multiprocessing import ProcessingPool as Pool
from pathos import helpers

import GOE_utils as utils

def figure_2a():
    pc = PhotochemPy('Archean2Proterozoic/species_zahnle2006.dat', \
                     'Archean2Proterozoic/reactions_new.rx', \
                     'Archean2Proterozoic/settings.yaml', \
                     'Archean2Proterozoic/atmosphere_zahnle2006_FO2=1e12_CH4O2=0.490.txt', \
                     'Archean2Proterozoic/Sun_2.4Ga.txt')
    initial = {'FO2':1e12,'FCH4_FO2':0.49}
    final = {'FO2':1e12,'FCH4_FO2':0.47}
    filename = "ZAHNLE_start_FO2=1e12_0.49_end_FO2=1e12_0.47.dat"
    utils.GOE(pc, initial, final, filename, atol = 1e-29)
    
def figure_2b():
    pc = PhotochemPy('Archean2Proterozoic/species_case1_0.094_CO2=1%.dat', \
                     'Archean2Proterozoic/reactions_new.rx', \
                     'Archean2Proterozoic/settings.yaml', \
                     'Archean2Proterozoic/atmosphere_case1_0.450_CO2=1%_FO2=1e12.txt', \
                     'Archean2Proterozoic/Sun_2.4Ga.txt')
    initial = {'FO2':1e12,'FCH4_FO2':0.45}
    final = {'FO2':1.8e12,'FCH4_FO2':0.45}
    filename = "CASE1_start_FO2=1e12_0.45_end_FO2=1.8e12_0.45.dat"
    utils.GOE(pc, initial, final, filename, atol=1e-29)

def figure_2c():
    pc = PhotochemPy('Archean2Proterozoic/species_zahnle2006.dat', \
                     'Archean2Proterozoic/reactions_new.rx', \
                     'Archean2Proterozoic/settings.yaml', \
                     'Archean2Proterozoic/atmosphere_zahnle2006_FO2=1e12_CH4O2=0.490.txt', \
                     'Archean2Proterozoic/Sun_2.4Ga.txt')
    initial = {'FO2':1e12,'FCH4_FO2':0.49}
    final = {'FO2':1e12,'FCH4_FO2':0.45}
    filename = "ZAHNLE_start_FO2=1e12_0.49_end_FO2=1e12_0.45.dat"
    utils.GOE(pc, initial, final, filename, atol = 1e-29)
    
def figure_3a():
    pc = PhotochemPy('Archean2Proterozoic/species_zahnle2006.dat', \
                     'Archean2Proterozoic/reactions_new.rx', \
                     'Archean2Proterozoic/settings.yaml', \
                     'Archean2Proterozoic/atmosphere_zahnle2006_FO2=1e12_CH4O2=0.470.txt', \
                     'Archean2Proterozoic/Sun_2.4Ga.txt')
    initial = {'FO2':1e12,'FCH4_FO2':0.47}
    final = {'FO2':1e12,'FCH4_FO2':0.49}
    filename = "ZAHNLE_start_FO2=1e12_0.47_end_FO2=1e12_0.49.dat"
    utils.GOE(pc, initial, final, filename)
    
def figure_3b():
    pc = PhotochemPy('Archean2Proterozoic/species_case1_0.094_CO2=1%.dat', \
                     'Archean2Proterozoic/reactions_new.rx', \
                     'Archean2Proterozoic/settings.yaml', \
                     'Archean2Proterozoic/atmosphere_case1_0.450_CO2=1%_FO2=1.8e12.txt', \
                     'Archean2Proterozoic/Sun_2.4Ga.txt')
    initial = {'FO2':1.8e12,'FCH4_FO2':0.45}
    final = {'FO2':1e12,'FCH4_FO2':0.45}
    filename = "CASE1_start_FO2=1.8e12_0.45_end_FO2=1e12_0.45.dat"
    utils.GOE(pc, initial, final, filename)
    
def figure_3c():
    pc = PhotochemPy('Archean2Proterozoic/species_zahnle2006.dat', \
                     'Archean2Proterozoic/reactions_new.rx', \
                     'Archean2Proterozoic/settings.yaml', \
                     'Archean2Proterozoic/atmosphere_zahnle2006_FO2=1e12_CH4O2=0.450.txt', \
                     'Archean2Proterozoic/Sun_2.4Ga.txt')
    initial = {'FO2':1e12,'FCH4_FO2':0.45}
    final = {'FO2':1e12,'FCH4_FO2':0.49}
    filename = "ZAHNLE_start_FO2=1e12_0.45_end_FO2=1e12_0.49.dat"
    utils.GOE(pc, initial, final, filename)

def figure_4b():
    pc = PhotochemPy('Archean2Proterozoic/species_zahnle2006.dat', \
                     'Archean2Proterozoic/reactions_new.rx', \
                     'Archean2Proterozoic/settings.yaml', \
                     'Archean2Proterozoic/atmosphere_zahnle2006_FO2=3.1e11_CH4O2=0.47.txt', \
                     'Archean2Proterozoic/Sun_2.4Ga.txt')
    initial = {'FO2':3.1e11,'FCH4_FO2':0.48}
    amplitude = 2.5e10
    period = 1e4
    filename = "ZAHNLE_FO2=3.100e+11_oscillate_0.480_amp=2.5e10_T=1e4yr.dat" 
    utils.oscillate(pc, initial, amplitude, period, filename)
    
def figure_4c():
    pc = PhotochemPy('Archean2Proterozoic/species_zahnle2006.dat', \
                     'Archean2Proterozoic/reactions_new.rx', \
                     'Archean2Proterozoic/settings.yaml', \
                     'Archean2Proterozoic/atmosphere_zahnle2006_FO2=3.1e11_CH4O2=0.45.txt', \
                     'Archean2Proterozoic/Sun_2.4Ga.txt')
    initial = {'FO2':3.1e11,'FCH4_FO2':0.45}
    amplitude = 0.7e10
    period = 1e4
    filename = "ZAHNLE_FO2=3.100e+11_oscillate_0.450_amp=0.7e10_T=1e4yr.dat" 
    utils.oscillate(pc, initial, amplitude, period, filename)
    
def figure_4d():
    pc = PhotochemPy('Archean2Proterozoic/species_zahnle2006.dat', \
                     'Archean2Proterozoic/reactions_new.rx', \
                     'Archean2Proterozoic/settings.yaml', \
                     'Archean2Proterozoic/atmosphere_zahnle2006_FO2=3.1e11_CH4O2=0.43.txt', \
                     'Archean2Proterozoic/Sun_2.4Ga.txt')
    initial = {'FO2':3.1e11,'FCH4_FO2':0.41}
    amplitude = 2.5e10
    period = 1e4
    filename = "ZAHNLE_FO2=3.100e+11_oscillate_0.410_amp=2.5e10_T=1e4yr.dat" 
    utils.oscillate(pc, initial, amplitude, period, filename)
    
def figure_S3():
    pc = PhotochemPy('Archean2Proterozoic/species_zahnle2006.dat', \
                     'Archean2Proterozoic/reactions_new.rx', \
                     'Archean2Proterozoic/settings.yaml', \
                     'Archean2Proterozoic/atmosphere_zahnle2006_FO2=3.1e11_CH4O2=0.44.txt', \
                     'Archean2Proterozoic/Sun_2.4Ga.txt')
    initial = {'FO2':3.1e11,'FCH4_FO2':0.44}
    
    pc.set_lbound('O2',2)
    pc.set_lbound('CH4',2)
    pc.set_surfflux('O2',initial['FO2'])
    pc.set_surfflux('CH4',initial['FCH4_FO2']*initial['FO2'])
    pc.vars.equilibrium_time=1e13
    pc.integrate(10000,method='CVODE_BDF',atol=1e-30)
    pc.out2in()
    
    yr = 365*24*60*60
    filename = "ZAHNLE_start_FO2=3.1e11_0.44_end_FH2=1.9e11_FCO=2e10.dat" 
    
    pc.set_surfflux('H2', 1.9e11)
    pc.set_surfflux('CO', 2e10)
    
    teval = np.logspace(5,14,1000)
    t0 = 0.0
    pc.evolve(t0,pc.vars.usol_init,teval,atol=1e-29,rtol=1e-3,outfile=filename, \
    nsteps = 100000, amount2save=1)
    
if __name__ == "__main__":
    # runs all simulations in parallel
    
    utils.VERBOSE = 1
    
    def wrap(fun):
        fun()

    simulations = [figure_2a, figure_2b, figure_2c, \
                   figure_3a, figure_3b, figure_3c, \
                   figure_4b, figure_4c, figure_4d, \
                   figure_S3]
                   
    p = Pool(helpers.cpu_count())
    p.map(wrap,simulations)
    
    