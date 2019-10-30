#!/bin/bash

DIR="${1}_env"
activate () {
    source ~/Documents/Projects/$1/${DIR}/bin/activate
}

cd
cd ~/Documents/Projects/
(atom $1 &)
(spotify &)
(firefox &)
(sleep 10)
(spotifycli --play)
cd $1
if [ -d $DIR ]; then
  activate
fi
