import cv2

def take_snapshot():
    video_capture_object = cv2.VideoCapture(0)
    result = True
    while (result):
        ret, frame = video_capture_object.read()
        print(ret)
        cv2.imwrite("this_person_is_using_the_pc.png", frame)
        result = False

    video_capture_object.release()
    cv2.destroyAllWindows()

    

take_snapshot()