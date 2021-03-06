#!/bin/bash
# ifconfig in net-tools
# iwconfig in wireless_tools

export wlan=wlp8s0u2
export eth=eno2

if [ $1 = 'c' ]; then
    source ~/Tools/ergwave/ergwaverc
    gsettings set org.gnome.system.proxy mode 'none'
    echo Done proxy setting
    sudo systemctl stop NetworkManager
    sudo systemctl mask NetworkManager
    sudo systemctl daemon-reload
    echo Done stopping NetworkManager
    sudo pkill dhcpcd
    sudo rfkill unblock wifi
    echo Done rf-kill unblock
    sudo ifconfig $eth down
    sudo ifconfig $wlan up
    sudo iwconfig $wlan essid ERGWAVE
    echo Done $wlan config
    sudo dhcpcd -4q $wlan
    echo Done dhcp $wlan
    python ~/Tools/ergwave/ergwave.py
fi

if [ $1 = 'dc' ]; then
    sudo pkill dhcpcd
    echo Done closing dhcp
    sudo ifconfig $wlan down
    sudo ifconfig $eth up
    sudo systemctl unmask NetworkManager
    sudo systemctl daemon-reload
    sudo systemctl start NetworkManager
    echo Done wifi config
    gsettings set org.gnome.system.proxy mode 'manual'
    echo Done proxy setting
    echo wifi disconnection succeed
fi
