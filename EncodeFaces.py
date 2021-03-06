import os
import cv2
import face_recognition
import pickle

knownEncodings = []
knownIds = []

# Here you put the folder where you dataset is located
for root, dirs, files in os.walk('dataset'):
    for file in files:

        # Get the id of the person according to the name of the folder where his photos are located
        _id = os.path.basename(root)
        imagePath = os.path.join(root, file)

        print("[INFO] processing image {} with id of {}".format(imagePath, _id))

        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb, model="hog")
        # Create a 128D vector with the face features of the person
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            knownEncodings.append(encoding)
            knownIds.append(_id)
            print(_id)

print("[INFO] serializing encodings...")
data = {"encodings": knownEncodings, "id": knownIds}
f = open("data/encodings.pickle", "wb")
f.write(pickle.dumps(data))
f.close()
