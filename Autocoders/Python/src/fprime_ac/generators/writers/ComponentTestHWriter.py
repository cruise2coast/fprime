#!/bin/env python
#===============================================================================
# NAME: ComponentTestHWriter.py
#
# DESCRIPTION: A writer for generating component test header files
#
# AUTHOR: Jordan Ishii
# EMAIL:  jordan.ishii@jpl.nasa.gov
# DATE CREATED  : July 8, 2019
#
# Copyright 2015, California Institute of Technology.
# ALL RIGHTS RESERVED. U.S. Government Sponsorship acknowledged.
#===============================================================================

from fprime_ac.generators.writers import TestWriterBase
from fprime_ac.generators.templates.test import hpp

class ComponentTestHWriter(TestWriterBase.TestWriterBase):
    """
    A writer for generating component test header files.
    """

    def __init__(self):
        self.initBase("ComponentTestH")

    def emitHppParams(self, params):
        return self.emitNonPortParamsHpp(10, params)

    def emitHppPortParams(self, params):
        return self.emitPortParamsHpp(10, params)

    def initFilesWrite(self, obj):
        self.openFile("TesterBase.hpp")

    def startSourceFilesWrite(self, obj):
        c = hpp.hpp()
        self.initTest(obj, c)
        c.emit_hpp_params = self.emitHppParams
        c.emit_hpp_port_params = self.emitHppPortParams
        c.param_maxHistorySize = (
            "maxHistorySize",
            "const U32",
            "The maximum size of each history"
        )
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
