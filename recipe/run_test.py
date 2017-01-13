#! /usr/bin/env python
from __future__ import print_function

import os

os.mkdir('_testing')
os.chdir('_testing')

print('import csdms')
import csdms

print('import Sedgrid')
import csdms.Sedgrid

print('from csdms.Sedgrid import Sedgrid')
from csdms.Sedgrid import Sedgrid

print('Sedgrid()')
Sedgrid()

print('from pymt.components import Sedgrid as Model')
from pymt.components import Sedgrid as Model

print('Model()')
model = Model()

print('defaults')
for default in model.defaults:
    print('{name}: {val} {units}'.format(
        name=default[0], val=default[1][0], units=default[1][1]))
