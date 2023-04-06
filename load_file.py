# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:54:49 2023

@author: gianm
"""

import time
startTime0 = time.time()

import femm 
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import csv
from matplotlib import rc

mpl.rcParams["text.usetex"] = True

femm.openfemm() 
femm.opendocument('C:\\femm42\\examples\\LM_laboratorio_1_cava_chiusa.fem')
#femm.mi_analyze()

npt =60
bx = 0
by = 0 

shiftangle = 60/npt

#femm.mi_moverotate(bx, by, shiftangle)

#femm.mi_analyze()

#shiftangle = np.arange(360)
shiftangle = np.ones(npt)*60/npt # np.linspace(0,60,npt)

with open('C:\\Users\\gianm\\OneDrive\\Desktop\\Università 📚\\progetto fem\\femm_flux_linkage.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for alpha in shiftangle:
        
        femm.mi_selectgroup(2)
        femm.mi_moverotate(bx, by, alpha)
        femm.mi_clearselected()
        
        femm.mi_analyze()
        
        femm.mi_loadsolution()
        
        writer.writerow([femm.mo_getcircuitproperties('phase_1')[2] , femm.mo_getcircuitproperties('phase_2')[2] , femm.mo_getcircuitproperties('phase_3')[2] ])




    
    
    