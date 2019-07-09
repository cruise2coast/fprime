#!/bin/env python
#===============================================================================
# NAME: TestImplCppWriter.py
#
# DESCRIPTION: A writer class for generating test implementation cpp files.
#
# AUTHOR: Jordan Ishii
# EMAIL:  jordan.ishii@jpl.nasa.gov
# DATE CREATED: July 8, 2019
#
# Copyright 2015, California Institute of Technology.
# ALL RIGHTS RESERVED. U.S. Government Sponsorship acknowledged.
#===============================================================================

from fprime_ac.utils import ConfigManager

from fprime_ac.generators.templates.test_impl import cpp
from fprime_ac.generators.writers import TestImplWriterBase

class TestImplCppWriter(TestImplWriterBase.TestImplWriterBase):
    """
    A writer class for generating test implementation cpp files.
    """

    def __init__(self):
        self.initBase("TestImplCpp")

    def emitPortParams(self, params):
        return self.emitPortParamsCpp(8, params)

    def emitNonPortParams(self, params):
        return self.emitNonPortParamsCpp(8, params)

    def initFilesWrite(self, obj):
        self.openFile("Tester.cpp")

    def startSourceFilesWrite(self, obj):
        c = cpp.cpp()
        self.init(obj, c)
        self.initTestImpl(obj, c)
        c.emit_port_params = self.emitPortParams
        c.emit_non_port_params = self.emitNonPortParams
        self._writeTmpl(c, "startSourceFilesWrite")

    def write(self, obj):
        self.initFilesWrite(obj)
        self.startSourceFilesWrite(obj)
        self.includes1Write(obj)
        self.includes2Write(obj)
        self.namespaceWrite(obj)
        self.publicWrite(obj)
        self.protectedWrite(obj)
        self.privateWrite(obj)
        self.finishSourceFilesWrite(obj)
