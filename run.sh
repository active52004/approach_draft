#!/bin/bash

texFile="approach_draft"

pdflatex ${texFile}.tex 
makeindex ${texFile}.nlo -s nomencl.ist -o ${texFile}.nls
pdflatex ${texFile}.tex
