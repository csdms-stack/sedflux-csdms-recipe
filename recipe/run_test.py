#! /usr/bin/env python
import os

os.mkdir('_testing')
os.chdir('_testing')

import csdms
import csdms.Sedgrid
from csdms.Sedgrid import Sedgrid

from pymt.components import Sedgrid as Model

model = Model()

for default in model.defaults:
    print('{name}: {val} {units}'.format(
        name=default[0], val=default[1][0], units=default[1][1]))
