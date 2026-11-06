## установка
```shell
git clone https://github.com/prolivtrevoga/esp32-lan-led.git && cd esp32-lan-led
```
---
### на пк
```shell
python3 -m venv .venv
.venv/bin/pip install fastapi uvicorn[standard]
```
запуск сервера
```shell
./venv/bin/python -m uvicorn api:app --reload --host 0.0.0.0 --port 8000
```
---
### на esp32
**на esp должен быть установлен MicroPython**

открыть терминал, выполнить
```shell
sudo apt update && sudo apt upgrade -y
sudo apt install pipx
```
```shell
sudo su
pipx ensurepath
pipx install mpremote

mpremote cp main.py :main.py
```
нажать кнопку перезагрузки на плате
