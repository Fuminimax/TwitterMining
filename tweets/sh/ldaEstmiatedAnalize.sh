#!/bin/bash

lda -inf -dir ./data -model model-final -niters 1000 -twords 20 -dfile ../output/newdata.dat
