# b0xx-joycontrol
b0xx keyboard controls connecting to nintendo switch with bluetooth using joycontrol (need to use a virtual machine if on windows, I used vmware)
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
```
follow instructions in https://github.com/Almtr/joycontrol-pluginloader#pairing-the-pro-controller-of-joycontrol and https://github.com/Almtr/joycontrol-pluginloader#usage
