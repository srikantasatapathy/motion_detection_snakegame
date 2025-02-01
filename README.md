# Motion Detection SnakeGame
1. The code uses OpenCV (cv2) for image processing, cvzone for hand tracking, and other standard libraries for mathematics and randomization.

2. Camera Setup
This initializes the webcam capture at 1280x720 resolution and sets up hand detection to track one hand with 80% confidence.

3. The Main Game Class (snakeCVclass):
This class handles all game logic and contains several key features:


* Snake properties (points, length, score)
* Food management (multiple food images including apples, guavas, mushrooms, and bombs)
* Collision detection
* Game over states and restart functionality

Key game mechanics include:

* The snake follows your index finger movement
* The snake grows when it eats food (except bombs)
* Food randomly relocates every 3 seconds if not eaten
* Eating a bomb ends the game
* Colliding with the snake's body ends the game
* A score system tracks successful food collection

4. Game Loop:

The main loop captures camera frames, detects hand position, and updates the game state accordingly.
Interesting features:

* The snake is drawn using OpenCV lines and circles
* Food items are overlaid as PNG images
* There's a restart button when game over occurs
* The game can be restarted by pressing 'r' or touching the restart button
* The game can be quit by pressing 'q'

Installation
===========================
step 1 => python3 -m venv venv 
step 2 => source venv/bin/activate

Step 3
Required libraries 
--------------------
pip install opencv-python
pip install cvzone              # Provides useful computer vision utilities.
pip install numpy               # Used for numerical operations, particularly for handling points.
pip install mediapipe
pip install pygame              # Add pygame for sound

Step 4 => python3 main.py