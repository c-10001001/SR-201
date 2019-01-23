Updated version of the script, python3 compatible.<br>
This folder contains a configuration.yml example which can be integrated into your own home-assistant configuration.
It should also work with hass.io but you might need to install python via `apk add --no-cache python3`

---

- Download sr_201_ctrl.py
- transfer it to your openhab machine, we used the /config/deps/ folder during testing.
- chmod +x the script.
- For adding it to home-assistant see [configuration.yml](https://github.com/001100010010011110100001101101110011/SR-201/blob/master/home-assistant/configuration.yml)


### Testing on commandline:

Browse to a folder where the script is located.
Issue the following commands to turn relay 1 on and then off:
```
# python ha_sr201_ctrl.py 192.168.1.25 6722 11
# python ha_sr201_ctrl.py 192.168.1.25 6722 21
```

Relay two can be controlled by issuing `12` and `22` instead of 11 and 21.
