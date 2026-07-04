sudo apt update
sudo apt upgrade

sudo apt install git -y
sudo apt install build-essential
sudo apt install cmake
sudo apt install mpv
sudo apt install ffmpeg
sudo apt install curl

##tkinter
sudo apt install python3-tk


##Change grub stuff
sudo nano /etc/default/grub
sudo update-grub

##Install brave
sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
sudo curl -fsSLo /etc/apt/sources.list.d/brave-browser-release.sources https://brave-browser-apt-release.s3.brave.com/brave-browser.sources
sudo apt update
sudo apt install brave-browser

##VSCode
https://code.visualstudio.com/docs/setup/linux

##Install github desktop mwt >>
https://github.com/shiftkey/desktop?tab=readme-ov-file#installation-via-package-manager

##Aliasing
echo "alias aliase='nano ~/.bashrc'" >> ~/.bashrc
echo "alias aliass='source ~/.bashrc'" >> ~/.bashrc

echo "alias die='shutdown now'" >> ~/.bashrc
echo "alias rbt='systemctl reboot'" >> ~/.bashrc
echo "alias x='exit'" >> ~/.bashrc
echo "alias brv='brave browser'" >> ~/.bashrc
echo "alias ghub='github-desktop'" >> ~/.bashrc

echo "alias ytd='/home/root-username/scripts/ytd-fast.sh'" >> ~/.bashrc
echo "alias ytdf='/home/root-username/scripts/ytd.sh'" >> ~/.bashrc
echo "alias mdw='/home/root-username/scripts/md-worker.sh'" >> ~/.bashrc
echo "alias imgw='/home/root-username/scripts/img-worker.sh'" >> ~/.bashrc
echo "alias aimg='/home/root-username/scripts/img-to-audio.sh'" >> ~/.bashrc

source ~/.bashrc


cd "$HOME"
mkdir scripts
mkdir gitclones
cd gitclones

git clone https://github.com/MisterChamster/private-image-to-audio-embedder.git img-to-audio
git clone https://github.com/MisterChamster/private-image-worker.git img-worker
git clone https://github.com/MisterChamster/private-yt-downloader.git yt-download
git clone https://github.com/MisterChamster/private-audio-metadata-worker.git audio-mtd-worker

