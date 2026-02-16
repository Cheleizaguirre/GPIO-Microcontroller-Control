# GPIO Microcontroller Control

Desktop application to control GPIO pins of a microcontroller or Raspberry Pi with real-time monitoring, scheduling, sensor integration, and email notifications. Built with Python 3, Tkinter, and subprocess scripts for GPIO management. The system allows toggling pins, scheduling automatic actions via cron, monitoring PIR sensors, and managing email-based alerts.

---

## 🎯 Purpose

1. **Enable** real-time control of GPIO pins on a Raspberry Pi or microcontroller.
2. **Provide** a graphical interface for easy ON/OFF switching, monitoring, and scheduling.
3. **Integrate** sensors and email notifications for automation and remote monitoring.
4. **Practice** Python desktop development, GPIO interfacing, and subprocess automation.

---

## ✨ Key Features

- Real-time GPIO pin monitoring with visual feedback.
- ON/OFF control of multiple pins via buttons, checkboxes, and combo boxes.
- Scheduling system to automatically turn pins on/off using cron jobs.
- PIR sensor integration for motion detection triggers.
- Email system to send alerts or status updates.
- Remote control support via scripts for networked microcontrollers.
- Intuitive Tkinter GUI with dynamic labels and images for state display.
- Buffered updates to ensure consistent monitoring and visual feedback.

---

## 🛠️ Stack


| Layer           |	Technology                                                     |
|-----------------|----------------------------------------------------------------|
| Language        |	Python 3                                                       |
| GUI Framework   |	Tkinter + ttk                                                  |
| GPIO Management |	RPi.GPIO + subprocess scripts                                  |
| Multimedia      |	Pygame (for optional feedback/alerts)                          |
| Scheduling      |	Linux cron jobs via Python scripts                             |
| Automation      |	Shell scripts (.sh) for pin control, sensor, and email actions |
| Platform        | Raspberry Pi / Linux-based microcontrollers                    |

---

## ⚙️ Local Installation (Developers)

```bash
# 1. Clone repository
$ git clone https://github.com/yourusername/GPIO-Microcontroller-Control.git
$ cd GPIO-Microcontroller-Control

# 2. Install dependencies
$ pip install RPi.GPIO pygame

# 3. Make sure scripts have executable permissions
$ sudo chmod +x *.sh

# 4. Run the main GUI application
$ python3 main.py
```

Note: This project requires a Raspberry Pi or compatible microcontroller with GPIO pins. Some scripts require root privileges (sudo) to manipulate GPIO pins or cron jobs.

---

## 🧠 How It Works

1. The Tkinter GUI displays real-time GPIO pin states and allows manual control.
2. User actions trigger Python functions that execute shell scripts (.sh) to toggle pins.
3. A scheduler writes cron jobs to automatically control pins at specified times.
4. PIR sensor monitoring runs as a background subprocess and updates the interface.
5. Email notifications are triggered via subprocess scripts when specific events occur.
6. Visual feedback is updated with labels, buttons, and images for current states.

---

## 🚀 Future Improvements

- Add multi-pin configuration for advanced microcontroller setups.
- Implement web-based remote control with Flask or FastAPI.
- Add historical logging for GPIO states and sensor triggers.
- Integrate more sensor types (temperature, light, humidity).
- Improve GUI with ttkbootstrap or custom themes for modern UI.

---

## 🤝 Contributing

1. Fork the repository and create a new branch (git checkout -b feature/YourFeature).
2. Commit changes with clear messages.
3. Open a Pull Request describing your improvements or bug fixes.

---
