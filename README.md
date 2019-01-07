# SR-201
Python code for SR-201 ethernet relay.

This repository will contains working code to configure and control SR-201 Ethernet relay boards through home-assistant.
We've also been able to control the board through the openhab exec binding.

Also see the following repository for more mature code:
https://github.com/cryxli/sr201

---
Configuring the relay:
Reset is done by placing a jumper on the clear and adjacent unlabeled pins like so:
5v        gnd
. +-+ . . .
. . . . . .

By default the relay comes with the following settings
IP static: `192.168.1.100`
Configuration Port: `5111`

It is best to prepare the desired configuration and acompanying commands before connect since the relay disconnect "idle" sessions quickly.

We will be configuring the relay with the following settings:<br>
IP:`192.168.1.25`
Netmask:`255.255.255.0`
Gateway:`192.168.1.254`

To do this you will need to enter a # followed by a commandcode then a comma and finally the new setting ending with a semicolon. When no new settings are specified the commandcodes end with a semicolon. 
The commandcodes are the same for each relay, the part with 
So the above example will need the following commands:
```
#19876;
#29876,192.168.1.25;
#39876,255.255.255.0;
#49876,192.168.1.254;
#A9876,0;
#79876;
```
The first command list the current configuration and can be used to verifiy the connection to the remote.
The second command sets the new IP, the third sers the netmask, and the fourth command sets a gateway.
The fifth command is especially important, this disabled the cloud connectivty (phone-home) for the relay.
The last command confirms the changes and resets the relay.

You can reconfigure the relay through telnet with a client like putty.
- Reset the relay.
- Assing your pc an IP in the correct range for example: 192.168.1.111
> Try to ping the relay, if the configuration of pc is correct and the relay was reset it should respond.
- Connect with telnet to `192.168.1.100` port `5111`
> the console might display >err; this indicates that you are connected!
- Issue the prepared commands if all is well each command will return >OK!

---
# Openhab2 sample files.
Prerequisites
- [ ] Install Openhab 2
  - [ ] Install exec binding
  - [ ] Install RegEx Transformation.

Copy the files and directories from this repo's `openhab2` folder into the openhab2 folder on your system. 
These examples assume relay-state.py is placed in the home of the openhab user so: `/home/openhab/relay-state.py`

Access the sitemap though http://youropenhabname:8080/basicui/app?sitemap=sr201
