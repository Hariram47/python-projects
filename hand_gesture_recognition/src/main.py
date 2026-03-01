import cv2
import pyautogui
import time
from hand_tracker import HandTracker

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

def main():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker(maxHands=1)

    screen_w, screen_h = pyautogui.size()

    cooldown = 0.8
    last_action_time = 0

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        frame = tracker.find_hands(frame)
        hands = tracker.find_position(frame)

        if hands:
            hand = hands[0]
            lmList = hand["lmList"]
            fingers = tracker.fingers_up(lmList)

            x1, y1 = lmList[8][1], lmList[8][2]
            cam_h, cam_w, _ = frame.shape

            screen_x = int(x1 * screen_w / cam_w)
            screen_y = int(y1 * screen_h / cam_h)

            current_time = time.time()

            if fingers == [0,1,0,0,0]:
                pyautogui.moveTo(screen_x, screen_y)
                pyautogui.mouseUp()
                drawing = False

            elif fingers == [0,1,1,0,0]:
                pyautogui.moveTo(screen_x, screen_y)
                pyautogui.mouseDown()
                drawing = True

            elif fingers == [0,1,1,1,0]:
                pyautogui.moveTo(screen_x, screen_y)
                pyautogui.mouseDown(button="right")
                drawing = True

            else:
                pyautogui.mouseUp()
                pyautogui.mouseUp(button="right")
                drawing = False

            if current_time - last_action_time > cooldown:

                if fingers == [1,0,0,0,0]:
                    pyautogui.press("right")

                elif fingers == [0,0,0,0,1]:
                    pyautogui.press("left")

                elif fingers == [1,1,1,1,1]:
                    pyautogui.scroll(400)

                elif fingers == [0,1,0,0,1]:
                    pyautogui.scroll(-400)

                last_action_time = current_time

        cv2.imshow("Smart PPT Gesture Control", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()