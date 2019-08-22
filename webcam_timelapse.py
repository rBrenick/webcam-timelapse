import os
import time
import cv2

def main():
    """
    at set intervals, take image from capture source and output in output_folder
    
    """
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    prev_time = int(time.time())

    output_folder = os.path.join(os.path.dirname(__file__), "OUTPUT")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        

    INTERVAL_IN_SECONDS = 3
    image_format = output_folder.replace("\\", "/") + "/opencv_time_{}.jpg"


    while True:
        
        current_time = int(time.time())

        if current_time - prev_time > INTERVAL_IN_SECONDS:
            prev_time = current_time
            
            ret, frame = cam.read()
            if not ret:
                break
            
            # cv2.imshow("test", frame)
            
            img_name = image_format.format(current_time)
            cv2.imwrite(img_name, frame)
            print(f"screenshot taken {img_name}")
            
            
    cam.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

