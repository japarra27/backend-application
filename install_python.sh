#!/bin/bash
sudo apt-get -y update
sudo apt-get -y install virtualenv

virtualenv -p python3 venv
sudo apt -y update
sudo apt -y upgrade

sudo apt -y install python3-pip
sudo apt-get install redis-server

sudo service redis-server start

