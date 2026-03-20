cmake_minimum_required(VERSION 3.13...3.27)
# Set the board here
set(PICO_BOARD pico2)
# initialize pico-sdk from submodule
# note: this must happen before project()
include(pico-sdk/pico_sdk_init.cmake)

project(pi2-oscilloscope)

# initialize the Raspberry Pi Pico SDK
pico_sdk_init()

add_executable(oscilloscope src/oscilloscope.c)

# pull in common dependencies
target_link_libraries(oscilloscope
  pico_stdlib
  hardware_adc
  hardware_dma
  hardware_clocks
  hardware_pwm
)

# enable usb output, disable uart output
pico_enable_stdio_usb(oscilloscope  1)
pico_enable_stdio_uart(oscilloscope 0)

# create map/bin/hex/uf2 file etc.
pico_add_extra_outputs(oscilloscope)
