"""
This is the VM on which the compiled calculator code runs and gives the results.
"""

class VM:
    def __init__(self):
        self.vars = dict()  # user defined vars (also the special '_' variable)
        self.inbuilt = dict()   # inbuilt functions : (min, max) no. of parameters
        self.operators = set()  # set of operators supported
        self.stack = []

        self.vars['_'] = 0.0

        # add inbuilt functions

        self.inbuilt['sin'] = (1, 1)
        self.inbuilt['cos'] = (1, 1)
        self.inbuilt['tan'] = (1, 1)
        self.inbuilt['abs'] = (1, 1)
        self.inbuilt['round'] = (1,2)
        self.inbuilt['max'] = (1, 0) # 0 = unlimited

        self.operators.add('+')
        self.operators.add('-')
        self.operators.add('*')
        self.operators.add('/')
        self.operators.add('%')
        self.operators.add('**')

        self.operators.add('=')
        self.operators.add('+=')
        self.operators.add('-=')
        self.operators.add('*=')
        self.operators.add('/=')
        self.operators.add('%=')
        self.operators.add('**=')


    
    def calculate(self, vmprogram):
        """
        Takes a vmprogram as input and returns the final value
        and error if any.

        Ouput: value, error
        """
        self.stack = [] # start with a fresh stack

        value = None
        error = None

        for elem in vmprogram:
            if elem in self.inbuilt or elem in self.operators:
                value, error = self.operate(elem)
                if error != None:
                    return value, error
                self.stack.append(value)
            else:
                self.stack.append(elem)


        # Return the value of the last element 
        # and set the special variable '_' to it.
        # report errors if the last value is not a 'float'
        if len(self.stack) == 1:
            elem = self.stack.pop()
            if type(elem) == float or type(elem) == int:
                self.vars['_'] = elem
                return elem, None
            else:
                error = "Expecting {} or {} found {} with value {}\nStack = {}".format(
                        float, int, type(elem), elem, self.stack)
                value = elem
                return value, error
        else:
            error = "Bad Stack. Stack = {}".format(self.stack)
            value = None
            return value, error


    def operate(self, elem):
        error = None
        if elem == '+':
            leftopr, error = self.topStackValue()
            if error != None: return None, error

            rightopr, error = self.topStackValue()
            if error != None: return None, error

            return rightopr + leftopr, None
        
        if elem == '-':
            leftopr, error = self.topStackValue()
            if error != None: return None, error

            rightopr, error = self.topStackValue()
            if error != None: return None, error

            return rightopr - leftopr, None

        if elem == '*':
            leftopr, error = self.topStackValue()
            if error != None: return None, error

            rightopr, error = self.topStackValue()
            if error != None: return None, error

            return rightopr * leftopr, None

        if elem == '/':
            leftopr, error = self.topStackValue()
            if error != None: return None, error

            rightopr, error = self.topStackValue()
            if error != None: return None, error

            if leftopr == 0.0:
                return None, "Division by zero! Stack = {}".format(self.stack)

            return rightopr / leftopr, None

        if elem == '**':
            leftopr, error = self.topStackValue()
            if error != None: return None, error

            rightopr, error = self.topStackValue()
            if error != None: return None, error

            return rightopr ** leftopr, None

        if elem == '=':
            leftopr, error = self.topStackValue()
            if error != None: return None, error

            rightopr = self.stack.pop()
            if type(rightopr) == str:
                self.vars[rightopr] = leftopr
                return leftopr, None
            else:
                return None, "lvalue required, got {}. Stack =".format(
                        rightopr, self.stack)

        if elem == '+=':
            leftopr, error = self.topStackValue()
            if error != None: return None, error

            rightopr = self.stack.pop()
            if type(rightopr) == str:
                if rightopr in self.vars:
                    self.vars[rightopr] = self.vars[rightopr] + leftopr
                    return self.vars[rightopr], None
                else:
                    return None, "Undefined variable {}".format(rightopr)
            else:
                return None, "lvalue required, got {}. Stack =".format(
                        rightopr, self.stack)

        if elem == 'abs':
            leftopr, error = self.topStackValue()
            if error != None: return None, error

            noneval, error = self.topStackValue()
            if error != None: return None, error

            if noneval != None:
                return None, "function:abs:Expecting None found {}".format(
                        noneval)

            return abs(leftopr), None



    def topStackValue(self):
        elem = self.stack.pop()
        if type(elem) == str:
            if elem in self.vars:
                return self.vars[elem], None
            else:
                return None, "Variable '{}' not defined, but used.".format(elem)
        else:
            return elem, None

if __name__ == '__main__':
    vm = VM()
    program = ['x', 20.0,'y','+', '=']
    print(program)
    val, err = vm.calculate(program)
    if err != None:
        print("Error:", err)
    print("Result:", val)

    program = [20.0,None, 'x','abs', '/']
    print(program)
    val, err = vm.calculate(program)
    if err != None:
        print("Error:", err)
    print("Result:", val)
