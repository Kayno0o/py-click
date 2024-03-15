import signal
import sys
from pynput.mouse import Listener as MouseListener
from pynput.mouse import Button
from pynput.keyboard import Listener as KeyboardListener
import time
from datetime import datetime
import json
import math

last_pos = (0, 0)

data = {
    "left_clicks": 0,
    "right_clicks": 0,
    "total_key_presses": 0,
    "key_presses": {},
    "total_distance": 0,
    "scroll_up": 0,
    "scroll_down": 0,
    "scroll_left": 0,
    "scroll_right": 0,
}


def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_log_file_name():
    now = datetime.now()
    return (
        "/home/kfyleyssant/Documents/github/py-click/"
        + now.strftime("%Y-%m-%d")
        + ".json"
    )


def load_log():
    global data
    file_path = get_log_file_name()
    try:
        with open(file_path, "r") as file:
            jsonData = json.load(file)
            for key, value in jsonData.items():
                if key in data:
                    data[key] = value
    except FileNotFoundError:
        pass


def save_log():
    file_path = get_log_file_name()
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)


def on_mouse_click(x, y, button, pressed):
    global data
    if pressed:
        if button == Button.left:
            data["left_clicks"] += 1
        elif button == Button.right:
            data["right_clicks"] += 1


def on_key_press(key):
    global data
    data["total_key_presses"] += 1
    try:
        data["key_presses"]["{}".format(key.char)] = (
            data["key_presses"].get("{}".format(key.char), 0) + 1
        )
    except AttributeError:
        data["key_presses"]["{}".format(key)] = (
            data["key_presses"].get("{}".format(key), 0) + 1
        )


def on_mouse_move(x, y):
    global data, last_pos
    pos = (x, y)
    print(euclidean_distance(last_pos, pos), last_pos, pos)
    data["total_distance"] = round(
        data["total_distance"] + abs(euclidean_distance(last_pos, pos)), 2
    )
    last_pos = pos


def signal_handler(sig, frame):
    print("Quitting script...")
    save_log()
    sys.exit(0)


def on_scroll(_x, _y, directionX, directionY):
    global data
    print(directionX, directionY)
    if directionY == -1:
        data["scroll_down"] += 1
    if directionY == 1:
        data["scroll_up"] += 1

    if directionX == -1:
        data["scroll_left"] += 1
    if directionX == 1:
        data["scroll_right"] += 1


signal.signal(signal.SIGINT, signal_handler)

mouse_listener = MouseListener(
    on_click=on_mouse_click, on_move=on_mouse_move, on_scroll=on_scroll
)
keyboard_listener = KeyboardListener(on_press=on_key_press)

load_log()

mouse_listener.start()
keyboard_listener.start()

while True:
    save_log()
    time.sleep(10)
