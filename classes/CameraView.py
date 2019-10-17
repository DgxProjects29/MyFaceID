import cv2

# this class returns the frames of the camera streaming


class CameraView:

    def __init__(self):
        # You could use a video file instead of a camera device
        self.cam = cv2.VideoCapture(0)

        # width is equal to 640 and height is 480
        self.height = self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.width = self.cam.get(cv2.CAP_PROP_FRAME_WIDTH)

    def start(self):
        pass

    def get_frame(self):
        if self.cam.isOpened():
            ret, frame = self.cam.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            else:
                return ret, None
        else:
            return False, None

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.cam.isOpened():
            self.cam.release()
