#!/bin/bash
# Auto Run Heard Protector for Heard Immunity.

echo " Enter FILE NAME (if in same dir), or full path:";
read filename;
echo "Enter SLEEP TIME, in seconds:";
read stime

echo "Eight in Repose";

sleep 4;

while true; do echo "Starting up. . . . . ";clear && python3 $filename; sleep $stime; done
