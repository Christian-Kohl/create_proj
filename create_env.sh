#!/bin/bash

cd ~/Documents/Projects/$1
ECTORY="${1}_env"
virtualenv $ECTORY

. $ECTORY/bin/activate

pip3 install numpy
pip3 install sklearn
pip3 install pandas
deactivate
