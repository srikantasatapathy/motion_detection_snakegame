import cvzone
import cv2
import numpy as np
import math
import random
from cvzone.HandTrackingModule import HandDetector
import time
import pygame  # Add pygame for sound


# Initialize pygame mixer for sound
pygame.mixer.init()

# Load sound effects
try:
    eat_sound = pygame.mixer.Sound("apple.mp3")  # Sound for eating regular food
    bomb_sound = pygame.mixer.Sound("bomb.mp3")  # Sound for eating bomb
except:
    print("Warning: Sound files not found. Please ensure 'eat.wav' and 'bomb.wav' exist in the same directory.")
    eat_sound = None
    bomb_sound = None

# setup openCV capture and window size
capture = cv2.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)

detect = HandDetector(detectionCon=0.8, maxHands=1)


class snakeCVclass:
    def __init__(self, foodImages):
        self.point = []  # Points of the snake
        self.length = []  # Distance between points
        self.currentLength = 0  # Total snake length
        self.TotalAllowedLength = 150  # Total allowed length
        self.headPrevious = 0, 0  # Previous head point.

        # Load multiple food images
        self.foodImages = {img: cv2.imread(img, cv2.IMREAD_UNCHANGED) for img in foodImages}
        self.foodNames = list(self.foodImages.keys())  # List of food file names
        self.currentFood = random.choice(self.foodNames)  # Pick a random food to start
        self.foodIMG = self.foodImages[self.currentFood]

        # Get food image size
        self.foodHeight, self.foodWidth, _ = self.foodIMG.shape
        self.foodLocation = 0, 0  # Food position
        self.FoodLocationRandom()  # Initialize food position

        self.score = 0  # Game score
        self.gameOver = False  # Check if game is over

        # Timer for food relocation
        self.foodTimer = time.time()  # Start the timer

    # set the food location
    # Randomly place food in a new location
    def FoodLocationRandom(self):
        self.foodLocation = random.randint(100, 1000), random.randint(100, 600)
        self.currentFood = random.choice(self.foodNames)  # Pick a new random food
        self.foodIMG = self.foodImages[self.currentFood]  # Update the image
        self.foodHeight, self.foodWidth, _ = self.foodIMG.shape  # Update size
        self.foodTimer = time.time()  # Reset the timer

    def update(self, mainIMG, headCurrent):

        if self.gameOver:
            restartX, restartY, restartW, restartH = 450, 100, 300, 80  # Button (x, y, width, height)
            cvzone.putTextRect(mainIMG, "Game Over", [250, 350], scale=8, thickness=4, colorT=(255, 255, 255),
                           colorR=(0, 0, 255), offset=20)
            
            cvzone.putTextRect(mainIMG, f'Your Score: {self.score}', [150, 500], scale=8, thickness=5,
                           colorT=(255, 255, 255), colorR=(233, 161, 16), offset=20)
            
            # Draw Restart Button
            cv2.rectangle(mainIMG, (restartX, restartY), (restartX + restartW, restartY + restartH), (0, 255, 0), cv2.FILLED)
            cvzone.putTextRect(mainIMG, "Restart", [restartX + 45, restartY + 55], scale=3, thickness=3, colorT=(255, 255, 255), colorR=(0, 255, 0))
            
            # Check if user touches the button
            currentX, currentY = headCurrent
            if restartX < currentX < restartX + restartW and restartY < currentY < restartY + restartH:
                self.gameOver = False
                self.score = 0  # Reset the score
                self.point = []
                self.length = []
                self.currentLength = 0
                self.TotalAllowedLength = 150
                self.headPrevious = 0, 0
                self.FoodLocationRandom()
            
        else:
            # Break down the previous and current points location to x and y
            previousX, previousY = self.headPrevious
            currentX, currentY = headCurrent

            # Find the distance between the previous and the current point.
            self.point.append([currentX, currentY])
            distance = math.hypot(currentX - previousX,
                                  currentY - previousY)  # distance = sqrt([currentX - previousX]^2 + [currentY - previousY]^2)
            self.length.append(distance)
            self.currentLength += distance
            self.headPrevious = currentX, currentY

            # Check if snake eats the bomb food (Game Over)
            foodX, foodY = self.foodLocation
            if (foodX - self.foodWidth // 2 < currentX < foodX + self.foodWidth // 2 and
                    foodY - self.foodHeight // 2 < currentY < foodY + self.foodHeight // 2):
                if self.currentFood == "bomb.png":
                    if bomb_sound:  # Play bomb sound
                        bomb_sound.play()
                    self.gameOver = True  # End game if bomb is eaten
                else:
                    if eat_sound:  # Play eating sound
                        eat_sound.play()
                    self.FoodLocationRandom()
                    self.TotalAllowedLength += 50
                    self.score += 1
                    print(self.score)

            # Reducing Length if current length exceeds the allowed length
            if self.currentLength > self.TotalAllowedLength:
                for i, length in enumerate(self.length):
                    self.currentLength -= length
                    self.length.pop(i)  # Remove the subtracted length in index i
                    self.point.pop(i)  # Remove the point corresponding to the removed length

                    # Check if the current length has become less than the total allowed length
                    if self.currentLength < self.TotalAllowedLength:
                        break
            # Get food position
            foodX, foodY = self.foodLocation

            # check if snake ate the food
            randomX, randomY = self.foodLocation
            if (foodX - self.foodWidth // 2 < currentX < foodX + self.foodWidth // 2 and
                    foodY - self.foodHeight // 2 < currentY < foodY + self.foodHeight // 2):
                self.FoodLocationRandom()
                self.TotalAllowedLength += 50
                self.score += 1
                print(self.score)
            # If food has been there for more than 3 seconds, relocate it
            if time.time() - self.foodTimer > 3:
                self.FoodLocationRandom()

            # Draw the snake line
            if self.point:
                for i, point in enumerate(self.point):
                    if i != 0:
                        cv2.line(mainIMG, self.point[i - 1], self.point[i], (233, 161, 16),
                                 20)  # cv2.line(image, start_point, end_point, color, thickness) color combination BGR
                cv2.circle(img, self.point[-1], 20, (67, 202, 9), cv2.FILLED)

            # collision check
            point = np.array(self.point[:-2], np.int32)
            point = point.reshape((-1, 1, 2))
            cv2.polylines(mainIMG, [point], False, (0, 200, 0), 3)
            minDist = cv2.pointPolygonTest(point, (currentX, currentY), True)

            # check if the collision happens
            if -1 <= minDist <= 1:
                if bomb_sound:  # Play bomb sound
                    bomb_sound.play()
                print("hit")
                self.gameOver = True
                self.point = []
                self.length = []
                self.currentLength = 0
                self.TotalAllowedLength = 150
                self.headPrevious = 0, 0
                self.FoodLocationRandom()

            # Draw food
            mainIMG = cvzone.overlayPNG(mainIMG, self.foodIMG, (foodX - self.foodWidth // 2, foodY - self.foodHeight // 2))

            # showScore
            cvzone.putTextRect(mainIMG, f'Your Score :{self.score}', [20, 40], scale=1, thickness=1, offset=10,colorT=(255,255,255), colorR=(233, 161, 16),font=cv2.FONT_HERSHEY_DUPLEX)  # color combination BGR  not RGB

        return mainIMG


game = snakeCVclass(["apple.png", "guava.png", "mushroom.png", "bomb.png"])
restart_game = False

while True:
    success, img = capture.read()  # Read a frame from the video capture
    img = cv2.flip(img, 1)  # Flip the camera horizontally
    hand, img = detect.findHands(img, flipType=False, draw=False)  # Detect hands in the camera  ( draw=False  -> Disables cvzone’s drawing on the hand)

    if hand:
        landmarkList = hand[0]['lmList']  # Get the landmark list for the detected hand
        pointIndex = landmarkList[8][0:2]  # Get the location of the index finger tip (x, y)
        img = game.update(img, pointIndex) # Update game

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('r'):
        game.gameOver = False
        game.score = 0  # Reset the score to 0
        restart_game = True

    if restart_game:
        game = snakeCVclass(["apple.png", "guava.png", "mushroom.png", "bomb.png"])  # Create a new instance of the game object
        restart_game = False

    if key == ord('q'):
        break
# Clean up
pygame.mixer.quit()
cv2.destroyAllWindows()
capture.release()