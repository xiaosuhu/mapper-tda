import numpy as np
import sys,os
import params

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../mapper')))

from mapper import em
from mapper import ff
from mapper import slc
from mapper.em_help import *
from em_3d_help import *

mkdir_p(params.PLOT_PATH)

fname1="/Users/xiaosuhu/Documents/Python/mapper-tda/tests/spirals.npy"
data=np.load(fname1)
#data_reorg=np.column_stack((data[:,2], data[:,1], data[:,0]))
'''
fname2="/Users/xiaosuhu/Documents/Python/mapper-tda/tests/lion_data.npy"
datalion=np.load(fname2)
'''
plot_3d(data,fname='franktestsparial.png')
test=em.ExploreMapper(data,slc.NNC,ff.AxisProj)

