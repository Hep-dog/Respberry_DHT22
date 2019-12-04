#!/usr/bin/bash

sudo apt update		&&
sudo apt upgrade	&&

sudo wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -	&&
sudo echo "deb https://repos.influxdata.com/debian buster stable" | sudo tee /etc/apt/sources.list.d/influxdb.list	&&

sudo apt update			&&
sudo apt install influxdb		&&
sudo apt install influxdb-client	&&
sudo apt install telegraf		&&


sudo wget -qO- https://packages.grafana.com/gpg.key | sudo apt-key add -	&&
sudo apt-key list		&&

sudo apt update			&&
sudo apt install grafana	&&


sudo systemctl enable influxdb.service	&&
sudo systemctl enable grafana.service
