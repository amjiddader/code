Install Gui on Ubuntu 
apt update
apt install tigervnc-standalone-server tigervnc-xorg-extension -y
apt install xserver-xorg-core -y
apt install ubuntu-gnome-desktop -y
systemctl start gdm

# Setup VNC password 
vncpasswd

# RUN VNC 
vncserver
vncserver -kill :*
mv ~/.vnc/xstartup ~/.vnc/xstartup.bak

vim ~/.vnc/xstartup

#!/bin/sh 
[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
vncconfig -iconic &
dbus-launch --exit-with-session gnome-session &


chmod +x ~/.vnc/xstartup

vncserver -localhost no -geometry 1080x720 -depth 24

Now access VNC at : server-ip:5901 
