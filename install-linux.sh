#!/bin/bash
echo "Installing pip if for some reason it's not installed"
sudo apt install python3-pip
echo "Pip installing matplotlib and numpy"
pip3 install matplotlib
pip3 install numpy