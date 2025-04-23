Configuring DHCP (Make sure to configure in the switch and not the router)

Check available options for DHCP and we will use the first one. This will replace `INT GIG0/0` with lets say example `interface fastEthernet 0/1`. But there might be an issue that the router doesnt support DHCP from fastEthernet connections. Therefore use `interface vlan 1` instead.

```
show ip interface brief
```

in router, initializing the router
```terminal
en
conf t
Hostname R1
INT GIG0/0 (to go to interface mode, do note address will be different)
IP ADD 192.168.1.1 255.255.255.0
NO SH (be default all cisco routers are in shutdown mode)
```

Creating IP pool
```terminal
exit (to go to config mode again)
IP DHCP POOL MUJ
NET 192.168.1.0 255.255.255.0 (we use 192.168.1.0 for net address, not IP)
DEFAULT-ROUTER 192.168.1.1
DNS-SERVER 8.8.8.8 (optional)
```

Checking id pool is created
```terminal
exit
exit
SHOW IP DHCP POOL (in privilege mode)
```

Now after this, for all our end devicec (PCs or laptops) we can configure DHCP ip addresses. The IP addresses are given on first come first serve basis.