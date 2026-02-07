import my_module
print(my_module.a)
print(my_module.area_of_square(4))


#another method

import my_module as m
print(m.a)
print(m.area_of_square(4))

# I want to import specific function

from my_module import calculator
calculator(3,2)

from my_module import calculator as c,a
c(4,5)
print(a)

from my_module import * #for all
c(4,5)
print(a)