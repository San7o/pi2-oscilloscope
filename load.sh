#!/bin/sh

set -e

#
# Load a program to the Pico2
#

# Set the correct device here
DEVICE=/dev/sdp1
PROGRAM=oscilloscope
MOUNT=/mnt/usb

if [ "$PROGRAM" = "" ]; then
    echo "Error, PROGRAM not selected"
    exit 1
fi

if [ ! -f build/"$PROGRAM".uf2 ]; then
    echo "Error, build/$PROGRAM.uf2 not found"
    exit 1
fi

mkdir -p $MOUNT
mount $DEVICE $MOUNT 

echo Copying $PROGRAM into $DEVICE ...
cp build/$PROGRAM.uf2 $MOUNT

# Wait a little bit
sleep 1
sync
sleep 1

echo Done!

