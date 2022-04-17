# Install building packages for Linux
sudo apt update
sudo apt upgrade
sudo apt install -y build-essential python3-pip python3-venv openjdk-18-jdk
sudo apt install -y git curl wget unzip zip nethogs gnome-shell-extensions gnupg
sudo apt install -y rtl8821ce-dkms ntfs-3g

mkdir ~/install
# Install Required Apps 
# install google chrome
cd ~/install
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
# install telegram
cd ~/install
wget https://updates.tdesktop.com/tlinux/tsetup.3.7.0.tar.xz
tar xf tsetup.3.7.0.tar.xz
# install protonvpn
cd ~/install
wget https://protonvpn.com/download/protonvpn-stable-release_1.0.1-1_all.deb
sudo apt install -y ./protonvpn-stable-release_1.0.1-1_all.deb
sudo apt update
sudo apt-get install -y protonvpn-cli
# install vscode
sudo snap install code --classic
# install pycharm
sudo snap install pycharm-professional --classic
# install clion
sudo snap install clion --classic
# install android studio
sudo snap install android-studio --classic
# install postman
sudo snap install postman
# install heroku
sudo snap install heroku --classic
# install flutter
sudo snap install flutter --classic
flutter doctor
# install requirements for flutter linux
sudo apt-get install clang cmake ninja-build pkg-config libgtk-3-dev liblzma-dev
flutter config --enable-linux-desktop
# install firebase-cli
cd ~/install
curl -sL https://firebase.tools | bash
# install yt-dlp
sudo snap install yt-dlp
# install mongodb
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo systemctl daemon-reload
sudo systemctl start mongod
sudo systemctl enable mongod
# install postgresql
sudo apt install -y postgresql postgresql-contrib libpq-dev
# Setup installed apps

# Setup Telegram
cd ~/install/Telegram/./Telegram

echo "Did you logged in and enabled auto start? (y/n)"
read telegram
if [ $telegram = "y" ]; then
    echo "Now setup Google Chrome"
fi
google-chrome
code
echo "Did you installed Github Copilot, Flutter, Python, C++, Code Runner, ACMX extensions? (y/n)"
read code
if [ $code = "y" ]; then
    echo "Now setup PyCharm"
fi
echo "Did you setup PyCharm, Github Copilot? (y/n)"
read pycharm
if [ $pycharm = "y" ]; then
    echo "Now setup Clion"
fi
echo "Did you setup Clion, Github Copilot? (y/n)"
read clion
if [ $clion = "y" ]; then
    echo "Now setup Android Studio"
fi
echo "Did you setup Android Studio, Github Copilot, Flutter, CMD-tools, Emulator? (y/n)"
read android
if [ $android = "y" ]; then
    echo "Now setup Postman"
fi
echo "Did you setup Postman? (y/n)"
read postman
if [ $postman = "y" ]; then
    echo "Now setup Heroku"
fi
echo "Did you setup Heroku? (y/n)"
read heroku
if [ $heroku = "y" ]; then
    echo "Now install dash-to-panel, simple-net-speed, "
fi
google-chrome extensions.gnome.org