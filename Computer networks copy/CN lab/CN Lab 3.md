Star topology using hub and switch

to check mac address of PC in command prompt
(make sure to give it an ip in the format `192.168.xxx.xx`)
```terminal
ipconfig /all
```

Use this command in privilege mode in CLI of switch to check mac addresses
```terminal
en
show mac address-table
```

if no mac address pulls up then ping the other 2 systems from the current system using this command in the command prompt of PC
```terminal
ping 192.168.xxx.xx
```
