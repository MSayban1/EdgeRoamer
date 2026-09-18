import pyautogui
import time
import random
import os

STARTUP_DELAY = 10
MIN_WAIT = 10
MAX_WAIT = 10

SCRIPT_FOLDER = os.path.dirname(os.path.abspath(__file__))
TOPICS_FILE = os.path.join(SCRIPT_FOLDER, "topics.txt")


def load_topics():
    # Reads every line from topics.txt sitting next to this script
    with open(TOPICS_FILE, "r", encoding="utf-8") as f:
        topics = [line.strip() for line in f if line.strip()]
    if not topics:
        raise ValueError("topics.txt is empty, add at least one topic")
    return topics


def open_edge():
    pyautogui.press("win")
    time.sleep(1.5)
    pyautogui.typewrite("microsoft edge", interval=0.05)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(4)


def search_random_topic(topics):
    topic = random.choice(topics)
    pyautogui.hotkey("ctrl", "l")
    time.sleep(0.5)
    pyautogui.typewrite(topic, interval=0.05)
    pyautogui.press("enter")
    print("Searched:", topic)


def random_scroll():
    for _ in range(random.randint(1, 3)):
        pyautogui.scroll(random.choice([-500, -400, 400, 500]))
        time.sleep(random.uniform(0.5, 1.5))


def open_new_tab():
    pyautogui.hotkey("ctrl", "t")
    time.sleep(1)


def random_wait():
    time.sleep(random.uniform(MIN_WAIT, MAX_WAIT))


def main():
    topics = load_topics()

    print("Bot starts in", STARTUP_DELAY, "seconds. Switch to your desktop now.")
    print("It will keep running until you stop it yourself.")
    print("Move your mouse to any screen corner, or press Ctrl+C, to stop it.")
    time.sleep(STARTUP_DELAY)

    open_edge()

    try:
        while True:
            search_random_topic(topics)
            random_wait()
            random_scroll()
            open_new_tab()
            random_wait()
    except KeyboardInterrupt:
        print("Stopped by you. Bot finished.")


if __name__ == "__main__":
    main()
