This folder is used for internet setup.

# Folders
* USB_Ethernet - contains files to setup internet over USB.
	* ipMasquerade.sh - shares the hosts internet
	* pocketssh.sh - ssh file that starts and ssh session but starts sharing internet.
	* setDNS.sh - Used by ipMasquerade.sh.
	* setDate.sh - Used by ipMasquerade.sh.

# USB Over Ethernet
If you need internet on your pocket beagle without wifi this is an option you have.

Go to the directory `USB_Ethernet` and run the scripts like below:
```bash
host$ ifconfig

enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
        inet6 fe80::47d6:e0f4:dc64:2397  prefixlen 64  scopeid 0x20<link>
        ether 08:00:27:8a:33:ba  txqueuelen 1000  (Ethernet)
        RX packets 4845146  bytes 1090226163 (1.0 GB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 4354745  bytes 6384727841 (6.3 GB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 3511  bytes 291124 (291.1 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 3511  bytes 291124 (291.1 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

host$ ./ipMasquerade.sh enp0s3
host$ ./pocketssh.sh
```

default login:
```
USER: fpp
PASS: falcon
```

# WIFI Setup
TODO: Insert more info later
