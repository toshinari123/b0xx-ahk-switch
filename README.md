# b0xx-joycontrol (not tested)
b0xx keyboard controls connecting to nintendo switch with bluetooth using joycontrol (need to use a virtual machine if on windows, I used ~~vmware~~ DONT use vmware use vbox instead; disk used: https://mirror.us.leaseweb.net/ubuntu-cdimage/xubuntu/releases/20.04/release/)
```
sudo apt install git pip python3-dbus libhidapi-hidraw0
git clone https://github.com/mart1nro/joycontrol.git
sudo pip3 install joycontrol/
git clone --recursive https://github.com/Almtr/joycontrol-pluginloader.git
```
paste in these lines into `joycontrol-pluginloader/joycontrolPlugin/commands.py`
```python
async def stick2(self, stick, axis, value):
        await self.cli.cmd_stick(stick, axis, int(value * MAX_STICK_POWER + MAX_STICK_POWER))
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

![image](https://cdn.discordapp.com/attachments/1108176577759559690/1118922382975963136/Untitled.png)

# connection problems
i couldnt connect, will try again some other time (it just doesnt show up in change grip / order menu)

maybe helpful links:
https://github.com/lowlevel-1989/joytransfer
lowlevel-1989/joytransfer
https://github.com/Poohl/joycontrol/issues/4
Cursed Bluetooth Hardware · Issue #4 · Poohl/joycontrol
https://github.com/mart1nro/joycontrol/issues/8
Incompatibility with bluetooth "input" plugin · Issue #8 · mart1nro/joycontrol
https://github.com/Poohl/joycontrol/issues/24
detected too many SDP-records. Switch might refuse connection. · Issue #24 · Poohl/joycontrol
https://github.com/Poohl/joycontrol
Poohl/joycontrol: Emulate Nintendo Switch Controllers over Bluetooth
https://github.com/mart1nro/joycontrol/issues/115
not quite sure what the issue is but i'll leave the error code here (running ubuntu 20.04 under windows WSL service) · Issue #115 · mart1nro/joycontrol


in vbox the `sudo hciconfig hci0 up` showed no such file or directory the problem can be seen in `dmesg | grep tooth` had to do this https://forums.linuxmint.com/viewtopic.php?t=377733 also link the config.bin
