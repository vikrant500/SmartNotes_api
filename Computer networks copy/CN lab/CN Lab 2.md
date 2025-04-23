```terminal
(by default we are in user exe mode)
en (takes to privilege mode)
conf t (takes to global configuration mode)
hostname rajesh
do reboot (optional)
```
Save can only be done in privilege mode
```terminal
exit
copy running-config startup-config
```
(Or just write 'wr' instead, you can also do this in configuration mode my typing 'do wr')
```terminal
show run
show startup (shows data of nvram)
show ip int br
conf t
int
interface gig0/0
```
(Now we are in interface mode)
```terminal
ip add 192.168.1.1 255.255.255.0
```
(Cisco tracers are in shutdown mode by default, so type)
```terminal
no shutdown
(Or no sh)
exit
exit
wr
show ip int
conf t
interface GigabitEthernet0/0
exit
interface GigabitEthernet0/0
exit
```
(Now to set up password)
```terminal
enable ?
enable password
enable password cisco
Exit (now in privilege)
```
(Now we have setup a pass for privilege mode)
```terminal
exit
en
(Enter pass)
show run
conf t
no enable password
enable secret password cisco
```
(To have an encrypted password)
```terminal
exit
exit
en
(enter pass)
show run
conf t
no enable secret (remove password)
exit
show run
xit
conf t
line vty 0 4
(Setting remote login pass)
password cisco
```