// Pin map for the environmental node (ESP32-WROOM-32).
// Source: Stage 2 submission, slide 12 (Electronics: Pinout & Power Distribution).
// Design-stage; not yet validated on hardware.
#pragma once

// DHT22 (single-wire, 10k pull-up)
#define PIN_DHT22_DATA     4

// PMS5003 on UART2, 9600 baud, SET low = sleep
#define PIN_PMS_TX         16
#define PIN_PMS_RX         17
#define PIN_PMS_SET        25

// MQ-135 analog on ADC1 via 10k/20k divider, heater gated by MOSFET
#define PIN_MQ135_AO       34
#define PIN_MQ135_HEATER   26

// JSN-SR04T ultrasonic (ECHO is 5 V, divided to 3.3 V)
#define PIN_JSN_TRIG       21
#define PIN_JSN_ECHO       35

// NEO-6M GPS on UART1 (remapped), 9600 baud
#define PIN_GPS_TX         32
#define PIN_GPS_RX         33

// RFM95W LoRa on VSPI, 865-867 MHz
#define PIN_LORA_SCK       18
#define PIN_LORA_MISO      19
#define PIN_LORA_MOSI      23
#define PIN_LORA_NSS       5
#define PIN_LORA_RST       14
#define PIN_LORA_DIO0      27

// microSD (shared SPI bus)
#define PIN_SD_CS          13

// Battery sense, ADC1, 100k/100k divider
#define PIN_BATT_SENSE     36

// Strapping pins 0, 2, 12, 15 intentionally left free.
// Use ADC1 only (ADC2 is unavailable while Wi-Fi is active).
