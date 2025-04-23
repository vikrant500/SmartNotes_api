```terminal
en
erase startup-config
conf t
hostname vik2
no ip domain-lookup
enable secret class
```

## Configuring Console and Virtual Terminal Lines
```terminal
line console 0
password cisco
login
logging synchronous
exec-timeout 0 0

exit

line vty 0 4
password cisco
login
logging synchronous
exec-timeout 0 0
exit
```

## Configuring IP addresses of connections
```terminal
int gig0/0/0
ip add 172.16.3.1 255.255.255.0
no shut
exit

(now for 'se' connections)

int se0/1/0
ip add 172.16.2.2 255.255.255.0
clock rate 64000
no shut

(repeat above for all connections)

exit
exit
show ip interface brief
```

## Routing
```terminal
(after pressing conf t)
vik1(config)# ip route 172.16.1.0 255.255.255.0 192.168.1.2
```
For router R3, we use:
`ip route` `(ip address of PC 2)` 255.255.255.0 `se0/1/0 address of R2`
