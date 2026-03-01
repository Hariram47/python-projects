import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self,
                 mode=False,
                 maxHands=2,
                 detection_confidence=0.7,
                 tracking_confidence=0.7):

        self.mode = mode
        self.maxHands = maxHands
        self.detection_confidence = detection_confidence
        self.tracking_confidence = tracking_confidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detection_confidence,
            min_tracking_confidence=self.tracking_confidence
        )

        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]

    def find_hands(self, frame, draw=True):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        frame,
                        handLms,
                        self.mpHands.HAND_CONNECTIONS
                    )

        return frame

    def find_position(self, frame, draw=False):

        allHands = []

        if self.results.multi_hand_landmarks:

            for handType, handLms in zip(
                    self.results.multi_handedness,
                    self.results.multi_hand_landmarks):

                myHand = {}
                lmList = []

                for id, lm in enumerate(handLms.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append((id, cx, cy))

                myHand["lmList"] = lmList
                myHand["type"] = handType.classification[0].label

                allHands.append(myHand)

        return allHands

    def fingers_up(self, lmList):

        fingers = []

        if lmList[self.tipIds[0]][1] > lmList[self.tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if lmList[self.tipIds[id]][2] < lmList[self.tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers