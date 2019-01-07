Updated version of the script, python3 compatible.<br>
This folder contains a configuration.yml example which can be integrated into your own home-assistant configuration.
It should also work with hass.io but you might need to install python via `apk add --no-cache python3`
---

- Download sr_201_ctrl.py
- transfer it to your openhab machine, we used the /config/deps/ folder during testing.
- chmod +x the script.

### Testing on commandline:

Browse to a folder where the script is located.
```
# python sr_201_ctrl.py 192.168.1.25 6722 11
```
