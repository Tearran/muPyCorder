from machine import Pin, I2C
import ssd1306

# using default address 0x3C
i2c = I2C(sda=Pin(4), scl=Pin(5))
# SSD1306_I2C([width in pixels], [Hight in pixels], i2c)
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.text('Hello, World!', 36, 32, 1)
display.show()