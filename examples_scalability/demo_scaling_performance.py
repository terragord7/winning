from winning.lattice_plot import  densitiesPlot
from winning.lattice import skew_normal_density, mean_of_density, implicit_state_prices, winner_of_many, sample_winner_of_many
from winning.lattice_calibration import implied_ability, state_prices_from_offsets, densities_from_offsets
import numpy as np
PLOTS=True
import math
import time

unit = 0.01
L = 500

def demo(  ):
    density                 = skew_normal_density(L=500, unit = unit, a=1.5)

    cpu_times = list()
    errors = list()
    race_sizes = [10,25,50,100,200,400,800,1600,3200,6400,10000,20000,40000,80000]
    for k,n in enumerate(race_sizes):
        print(n)
        true_offsets            = [ int(unit*k) for k in range( n ) ]
        state_prices            = state_prices_from_offsets( density=density, offsets=true_offsets )
        print("State prices are " + str( state_prices ))
        offset_samples          = list( range( -100, 100 ))[::-1]
        # Now try to infer offsets from state prices
        start_time = time.time()
        implied_offsets         = implied_ability( prices = state_prices, density = density, offset_samples= offset_samples, nIter=5)
        cpu_times.append(time.time()-start_time)
        recentered_offsets      = [ io-implied_offsets[0] for io in implied_offsets]
        differences             = [ o1-o2 for o1, o2 in zip(recentered_offsets,true_offsets)]
        avg_l1_in_offset        = np.mean(np.abs( differences ))
        errors.append( avg_l1_in_offset)
        print(avg_l1_in_offset)
        print(cpu_times)
        log_cpu = [math.log(cpu) for cpu in cpu_times]
        log_n   = [math.log(n_) for n_ in race_sizes[:k+1]]
        if k>=2:
            print('Fitting ...')
            print(np.polyfit(log_n, log_cpu, 1))


    import matplotlib.pyplot as plt
    plt.clf()
    plt.scatter(race_sizes[:k+1],cpu_times)
    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('Number of participants (n)')
    plt.ylabel('Inversion time in seconds')
    plt.show()

if __name__=='__main__':
    demo()
