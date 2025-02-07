
A fast numerical algorithm for inferring relative ability from multi-entrant contest winning probabilities. 

Published in SIAM Journal on Quantitative Finance ([pdf](https://github.com/microprediction/winning/blob/main/docs/Horse_Race_Problem__SIAM_updated.pdf))
 
![](https://i.imgur.com/83iFzel.png) 

### Usage

We choose a performance density

    density = centered_std_density()

We set 'dividends', which are for all intents and purposes inverse probabilities

    dividends = [2,6,np.nan, 3]

The algorithm implies relative ability (i.e. how much to translate the performance distributions to match the winning probabilities). 

    abilities = dividend_implied_ability(dividends=dividends,density=density, nan_value=2000)

Horses with no bid are assigned odds of nan_value ... or you can leave them out of course. 

### Generality

The density is just a vector representing an atomic distribution supported on the natural numbers. Thus it can approximate any performance distribution you desire. 

### Plotting.  

Its a good idea to plot, to ensure you haven't fallen of the grid. 

    L = 600
    unit = 0.01
    density = centered_std_density(L=L, unit=unit)
    dividends = [2,6,np.nan, 3]
    abilities = dividend_implied_ability(dividends=dividends,density=density, nan_value=2000, unit=unit)
    densities = [skew_normal_density(L=L, unit=unit, loc=a, a=0, scale=1.0) for a in abilities]
    legend = [ str(d) for d in dividends ]
    densitiesPlot(densities=densities, unit=unit, legend=legend)
    plt.show()

![](https://i.imgur.com/tYsrAWY.png)

### Pricing show and place from win prices:

    from winning.lattice_pricing import skew_normal_simulation
    from pprint import pprint
    dividends = [2.0,3.0,12.0,12.0,24.0,24.0]
    pricing = skew_normal_simulation(dividends=dividends,longshot_expon=1.15,skew_parameter=1.0,nSamples=1000)
    pprint(pricing)

### Practical use

See the  [paper](https://github.com/microprediction/winning/blob/main/docs/Horse_Race_Problem__SIAM_.pdf) for why this is useful in lots of places, according to a wise man. For instance, the algorithm may also find use anywhere winning probabilities or frequencies are apparent, such as with e-commerce product placement, in web search, or, as is shown in the paper: addressing a fundamental problem of trade. 

### Cite

    
        @article{doi:10.1137/19M1276261,
        author = {Cotton, Peter},
        title = {Inferring Relative Ability from Winning Probability in Multientrant Contests},
        journal = {SIAM Journal on Financial Mathematics},
        volume = {12},
        number = {1},
        pages = {295-317},
        year = {2021},
        doi = {10.1137/19M1276261},
        URL = { 
                https://doi.org/10.1137/19M1276261
        },
        eprint = { 
                https://doi.org/10.1137/19M1276261
        }
        }

### Introduction and nomenclature.

The lattice_calibration module allows the user to infer relative abilities from state prices in a multi-entrant contest. The assumption
made is that the performance distribution of one competitor is a translation of the performance distribution of another. The algorithm is:

- Fast 
- Scalable ... to contests with hundreds of thousands of entrants.
- General ... as noted it works for any performance distribution. 

The paper explains why it is useful beyond the racetrack, though the code is written with some racing vocabularly. At the racetrack, this would mean looking at the win odds and interpreting them as a relative ability. Here's a quick glossary to help with reading the code. It's a mix of financial and racetrack lingo. 

- *State prices* The expectation of an investment that has a payoff equal to 1 if there is only one winner, 1/2 if two are tied, 1/3 if three are tied and so forth. State prices are synomymous with winning probability, except for dead heats. However in the code a lattice is used so dead-heats must be accomodated and the distinction is important. 

- (Relative) *ability* refers to how much one performance distribution needs to be 
translated in order to match another. Implied abilities are vectors of relative abilities consistent with a collection of state prices.

- *Dividends* are the inverse of state prices. This is Australian tote vernacular. Dividends are called 'decimal odds' in the UK and that's probably a better name. A dividend of 9.0 corresponds to a state price of 1/9.0, and a bookmaker quote of 8/1. Don't ask me to translate to American odds conventions because they are so utterly ridiculous!      


### A little sugar on top

The core algorithm is entirely ambivalent to the choice of performance distribution, and that certainly need not correspond to some analytic distribution with known properties. However, if you just want to use skew_normal say:

- std_calibration module. 
- skew_calibration module.  

See the examples_basic for a gentle introduction. 
