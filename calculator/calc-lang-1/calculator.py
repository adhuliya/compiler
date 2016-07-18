#!/usr/bin/env python3
"""
Run this module to start using the calculator.
This is the driver program for the calculator.
"""

import os
import parser
import vm


def main():
    line = None
    targetprogram = None
    err = None # reads the error (if any) returned from methods...
    val = None # the value to print

    p = parser.Parser()
    v = vm.VM()

    while True:
        line = None
        targetprogram = None
        err = None # reads the error (if any) returned from methods...
        val = None # the value to print

        try:
            line = input(os.linesep + ">>> ")
            if not line.strip(): continue
        except EOFError:
            break

        targetprogram, err = p.parse(line)
        if err:
            print(err)
            continue

        print("Target Program:",  targetprogram)

        val, err = v.calculate(targetprogram)
        if err: 
            print(err)
            continue

        if val:
            print(val)



if __name__ == '__main__':
    main()
