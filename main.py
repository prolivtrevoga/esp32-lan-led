import network
import urequests
import time
from machine import Pin

# конфиг
WIFI_SSID = ""
WIFI_PASS = ""
SERVER_URL = "http://192.168.14.197:8000"  # апи
REQUEST_INTERVAL = 2 # пауза между запросами к апи
LED_PIN = 2 # пин светодиода

led = Pin(LED_PIN, Pin.OUT)
led.off()

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("подключение к wifi...")
        wlan.connect(WIFI_SSID, WIFI_PASS)
        
        timeout = 15
        while not wlan.isconnected() and timeout > 0:
            time.sleep(1)
            timeout -= 1
            
    if wlan.isconnected():
        print("подключено к сети. IP:", wlan.ifconfig()[0])
        return True
    else:
        print("не удалось подключиться к wifi")
        return False

def parse_bool(value): # приводит строку из json к bool
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in ("true", "1", "yes", "on")
    if isinstance(value, (int, float)):
        return value != 0
    return False

def check_led_state():
    response = None
    try:
        response = urequests.get(SERVER_URL, timeout=10)
        if response.status_code == 200:
            data = response.json()
            led_state = parse_bool(data.get("led", False))

            if led_state:
                led.on()
                print("led: on")
            else:
                led.off()
                print("led: off")
        else:
            print("HTTP error:", response.status_code)
    except Exception as e:
        print("ошибка запроса:", e)
    finally:
        if response:
            response.close()


if connect_wifi():
    while True:
        check_led_state()
        time.sleep(REQUEST_INTERVAL)
