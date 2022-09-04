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
