# ---------- Reading Videos ----------
capture = cv.VideoCapture('videos/sample.mp4')  # Opens a video file

while True: #Video is a sequence of images Loop runs frame by frame
    isTrue, frame = capture.read() #isTrue → True if frame read successfully .frame → current video image

    if not isTrue:
        break

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
