# Instalar Mininet
sudo pacman -S --needed base-devel git

git clone https://aur.archlinux.org/mininet.git ~/mininet

cd ~/mininet
makepkg -si

# Instalar xorg
pacman -S xorg-xhost

# Instalar OpenvSwitch
pacman -S openvswitch

# Usar Mininet
systemctl start ovs-vswitchd

systemctl start ovsdb-server

sudo mn

# Example 

h1 ping -c 4 h2

# Wireshark

Capturing from s1-eth1

# Referencias

https://mailman.stanford.edu/pipermail/mininet-discuss/2014-February/004030.html

https://hackmd.io/@pmanzoni/BklqpKddS

https://www.youtube.com/watch?v=2A_VZb4vPPY&t=276s
