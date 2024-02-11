
# классный скрипт, можно много чего делать с его помощью, значительно облегчает работу
from winGuiAuto import *
import time
import os
import configparser
# import pyautogui
import keyboard


PROGRAM_VERSION = "1.0.0"

CONFIG_FILE = "auto_login.ini"

DEFAULT_CONFIG = {
    "delay": 2,
    "valid_foreground_window_title": "1С",
    "password": "",
    "debug_print": False,
}
config = {}

def load_config():
    global config

    def load_key(parser, key, type="str"):
        try:
            if type == "str":
                value = parser["DEFAULT"][key]
            elif type == "int":
                value = int(parser["DEFAULT"][key])
            elif type == "float":
                value = float(parser["DEFAULT"][key])
            elif type == "bool":
                value = bool(int(parser["DEFAULT"][key]))
        except KeyError:
            print(f"No key '{key}' in config file! Loaded from DEFAULT_CONFIG")
            value = DEFAULT_CONFIG[key]    

        return value


    if not os.path.exists(CONFIG_FILE):
        print("Config file not found! Loaded DEFAULT_CONFIG")
        config = DEFAULT_CONFIG
        return

    parser = configparser.ConfigParser()
    parser.read(CONFIG_FILE, encoding="utf-8")

    config["delay"] = load_key(parser, "delay", "int")
    config["valid_foreground_window_title"] = load_key(parser, "valid_foreground_window_title")
    config["password"] = load_key(parser, "password")
    config["debug_print"] = load_key(parser, "debug_print", "bool")


def debug_print(msg):
    if config["debug_print"]:
        print(msg)


def is_valid_foreground_window(valid_window_title):
    result = False

    foreground_window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    debug_print(foreground_window_title)

    if valid_window_title in foreground_window_title:
        result = True

    return result


def main():
    print(f"Program version: {PROGRAM_VERSION}")
    load_config()
    print(f"Current configuration: \n{config}")

    while True:
        time.sleep(config["delay"])


        if is_valid_foreground_window(config["valid_foreground_window_title"]):
            # вводим пароль и жмем enter
            debug_print("login attempt...")
            # pyautogui.typewrite(config["password"])
            # pyautogui.press("enter")
            keyboard.write(config["password"])
            keyboard.press_and_release("enter")

            # и закрываемся
            exit()


if __name__ == "__main__":
    main()