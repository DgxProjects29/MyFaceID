import face_recognition
import pickle
import cv2
import os

# This class is used for scanning the frame of the camera streaming and return the id of the person. Besides it returns
# other data which will be used for the history. PD: this class uses the average method.


class FaceScan:
    def __init__(self):

        self.data = pickle.loads(open("data/encodings.pickle", "rb").read())
        parent = os.path.abspath(os.path.join('classes', os.pardir))
        self.data_settings = pickle.loads(open(parent + "/data/settings.pickle", "rb").read())

    def scanning(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb, model="hog")
        _id = "UnKnown"

        if len(boxes) != 0:
            encoding = face_recognition.face_encodings(rgb, boxes)
            matches = face_recognition.face_distance(self.data["encodings"], encoding[0])
            votes = {}
            average = {}
            unique_id = []

            for i, m in enumerate(matches):
                _id = self.data["id"][i]
                if _id not in average:
                    unique_id.append(_id)
                average[_id] = average.get(_id, 0) + m
                if m <= 0.5:
                    votes[_id] = votes.get(_id, 0) + 1

            for i2 in unique_id:
                average[i2] = average[i2]/self.data["id"].count(i2)

            print(votes)
            print(average)

            if len(average) != 0:
                _id = min(average, key=average.get)
                if average[_id] <= self.data_settings['average_num']:
                    return _id, votes, average
                else:
                    return "UnKnown", votes, average
            else:
                return "UnKnown", votes, average
        else:
            return "NoFace", False, False
