#!/bin/bash

git clone https://github.com/Matt8687/RaspberryPiCameraSystemStartup.git

if ! [ -a "startup.py" ]; 
then
    echo -e "The Startup.py file does not exist in the current directory,\nplease ensure that it is before continuing.";
    exit 1
fi

python startup.py
