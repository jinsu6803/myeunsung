from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from django.http import HttpResponse
import cv2
import threading
import numpy as np
import pyrealsense2 as rs


def home(request):
    context = {}

    return render(request, "home.html", context)


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(1)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


class LidarCamera(object):
    def __init__(self):
        self.grabbed = True
        self.pipeline = rs.pipeline()
        self.config = rs.config()

        self.config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        self.pipeline.start(self.config)
        self.frames = self.pipeline.wait_for_frames()
        self.depth_frame = self.frames.get_depth_frame()
        self.depth_image = np.asanyarray(self.depth_frame.get_data())

        self.depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(self.depth_image, alpha=0.03), cv2.COLORMAP_JET)

        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.pipeline.stop()

    def get_frame(self):
        image = self.depth_colormap
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            self.frames = self.pipeline.wait_for_frames()
            self.depth_frame = self.frames.get_depth_frame()
            self.depth_image = np.asanyarray(self.depth_frame.get_data())
            self.depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(self.depth_image, alpha=0.03), cv2.COLORMAP_JET)


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def detectme(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        print("에러입니다...")
        pass


@gzip.gzip_page
def lidar_detectme(request):
    try:
        lidar = LidarCamera()
        return StreamingHttpResponse(gen(lidar), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        print("에러입니다...")
        pass