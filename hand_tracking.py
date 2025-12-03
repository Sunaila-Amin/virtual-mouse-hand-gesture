import cv2
import mediapipe as mp
import time
import numpy as np
import pyautogui
import math

pyautogui.FAILSAFE = False

# Screen size
screen_w, screen_h = pyautogui.size()

# MediaPipe Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

prev_x, prev_y = 0, 0
smoothening = 7

drag_started = False
drag_start_time = 0

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    h, w, c = img.shape

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            fingers = []

            # Thumb (sideways logic)
            if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
                fingers.append(1)
            else:
                fingers.append(0)

            # Other fingers (vertical logic)
            tip_ids = [8, 12, 16, 20]
            for tip in tip_ids:
                if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # Draw finger states
            cv2.putText(img, str(fingers), (10, 120),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

            # Coordinates for index finger
            x1 = int(hand_landmarks.landmark[8].x * w)
            y1 = int(hand_landmarks.landmark[8].y * h)

            # Smooth cursor movement
            screen_x = np.interp(x1, (0, w), (0, screen_w))
            screen_y = np.interp(y1, (0, h), (0, screen_h))
            curr_x = prev_x + (screen_x - prev_x) / smoothening
            curr_y = prev_y + (screen_y - prev_y) / smoothening
            prev_x, prev_y = curr_x, curr_y

            # 1️⃣ Cursor Movement (only index up)
            if fingers == [0,1,0,0,0]:
                pyautogui.moveTo(curr_x, curr_y)
                cv2.circle(img, (x1, y1), 12, (255,0,255), cv2.FILLED)

            # Distance between thumb & index
            x2 = int(hand_landmarks.landmark[4].x * w)
            y2 = int(hand_landmarks.landmark[4].y * h)
            length = math.hypot(x2 - x1, y2 - y1)

            # 2️⃣ Left Click (pinch)
            if length < 40 and not drag_started:
                pyautogui.click()
                cv2.circle(img, (x1, y1), 15, (0,255,0), cv2.FILLED)
                time.sleep(0.2)

            # 3️⃣ Right Click (index + middle up)
            if fingers == [0,1,1,0,0]:
                pyautogui.rightClick()
                cv2.circle(img, (x1, y1), 15, (0,0,255), cv2.FILLED)
                time.sleep(0.2)

            # 4️⃣ Drag-and-Drop (pinch hold > 0.3 seconds)
            if length < 40:
                if not drag_started:
                    drag_start_time = time.time()
                    drag_started = True
                elif time.time() - drag_start_time > 0.3:
                    pyautogui.mouseDown()
            else:
                if drag_started:
                    pyautogui.mouseUp()
                drag_started = False

            # 5️⃣ Scroll (Pinky up)
            if fingers == [0,0,0,0,1]:
                if y1 < h//2:
                    pyautogui.scroll(50)   # scroll up
                else:
                    pyautogui.scroll(-50)  # scroll down

    cv2.imshow("Virtual Mouse", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
