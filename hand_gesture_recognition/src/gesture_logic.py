class GestureLogic:
    def __init__(self):
        self.tip_ids = [4, 8, 12, 16, 20]

    def fingers_up(self, landmark_list):

        if not landmark_list or len(landmark_list) < 21:
            return []

        fingers = []

        if landmark_list[self.tip_ids[0]][1] > landmark_list[self.tip_ids[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for i in range(1, 5):
            if landmark_list[self.tip_ids[i]][2] < landmark_list[self.tip_ids[i] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

    def detect_gesture(self, landmark_list):

        fingers = self.fingers_up(landmark_list)

        if fingers == [0, 0, 0, 0, 0]:
            return "FIST"

        elif fingers == [0, 1, 0, 0, 0]:
            return "ONE"

        elif fingers == [0, 1, 1, 0, 0]:
            return "PEACE"

        elif fingers == [0, 1, 1, 1, 0]:
            return "THREE"

        elif fingers == [1, 0, 0, 0, 0]:
            return "THUMB"

        elif fingers == [1, 1, 1, 1, 1]:
            return "PALM"

        else:
            return "UNKNOWN"