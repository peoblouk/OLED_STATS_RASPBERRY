<!-- @format -->

# OLED Stats

OLED Stats Display Script For Raspberry Pi

The script is pre-configured for 128x21 I2C OLED Display, but can easily be modified to run on a 128x32 I2C OLED Display

## Installation Steps:

1. Connect **GND, VCC(3.3v), SCL, & SDA** ports of the display according to the picture shown below:
2. Upgrade your Raspberry Pi firmware and reboot:

```shell
    $ sudo apt-get update
    $ sudo apt-get full-upgrade
    $ sudo reboot
```

3. Install python3-pip & upgrade the setuptools

```shell
    $ sudo apt-get install python3-pip
    $ sudo pip3 install --upgrade setuptools
```

4. Install the Adafruit CircuitPython library using the following commands:

```shell
    $ cd ~
    $ sudo pip3 install --upgrade adafruit-python-shell
    $ sudo reboot

    $ wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
    $ sudo python3 raspi-blinka.py
```

5. Check the `I2C` status using the command:

```shell
    $ sudo i2cdetect -y 1

        0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
    00:                         -- -- -- -- -- -- -- --
    10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    30: -- -- -- -- -- -- -- -- -- -- -- -- 3c -- -- --
    40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    70: -- -- -- -- -- -- -- --
```

6. Install the CircuitPython libraries specific to the display. Enter the following commands:

```shell
    $ sudo pip3 install adafruit-circuitpython-ssd1306
    $ sudo pip3 install psutil
    $ sudo reboot
    $ sudo apt-get install python3-pil
```

7. Download the python script from github:

```shell
    $ git clone https://github.com/peoblouk/oled_stats_128x32.git

    $ cd OLED_Stats
    $ cp PixelOperator.ttf ~/PixelOperator.ttf
    $ cp stats.py ~/stats.py
```

8. For activating on startup do `crontab` follow the procedure:

```shell
    $ crontab -e
```

**Add this at the bottom:**

```
    @reboot python3 /home/{username}}/stats.py &
```

9. At the end reboot

```shell
    $ sudo reboot
```
