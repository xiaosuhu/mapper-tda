

import sys, os
import params
import pathlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../mapper')))
#sys.path.append('../mapper')


from mapper import em
from mapper import ff
from mapper import slc
from mapper.em_help import *
from em_3d_help import *




mkdir_p(params.PLOT_PATH)


data = read_3d_obj(fname="/Users/xiaosuhu/Documents/Python/mapper-tda/tests/lion_data.npy", fname_obj="/Users/xiaosuhu/Documents/Python/mapper-tda/tests/lion-reference.obj")


plot_3d(data, fname='3dTEST.png')


foo = em.ExploreMapper(data, slc.SingleLinkageClustering, ff.EccentricityP)

