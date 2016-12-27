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

    l = QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedKingdom)
    kdv.setLocale(l)

    assert(kdv.validate("NotADate")[0] == QtGui.QValidator.Intermediate)
    assert(kdv.validate("28/12/2015")[0] == QtGui.QValidator.Acceptable)

if __name__ == '__main__':
    sys.exit(main())
