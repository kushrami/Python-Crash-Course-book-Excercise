#imports:

import module_8_16

module_8_16.print_profile('tesla','model s')
from module_8_16 import build_profile
build_profile('ferrari','956')
from module_8_16 import print_profile as fn
fn('suzuki','hatchback')

import module_8_16 as mn
mn.print_profile('kia','celtos')
from module_8_16 import *
module_8_16.print_profile("subaru",'i dont know')