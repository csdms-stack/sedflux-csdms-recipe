#! /usr/bin/env python
import os

os.mkdir('_testing')
os.chdir('_testing')

from pymt.babel import setup_babel_environ
from pymt.framework.bmi_bridge import bmi_factory

setup_babel_environ()
for k, v in os.environ.items():
    print('{k}: {v}'.format(k=k, v=v))

print('import csdms')
import csdms

print('import Sedgrid')
import csdms.Sedgrid

print('from csdms.Sedgrid import Sedgrid')
from csdms.Sedgrid import Sedgrid

print('Sedgrid()')
Sedgrid()

print('bmi_factory(Sedgrid)')
bmi_factory(Sedgrid)

print('from pymt.components import Sedgrid as Model')
from pymt.components import Sedgrid as Model

print('Model()')
model = Model()


print('defaults')
for default in model.defaults:
    print('{name}: {val} {units}'.format(
        name=default[0], val=default[1][0], units=default[1][1]))
