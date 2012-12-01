jimovpn
=======

openvpn hosted on raspberry pi server

Part I: Get Raspberry Pi Started
================================

The official RPi Easy SD Card Setup guild:
*(http://elinux.org/RPi_Easy_SD_Card_Setup).*

Copying an image to the SD Card in Mac OS X
-------------------------------------------
1. Download the image from a mirror or torrent.
* http://www.raspberrypi.org/downloads
For starters, wheezy-raspbian is recommended.
2. Extract the image:
* unzip ~/Downloads/2012-10-28-wheezy-raspbian.zip
3. From the terminal run:
* df -h
Please record the device name of the filesystem's partition, e.g.*/dev/disk3s1*
4. Unmount the partition so that you will be allowed to overwrite the disk:
* sudo diskutil unmount /dev/disk3s1
(or: open Disk Utility and unmount the partition of the sdcard (do not eject
it, or you have to reconnect it)
5. Using the device name of the partition work out the raw device name for the
entire disk, by omitting the final "s1" and replacing "disk" with "rdisk" (this
is very important: you will lose all data on the hard drive on your computer if
you get the wrong device name). Make sure the device name is the name of the
whole SD card as described above, not just a partition of it (for example,
rdisk3, not rdisk3s1. Similarly you might have another SD drive name/number
like rdisk2 or rdisk4, etc. -- recheck by using the df -h command both before &
after you insert your SD card reader into your Mac if you have any doubts!):
e.g. /dev/disk3s1 => /dev/rdisk3
6. In the terminal write the image to the card with this command, using the raw
disk device name from above (read *carefully* the above step, to be sure you
use the correct rdisk# here!):
* sudo dd bs=1m if=~/.../2012-10-28-wheezy-raspbian.img of=/dev/rdisk3
* if the above command report an error(dd: bs: illegal numeric value), please
change bs=1M to bs=1m
* (note that dd will not feedback any information until there is an error or it
is finished, information will show and disk will re-mount when complete.
However if you are curious as to the progresss - ctrl-T (SIGINFO, the status
argument of your tty) will display some en-route statistics).
7. After the dd command finishes, eject the card:
* sudo diskutil eject /dev/rdisk3
* (or: open Disk Utility and eject the sdcard)
8. Insert it in the raspberry pi and go nuts!

Part II: Config Your Raspberrry Pi
==================================
From command line input:
* sudo raspi-config

Part III: Install nginx
=======================
1. From terminal command line:
* sudo apt-get install nginx
2. Create user and group for nginx
* sudo useradd www-data
* sudo groupad www-data
3. Add nginx user to nginx group
* sudo usermod -g www-data www-data
4. Now we need have our nginx config file set under /etc/nginx/sites-available
server {
        # Make site accessible from jimovpn.yifengliu.com and LAN IPs.
        server_name example.com 192.168.1.*;

        location / {
                uwsgi_pass unix:///run/uwsgi/app/jimovpn/socket;
                include uwsgi_params;
        }

        location /doc/ {
                alias /usr/share/doc/;
                autoindex on;
                allow 127.0.0.1;
                allow ::1;
                deny all;
        }
}
5. Put your own index.html under /var/www
6. Start the web server
* sudo service nginx start
