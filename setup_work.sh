#!/bin/bash

cd
cd Documents/Projects/$1
(atom $1 &)
(spotify &)
(firefox &)
(sleep 10)
(spotifycli --play)
