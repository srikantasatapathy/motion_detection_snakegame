# 🐍 Motion Detection Snake Game using Computer Vision

### 🎮 A modern twist on the classic **Snake Game** using **Computer Vision**! Control the snake using your **hand movements** instead of a keyboard or joystick.

---

## 📌 Features

- 🖐️ **Hand Tracking:** The snake follows your index finger in real-time.
- 🍏 **Dynamic Food System:** Different food items have different point values.
- ⏳ **Time-Limited Food:** Food relocates every 3 seconds if not eaten.
- 💥 **Game Over Conditions:**
  - Eating a bomb ends the game.
  - Colliding with your own body results in game over.
- 🏆 **Scoring System:**
  - 🍎 Apple, Guava, Mushroom, Grape = **+1 point**
  - 🍊 Orange = **+3 points**
  - 🍓 Strawberry = **+5 points**
  - 🌶️ Red Chili = **-2 points (Be careful!)**

---

## 🛠️ Tech Stack & Libraries

- **Python 3.7+**
- **cvzone** – Computer vision utilities
- **OpenCV (cv2)** – Video capture & image processing
- **NumPy** – Numerical computations
- **Math** – Distance calculations
- **Random** – Food placement logic
- **HandDetector (cvzone.HandTrackingModule)** – Hand tracking & gesture detection

---

## 💻 Minimum System Requirements

- **Processor:** Intel Core i3 (8th Gen) / AMD Ryzen 3 or better
- **RAM:** 4GB (8GB recommended for smooth performance)
- **GPU (Optional but Recommended):** Intel HD Graphics or NVIDIA GTX 1050+
- **Storage:** 10GB free space
- **Webcam:** 720p or higher

---

## 🚀 Installation Guide

### 1️⃣ Install Python (If not installed)

Download and install **Python 3.7+** from [Python Official Site](https://www.python.org/downloads/).


### 2️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/snake-game-cv.git
cd snake-game-cv
```

###  Create Virtual Environment

```bash
python3 -m venv venv 
source venv/bin/activate
```

### 3️⃣ Install Required Dependencies

```bash
pip install cvzone opencv-python numpy mediapipe pygame
```

### 4️⃣ Run the Game

```bash
python snake_game.py
```

---

## 🛠️ Troubleshooting

- If **cvzone** fails to install, try:
  ```bash
  pip install mediapipe
  ```
- Ensure **webcam drivers** are updated.
- If on **macOS (M1/M2)**, use **Rosetta 2** for better Python package compatibility.

---

## 🎯 Future Enhancements

- 🎨 UI Improvements
- 🎵 Add background music and sound effects
- 🔥 More interactive gestures for controls

---

## 📢 Contributing

Have ideas to improve this game? Feel free to **fork** and contribute! 🚀

---

## 📝 License

This project is open-source and available under the **MIT License**.

---

### 🔥 **Enjoy the game and let me know your thoughts!** 🎮🖐️
