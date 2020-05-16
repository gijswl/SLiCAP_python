#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os

LOGFILE         = True
LANGUAGE        = 'english' # Language for error and warnings
DISP            = 4         # Numner of digits for floats in output

LAPLACE         = 's'       # Laplace veriable
FREQUENCY       = 'f'       # Frequency in Hz
OMEGA           = 'omega'   # Frequency in rad/s
MAXRECSUBST     = 10        # Maximum number of recursic=ve substitutions
HZ              = True      # True if frequency output in Hz, else: False

# PATHS: relative to the project directory
CIRCUITPATH     = 'cir/'      # path for .asc, .net, .cir, .sch files
LIBRARYPATH     = 'lib/'      # path for include and library files
TXTPATH         = 'txt/'      # path for text files (text2html)
CSVPATH         = 'csv/'      # path for CSV files (csv2html)
LATEXPATH       = 'tex/'      # path for LaTeX output saveTeX()
MATHMLPATH      = 'mathml/'   # path for mathML output saveMathML()

# Default plot settings
figureAxisHeight= 4
figureAxisWidth = 6
defaultColors   = ('r','b','g','c','m','y','k')
defaultMarkers  = ['']
tableFileType   = 'csv'
figureFileType  = 'svg'
axisXscale      = 'linear'    # Scale for the x-axis can be 'linear' or 'log'
axisYscale      = 'linear'    # Scale for the y-axis can be 'linear' or 'log'
legendLoc       = 'best'
SCALEFACTORS    =  {'y':'-24','z':'-21','a':'-18','f':'-15','p':'-12','n':'-9',
                    'u':'-6','m':'-3','k':'3','M':'6','G':'9','T':'12','P':'15',
                    'E':'18','Z':'21','Y':'24'}