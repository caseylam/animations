import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as ani

bh_dict = {}
# Table 1 of Remillard and McClintock 2006
# https://www.annualreviews.org/doi/10.1146/annurev.astro.44.051905.092532
# FIXME: ADD IN INFO FROM C&J14
# Tables 1 and 2 of Casares and Jonker 2014
# https://link.springer.com/article/10.1007%2Fs11214-013-0030-6
bh_dict['GRO_J0422+32'] = {'Year' : 1992, 'Mass' : 0.5 * (3.7 + 5.0), 'Method' : 'XRB'}
bh_dict['LMC_X–3'] = {'Year' : 0, 'Mass' : 0.5 * (5.9 + 9.2), 'Method' : 'XRB'}
bh_dict['LMC_X–1'] = {'Year' : 0, 'Mass' : 0.5 * (4.0 + 10.0), 'Method' : 'XRB'}
bh_dict['A0620–003'] = {'Year' : 1975 , 'Mass' : 0.5 * (8.7 + 12.9), 'Method' : 'XRB'}
bh_dict['GRS1009–45'] = {'Year' : 1993, 'Mass' : 0.5 * (3.6 + 4.7), 'Method' : 'XRB'}
bh_dict['XTE_J1118+480'] = {'Year' : 2000, 'Mass' : 0.5 * (6.5 + 7.2), 'Method' : 'XRB'}
bh_dict['Nova_Mus_91'] = {'Year' : 1991, 'Mass' : 0.5 * (6.5 + 8.2), 'Method' : 'XRB'}
bh_dict['GS1354–64'] = {'Year' : 1987, 'Mass' : 0, 'Method' : 'XRB'}
bh_dict['4U1543–475'] = {'Year' : 1971, 'Mass' : 0.5 * (8.4 + 10.4), 'Method' : 'XRB'}
bh_dict['XTE_J1550–564'] = {'Year' : 1998, 'Mass' : 0.5 * (8.4 + 10.8), 'Method' : 'XRB'}
bh_dict['XTE_J1650–500h'] = {'Year' : 2001, 'Mass' : 0, 'Method' : 'XRB'}
bh_dict['GRO_J1655–40'] = {'Year' : 1994, 'Mass' : 0.5 * (6.0 + 6.6), 'Method' : 'XRB'}
bh_dict['GX_339–4'] = {'Year' : 1972, 'Mass' : 0, 'Method' : 'XRB'}
bh_dict['Nova_Oph_77'] = {'Year' : 1977, 'Mass' : 0.5 * (5.6 + 8.3), 'Method' : 'XRB'}
bh_dict['V4641_Sgr'] = {'Year' : 1999, 'Mass' : 0.5 * (6.8 + 7.4), 'Method' : 'XRB'}
bh_dict['XTE_J1859+226'] = {'Year' : 1999, 'Mass' : 0.5 * (7.6 + 12.0), 'Method' : 'XRB'}
bh_dict['GRS1915+105'] = {'Year' : 1992, 'Mass' : 0.5 * (10.0 + 18.0) , 'Method' : 'XRB'}
bh_dict['Cyg_X–1'] = {'Year' : 0, 'Mass' : 0.5 * (6.8 + 13.3), 'Method' : 'XRB'}
bh_dict['GS2000+251'] = {'Year' : 1988, 'Mass' : 0.5 * (7.1 + 7.8), 'Method' : 'XRB'}
bh_dict['V404_Cyg'] = {'Year' : 1989, 'Mass' : 0.5 * (10.1 + 13.4), 'Method' : 'XRB'}

# Table III of Abbott+2019
# https://journals.aps.org/prx/abstract/10.1103/PhysRevX.9.031040
bh_dict['GW150914_1'] = {'Year' : 2015, 'Mass' : 35.6, 'Method' : 'LIGOpre'}
bh_dict['GW150914_2'] = {'Year' : 2015, 'Mass' : 30.6, 'Method' : 'LIGOpre'}
bh_dict['GW150914_M'] = {'Year' : 2015, 'Mass' : 63.1, 'Method' : 'LIGOpost'}
bh_dict['GW151012_1'] = {'Year' : 2015, 'Mass' : 23.2, 'Method' : 'LIGOpre'}
bh_dict['GW151012_2'] = {'Year' : 2015, 'Mass' : 13.6, 'Method' : 'LIGOpre'}
bh_dict['GW151012_M'] = {'Year' : 2015, 'Mass' : 35.6, 'Method' : 'LIGOpost'}
bh_dict['GW151226_1'] = {'Year' : 2015, 'Mass' : 13.7, 'Method' : 'LIGOpre'}
bh_dict['GW151226_2'] = {'Year' : 2015, 'Mass' : 7.7, 'Method' : 'LIGOpre'}
bh_dict['GW151226_M'] = {'Year' : 2015, 'Mass' : 20.5, 'Method' : 'LIGOpost'}
bh_dict['GW170104_1'] = {'Year' : 2017, 'Mass' : 30.8, 'Method' : 'LIGOpre'}
bh_dict['GW170104_2'] = {'Year' : 2017, 'Mass' : 20.0, 'Method' : 'LIGOpre'}
bh_dict['GW170104_M'] = {'Year' : 2017, 'Mass' : 48.9, 'Method' : 'LIGOpost'}
bh_dict['GW170608_1'] = {'Year' : 2017, 'Mass' : 11.0, 'Method' : 'LIGOpre'}
bh_dict['GW170608_2'] = {'Year' : 2017, 'Mass' : 7.6, 'Method' : 'LIGOpre'}
bh_dict['GW170608_M'] = {'Year' : 2017, 'Mass' : 17.8, 'Method' : 'LIGOpost'}
bh_dict['GW170729_1'] = {'Year' : 2017, 'Mass' : 50.2, 'Method' : 'LIGOpre'}
bh_dict['GW170729_2'] = {'Year' : 2017, 'Mass' : 34.0, 'Method' : 'LIGOpre'}
bh_dict['GW170729_M'] = {'Year' : 2017, 'Mass' : 79.5, 'Method' : 'LIGOpost'}
bh_dict['GW170809_1'] = {'Year' : 2017, 'Mass' : 35.0, 'Method' : 'LIGOpre'}
bh_dict['GW170809_2'] = {'Year' : 2017, 'Mass' : 23.8, 'Method' : 'LIGOpre'}
bh_dict['GW170809_M'] = {'Year' : 2017, 'Mass' : 56.3, 'Method' : 'LIGOpost'}
bh_dict['GW170814_1'] = {'Year' : 2017, 'Mass' : 30.6, 'Method' : 'LIGOpre'}
bh_dict['GW170814_2'] = {'Year' : 2017, 'Mass' : 25.2, 'Method' : 'LIGOpre'}
bh_dict['GW170814_M'] = {'Year' : 2017, 'Mass' : 53.2, 'Method' : 'LIGOpost'}
bh_dict['GW170818_1'] = {'Year' : 2017, 'Mass' : 35.4, 'Method' : 'LIGOpre'}
bh_dict['GW170818_2'] = {'Year' : 2017, 'Mass' : 26.7, 'Method' : 'LIGOpre'}
bh_dict['GW170818_M'] = {'Year' : 2017, 'Mass' : 59.4, 'Method' : 'LIGOpost'}
bh_dict['GW170823_1'] = {'Year' : 2017, 'Mass' : 39.5, 'Method' : 'LIGOpre'}
bh_dict['GW170823_2'] = {'Year' : 2017, 'Mass' : 29.0, 'Method' : 'LIGOpre'}
bh_dict['GW170823_M'] = {'Year' : 2017, 'Mass' : 65.4, 'Method' : 'LIGOpost'}

years = np.arange(1960, 2030)
frames = []

fig = plt.figure()

for yy in years:
    bh_list = [bh for bh in bh_dict if bh_dict[bh]['Year'] < yy]
    bh_mass = [bh_dict[bh]['Mass'] for bh in bh_list]
    bh_year = [bh_dict[bh]['Year'] for bh in bh_list]
    frame = plt.plot(bh_mass, bh_year, 'k.')
    frames.append(frame)

plt.xlim(0, 100)
plt.ylim(years[0], years[-1])

boop = ani.ArtistAnimation(fig, frames)        

boop 

            
