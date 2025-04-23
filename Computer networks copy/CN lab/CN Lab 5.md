Configuration of VLAN and inter-VLAN Communication using Router.
(Make sure to use switch 2960-24TT otherwise it will not work, test more routers as well)

On the switch go to cli and
```
en
show vlan
conf t
hostname vik
```

we wanna give IoT vlan 10 and CCE vlan 20

how many VLAN can we use?
```
vlan ?
```
output: `<1-4094> ISL VLAN IDs 1-1005`

Enter vlan 10 and 20 modes and rename accordingly
```
vlan 10
name IoT
exit
vlan 20
name CCE
exit
exit
```

`show vlan` to see the available VLANs

to set system now:

```
conf t
int fa0/1
switchport access vlan 20
exit
```

This will take a lot of time so we use `range`

```
int range fa0/1-fa0/3
switchport access vlan 20
exit
int range fa0/4-fa0/6
switchport access vlan 10
exit
```