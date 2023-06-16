#!/bin/sh

feh --bg-scale --randomize ~/.wallpapers
udiskie -t &
volumeicon &
setxkbmap us
picom &
# xset led 3

#starting utility applications at boot time
variety &
nm-applet &
# pamac-tray &
xfce4-power-manager &
numlockx on &
# blueberry-tray &
cbatticon &
picom --config $HOME/.config/qtile/scripts/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/lib/xfce4/notifyd/xfce4-notifyd &
xrandr --output HDMI-A-1 --primary --auto --right-of HDMI-A-2
xrandr --output HDMI-A-2 --primary

#starting user applications at boot time
# run volumeicon &
#run discord &
#nitrogen --restore &
#run caffeine -a &
#run vivaldi-stable &
#run firefox &
#run thunar &
#run dropbox &
#run insync start &
#run spotify &
#run atom &
#run telegram-desktop &
