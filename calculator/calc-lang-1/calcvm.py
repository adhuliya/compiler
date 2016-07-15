"""
This is the VM on which the compiled calculator code runs and gives the results.
"""


class CalcVM:
    def __init__(self):
        self.vars = dict()  # user defined vars (also the special '_' variable)
        self.inbuilt = dict()   # inbuilt functions : (min, max) no. of parameters

        self.vars['_'] = 0.0

        # add inbuilt functions

        self.inbuilt['sin'] = (1, 1)
        self.inbuilt['cos'] = (1, 1)
        self.inbuilt['tan'] = (1, 1)
        self.inbuilt['abs'] = (1, 1)
        self.inbuilt['round'] = (1,2)
