#!/bin/bash

# DOCKER INSTALLATION:
echo splash installation started ...
echo please wait a second ...
sleep 1s

# change directory
cd /home/jtech || exit

# update packages:
echo updating packages ...
sudo apt update

# install prerequisite packages which let apt use packages over https:
echo intalling prerequisite to let apt use packages overs https ...
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# add the GPG key for the official Docker repository to your system:
echo adding the GPG key for the official Docker repository to the system ...
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# add the docker repository to APT sources:
echo adding docker repository to apt sources ...
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# update the package database with the Docker packages from the newly added repo:
echo updating package database ...
sudo apt update

# install docker
echo installing docker ...
sudo apt install docker-ce

# echo checking docker status ...
# sudo systemctl status docker

# download & install splash
echo downloading and installing splash ...
sudo docker pull scrapinghub/splash

# launch splash
echo launching splash ...
sudo docker run -it -p 8050:8050 scrapinghub/splash

# open up your browser & navigate to the following address:
# http://127.0.0.1:8050 



