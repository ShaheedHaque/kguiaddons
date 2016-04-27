#!/usr/bin/env python
#-*- coding: utf-8 -*-

from __future__ import print_function

import sys

sys.path.append(sys.argv[1])

from PyQt5 import QtCore
from PyQt5 import QtGui

from PyKF5 import KGuiAddons

def main():
    app = QtGui.QGuiApplication(sys.argv)

    kdv = KGuiAddons.KDateValidator()
    num = 0

    l = QtCore.QLocale()

    assert(kdv.validate("NotADate")[0] == QtGui.QValidator.Intermediate)
    assert(kdv.validate("12/28/15")[0] == QtGui.QValidator.Acceptable)

if __name__ == '__main__':
    sys.exit(main())
