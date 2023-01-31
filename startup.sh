#!/bin/bash

if nc -zw1 google.com 443; then
    if ! [ -a RaspberryPiCameraSystemStartup ]; then
        git clone https://github.com/Matt8687/RaspberryPiCameraSystemStartup.git
    elif [ -a RaspberryPiCameraSystemStartup ]; then
        git pull https://github.com/Matt8687/RaspberryPiCameraSystemStartup.git
    fi
else echo "No Internet, booting offline..."
fi

if ! [ -a RaspberryPiCameraSystemStartup/startup.py ]; 
then
    echo -e "The Startup.py file does not exist in the current directory,\nplease ensure that it is before continuing.";
    exit 1
fi

python RaspberryPiCameraSystemStartup/startup.py
