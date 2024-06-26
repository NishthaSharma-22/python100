import mediapipe as mp
import cv2
import numpy as np
import time
import random

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
score = 0

x_enemy = random.randint(50, 600)
y_enemy = random.randint(50, 400)

def enemy(image):
    global score, x_enemy, y_enemy
    cv2.circle(image, (x_enemy, y_enemy), 25, (200, 0, 0), 5)

video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Error: Could not open video stream.")
    exit()

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            print("Error: Failed to capture image.")
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = cv2.flip(image, 1)
        imageHeight, imageWidth, _ = image.shape

        results = hands.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        font = cv2.FONT_HERSHEY_COMPLEX
        color = (255, 0, 255)

        text = cv2.putText(image, "Score", (480,30), font, 1, color, 4, cv2.LINE_AA)
        text = cv2.putText(image, str(score), (590, 30), font, 1, color, 4, cv2.LINE_AA)

        enemy(image)

        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2))
        
        if results.multi_hand_landmarks:
            for handLandmarks in results.multi_hand_landmarks:
                for point in mp_hands.HandLandmark:
                    normalizedLandmark = handLandmarks.landmark[point]
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)

                    if point == mp_hands.HandLandmark.INDEX_FINGER_TIP:
                        if pixelCoordinatesLandmark is not None:
                            cv2.circle(image, (pixelCoordinatesLandmark[0], pixelCoordinatesLandmark[1]), 25, (0, 200, 0), 5)

                            if abs(pixelCoordinatesLandmark[0] - x_enemy) <= 10 and abs(pixelCoordinatesLandmark[1] - y_enemy) <= 10:
                                print("Found")
                                x_enemy = random.randint(50, 600)
                                y_enemy = random.randint(50, 400)
                                score += 1
                                text = cv2.putText(image, "Score", (100, 100), font, 1, color, 4, cv2.LINE_AA)
                                enemy(image)

        cv2.imshow("Hand Tracking", image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            print(score)
            break

video.release()
cv2.destroyAllWindows()
