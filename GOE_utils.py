import numpy as np
import numba as nb
import pickle

VERBOSE = 0

@nb.njit()
def CH4_flux(tn, FCH4_mean, amplitude, period_s):
    return FCH4_mean + amplitude*np.sin(2*np.pi*tn/(period_s))
    
def make_cfunc(FCH4_mean, amplitude, period_s):
    @nb.cfunc(nb.types.double(nb.types.double))
    def CH4_flux_cfunc(tn):
        return CH4_flux(tn, FCH4_mean, amplitude, period_s) 
    return CH4_flux_cfunc
    
def oscillate(pc, initial, amplitude, period, filename, rtol = 1e-3, atol = 1e-30):
    pc.vars.verbose = VERBOSE
    pc.set_lbound('O2',2)
    pc.set_lbound('CH4',2)
    pc.set_surfflux('O2',initial['FO2'])
    FCH4 = initial['FCH4_FO2']*initial['FO2']
    pc.set_surfflux('CH4',FCH4)
    pc.vars.equilibrium_time=1e13
    pc.integrate(10000,method='CVODE_BDF',atol=1e-30)
    pc.out2in()
    
    yr = 365*24*60*60
    period_s = period*yr
    
    CH4_flux_cfunc = make_cfunc(FCH4, amplitude, period_s)
    
    ind = pc.ispec.index('CH4')
    pc.vars.lbound[ind] = 10
    pc.vars.lbound_ptrs[ind] = CH4_flux_cfunc.address 

    teval = np.linspace(0,3*period*yr,600)
    t0 = 0.0
    pc.evolve(t0,pc.vars.usol_init,teval,atol=atol,rtol=rtol,outfile=filename, \
    nsteps = 1000000, amount2save=1)

def GOE(pc, initial, final, filename, rtol = 1e-3, atol = 1e-30, nt = 1000, t_eval = None):
    pc.vars.verbose = VERBOSE
    pc.set_lbound('O2',2)
    pc.set_lbound('CH4',2)
    pc.set_surfflux('O2',initial['FO2'])
    pc.set_surfflux('CH4',initial['FCH4_FO2']*initial['FO2'])
    pc.vars.equilibrium_time=1e13
    pc.integrate(10000,method='CVODE_BDF',atol=1e-30)
    pc.out2in()
    
    pc.set_surfflux('O2',final['FO2'])
    pc.set_surfflux('CH4',final['FCH4_FO2']*final['FO2'])
    if type(t_eval) != np.ndarray:
        teval = np.logspace(5,14,nt)
    else:
        teval = t_eval
    t0 = 0.0
    pc.evolve(t0,pc.vars.usol_init,teval,atol=atol,rtol=rtol,outfile=filename, \
    nsteps = 100000, amount2save=1)


def get_sweep_results(foldername, ratios = None):

    if ratios == None:
        ratios = np.arange(.50,.260,-.005)

    FCH4_FO2 = []
    FO2 = []
    O2 = []
    CH4 = []
    FCH4 = []
    O3column = []
    S8 = []
    redox_column = []

    for i, ratio in enumerate(ratios):
        fil = open(foldername+'/'+'%.3f'%ratio+'.pkl','rb')
        zahnle = pickle.load(fil)
        fil.close()

        for j in range(len(zahnle['FO2'])):
            if zahnle['message'][j] == 'success':
                FCH4_FO2.append(ratio)
                FO2.append(zahnle['FO2'][j])
                O2.append(zahnle['O2'][j])
                FCH4.append(zahnle['FO2'][j]*ratio)
                CH4.append(zahnle['CH4'][j])
                S8.append(zahnle['S8_dep'][j])
                redox_column.append(zahnle['redox_column'][j])

    FCH4_FO2 = np.array(FCH4_FO2)
    FO2 = np.log10(FO2)
    O2 = np.log10(O2)
    FCH4 = np.log10(FCH4)
    CH4 = np.log10(CH4)
    S8 = -np.array(S8)
    S8 = np.log10(np.clip(S8,1e-66,np.inf))
    redox_column = np.log10(np.array(redox_column))
    
    return FCH4_FO2, FO2, O2, FCH4, CH4, S8, redox_column