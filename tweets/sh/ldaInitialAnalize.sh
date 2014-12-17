#!/bin/bash

/usr/local/bin/lda -est -alpha 0.5 -beta 0.1 -ntopics 100 -nithers 1000 -twords 20 -dfile data/newdata.dat