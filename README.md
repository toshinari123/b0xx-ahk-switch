# b0xx-joycontrol
b0xx keyboard controls connecting to nintendo switch with bluetooth using joycontrol (need to use a virtual machine if on windows, I used vmware and https://mirror.us.leaseweb.net/ubuntu-cdimage/xubuntu/releases/20.04/release/)
```
sudo apt install git pip python3-dbus libhidapi-hidraw0
git clone https://github.com/mart1nro/joycontrol.git
sudo pip3 install joycontrol/
git clone --recursive https://github.com/Almtr/joycontrol-pluginloader.git
```
paste in these lines into `joycontrol-pluginloader/joycontrolPlugin/commands.py`
```python
async def stick2(self, stick, axis, value):
        await self.cli.cmd_stick(stick, axis, value * MAX_STICK_POWER + MAX_STICK_POWER)
```
save and type in terminal:
```
sudo pip3 install joycontrol-pluginloader/
sudo pip3 uninstall hid
sudo pip3 install hid==1.0.4
```
follow instructions in https://github.com/Almtr/joycontrol-pluginloader#pairing-the-pro-controller-of-joycontrol and https://github.com/Almtr/joycontrol-pluginloader#usage
(boxx.py is a joycontrol plugin)
# layout

![image](https://discord.com/channels/@me/1108176577759559690/1118922383244394636)
