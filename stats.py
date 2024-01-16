# Source:
# Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
# Load another font from: https://www.dafont.com/bitmap.php

import time
import board
import busio
import digitalio

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import subprocess

# APP PARAMETRS #
oled_reset = digitalio.DigitalInOut(board.D4)  # Define the Reset Pin

# Display Parameters 128 x 32 (0,91 inch)
WIDTH = 128
HEIGHT = 32
BORDER = 1

LOOPTIME = 1.0  # Display Refreshrate
PAGE_SCROLL = 2.0  # Changing pages


#################
def clear_display():  # Clear display.
    oled.fill(0)
    oled.show()


def first_page():  # Refresh first page
    ### IP ADDRESS ###
    cmd = "hostname -I | cut -d' ' -f1"
    IP = subprocess.check_output(cmd, shell=True)

    ### CPU USAGE ###
    cmd = "top -bn1 | grep load | awk '{printf \"CPU: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell=True)

    ### CPU TEMPERATURE ###
    cmd = "vcgencmd measure_temp |cut -f 2 -d '='"
    Temp = subprocess.check_output(cmd, shell=True)

    # Formatting stats
    draw.text((0, 0), "IP: " + str(IP, "utf-8"), font=font, fill=255)
    draw.text((0, 16), str(CPU, "utf-8") + "%", font=font, fill=255)
    draw.text((70, 16), "T: " + str(Temp, "utf-8"), font=font, fill=255)


def second_page():  # Refresh second page
    ### RAM USAGE ###
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell=True)

    ### DISK USAGE ###
    cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%dGB %s", $3,$2,$5}\''
    Disk = subprocess.check_output(cmd, shell=True)

    # Formatting stats
    draw.text((0, 0), str(MemUsage, "utf-8"), font=font, fill=255)
    draw.text((0, 16), str(Disk, "utf-8"), font=font, fill=255)


# Init #
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

clear_display()

image = Image.new(
    "1", (oled.width, oled.height)
)  # Create blank image for drawing, "1" mean for 1-bit color

draw = ImageDraw.Draw(image)  # Get drawing object to draw on image.

draw.rectangle(
    (0, 0, oled.width, oled.height), outline=255, fill=255
)  # Draw a white background

font = ImageFont.truetype("PixelOperator.ttf", 16)  # Font

while True:
    # first page
    draw.rectangle(
        (0, 0, oled.width, oled.height), outline=0, fill=0
    )  # Draw a black filled box to clear the image.
    first_page()
    # Display image
    oled.image(image)
    oled.show()
    time.sleep(LOOPTIME + PAGE_SCROLL)

    # second page
    draw.rectangle(
        (0, 0, oled.width, oled.height), outline=0, fill=0
    )  # Draw a black filled box to clear the image.
    second_page()
    oled.image(image)
    oled.show()
    time.sleep(LOOPTIME + PAGE_SCROLL)
