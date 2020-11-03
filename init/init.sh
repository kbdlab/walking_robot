set -e
sudo raspi-config
wget https://download.teamviewer.com/download/linux/teamviewer-host_armhf.deb
sudo apt install ./teamviewer-host_armhf.deb 
sudo teamviewer setup
sudo teamviewr info
