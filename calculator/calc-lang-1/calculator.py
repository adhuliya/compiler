#!/usr/bin/env python3
"""
Run this module to start using the calculator.
This is the driver program for the calculator.
"""

import os
import parser
import vm


p = parser.Parser()
v = vm.VM()

def main():
    line = None
    err = None # reads the error (if any) returned from methods...
    val = None # the value to print

    while True:
        line = None
        targetprogram = None
        err = None # reads the error (if any) returned from methods...
        val = None # the value to print

        try:
            line = input(os.linesep + ">>> ")
        except EOFError:
            break

        ok, val, err = calculate(line)
        if not ok: continue

        if err: 
            print(err)
            continue

        if val:
            print(val)

def calculate(line):
    targetprogram = None
    err = None # reads the error (if any) returned from methods...
    val = None # the value to print

    # if line is blank return False 
    if not line.strip(): return False, None, None

    targetprogram, err = p.parse(line)
    if err: return True, None, err

    # print("Target Program:",  targetprogram)

    val, err = v.calculate(targetprogram)
    if err: return True, None, err

    return True, val, None


if __name__ == '__main__':
    main()
