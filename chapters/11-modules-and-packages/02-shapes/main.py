# import models

# r = models.Rectangle(2, 3)
# area_r = r.area()

# p = models.Rectangle(5, 6)
# p.print_area()

# models.folan()

# ----------------------------------

# from asghar.models import Rectangle, folan
# from asghar.db import folan as folan2

# r = Rectangle(2, 3)
# area_r = r.area()

# p = Rectangle(5, 6)
# p.print_area()

# folan()
# folan2()

# ----------------------------------

# from models import *
# from db import *

# r = Rectangle(2, 3)
# area_r = r.area()

# p = Rectangle(5, 6)
# p.print_area()

# folan()

# ---------------------------------

import asghar.models as m
from asghar.db import folan as folan2 


r = m.Rectangle(2, 3)
area_r = r.area()

p = m.Rectangle(5, 6)
p.print_area()

m.folan()
folan2()
