set -e
sudo apt update
sudo apt install libqt5gui5
sudo raspi-config
wget https://download.teamviewer.com/download/linux/teamviewer-host_armhf.deb
sudo dpkg -i teamviewer-host_armhf.deb
sudo apt --fix-broken install 
sudo teamviewer setup
sudo teamviewr info