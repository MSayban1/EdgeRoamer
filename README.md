# 🌐 EdgeRoamer

**An automated browsing companion for Microsoft Edge, built with pure Python and desktop automation.**

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

---

## 📖 Overview

EdgeRoamer takes control of your keyboard and mouse the same way you would, opens Microsoft Edge, searches random topics, scrolls through the results, then hops into a fresh tab and does it again. It keeps going in an endless loop until you decide to stop it.

There is no Selenium, no WebDriver, and no browser automation framework involved. EdgeRoamer talks to your screen at the operating system level through `pyautogui`, simulating real key presses and mouse actions, so it works exactly like a person sitting at the keyboard would.

---

## ✨ Features

- 🖱️ **Real input simulation** — every action is a genuine keystroke or mouse event, not a background API call
- 🔁 **Runs forever** — loops endlessly until you stop it yourself
- 🎲 **Random topic selection** — pulls a fresh search term from an editable text file every cycle
- 📜 **Human-like scrolling** — adds small random scroll bursts after each search
- 🗂️ **Simple configuration** — edit a plain `.txt` file to change what it searches, no code editing required
- 🛑 **Instant failsafe** — move your mouse to any screen corner and the bot stops immediately
- 🚫 **Zero heavy dependencies** — one lightweight library, no virtual environment required

---

## 📁 Project Structure

```
EdgeRoamer/
├── edge_bot.py     # Main automation script
├── topics.txt      # List of search topics, one per line
├── README.md       # Project documentation
└── LICENSE         # MIT License
```

---

## ⚙️ Requirements

| Requirement       | Details                          |
|--------------------|-----------------------------------|
| Operating System   | Windows, with Microsoft Edge installed |
| Python             | 3.7 or newer                     |
| Dependency          | `pyautogui`                      |

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/EdgeRoamer.git
cd EdgeRoamer
```

Install the one required package, no virtual environment needed:

```bash
pip install pyautogui
```

---

## ▶️ Usage

Run the script from the project folder:

```bash
python edge_bot.py
```

What happens next:

1. You get a five second warning to switch to your desktop.
2. Microsoft Edge opens automatically through the Start menu, exactly like a human opening it.
3. The bot picks a random topic from `topics.txt`, jumps to the address bar, types it, and searches.
4. It scrolls the page a little, waits a random amount of time, then opens a brand new tab.
5. Steps 3 and 4 repeat endlessly until you stop the bot.

---

## 🛑 Stopping the Bot

EdgeRoamer is designed to run indefinitely, so stopping it is deliberate and instant:

- **Mouse failsafe** — drag your cursor into any corner of the screen and the script terminates immediately.
- **Keyboard interrupt** — press `Ctrl + C` in the terminal window running the script.

---

## 🔧 Configuration

### Changing search topics

Open `topics.txt` and add or remove one topic per line:

```
python automation tutorial
latest tech news
space exploration news
```

The bot automatically reads whatever is in that file every time it runs, so you never need to touch the Python code to change what it searches.

### Adjusting timing

Inside `edge_bot.py`, near the top of the file, you can tune these values:

| Variable         | Purpose                                      |
|-------------------|-----------------------------------------------|
| `STARTUP_DELAY`   | Seconds to wait before the bot takes control  |
| `MIN_WAIT`        | Shortest pause between actions                |
| `MAX_WAIT`        | Longest pause between actions                 |

---

## ⚠️ Disclaimer

This project simulates real mouse and keyboard input on your machine. While it runs, avoid touching your mouse or keyboard so the bot does not click or type in the wrong place. Use it only on your own device and at your own discretion.

---

## 👨‍💻 Author

**Script Written by:** Muhammad Sayban
**Company:** Saban Productions

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full details.
