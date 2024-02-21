#!/usr/bin/env python3
import cv2

# Open a video file or use the camera (0 for default camera)
video_capture = cv2.VideoCapture(0)  # Replace 'your_video_file.mp4' with the actual video file path

while video_capture.isOpened():
    # Read a frame from the video
    ret, frame = video_capture.read()

    # Break the loop if the video is finished
    if not ret:
        break

    # Display the frame
    cv2.imshow('frame', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
video_capture.release()
cv2.destroyAllWindows()
