import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snap():
    number = random.randint(1, 100)
    video_capture_object = cv2.VideoCapture(0)
    result = True
    while (result):
        ret, frame = video_capture_object.read()
        filename = "this_person_is_using_the_pc" + str(number) + ".png"
        cv2.imwrite(filename, frame)
        start_time = time.time
        result = False

    
    video_capture_object.release()
    cv2.destroyAllWindows()
    print("snapshot taken. Check your cloud for the image.")

    return filename

def upload_snap(imgname):
    access_token = 'hlbnIgnFHW4AAAAAAAAAATu_CwD2lWmAPlEQvOIUAopaTzlkDr3tUdzY_A80kS0z'
    file = imgname
    file_from = file
    file_to = '/who_is_using_this_pc/' + imgname
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("uploaded")
    

def main():
    while (True):
        if((time.time() - start_time) >= 10):
            name = take_snap()
            upload_snap(name)


main()
