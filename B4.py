
import numpy as np
import cv2
#Su dung cam
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    #lấy chiều rộng của video
    width = int(cap.get(3))
    #lấy chiều cao của video
    height = int(cap.get(4))
    #thu nhỏ frame cam còn  1 nửa mỗi chiều
    small_frame = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5)
    #tạo 1 khối có kích thước bằng cam toàn số 0(màu đen), uint8 số nguyên 8 bit
    image = np.zeros(frame.shape, np.uint8)
    #tạo 4 khối nhỏ bằng nhau => kết quả hình b4
    """image[:height//2, :width//2] = small_frame
    image[:height//2, width//2:] = small_frame
    image[height//2:, :width//2] = small_frame
    image[height//2:, width//2:] = small_frame"""

    #tạo 4 khối nhỏ bằng nhau và xoay các khôi => hình 4.2
    image[:height // 2, :width // 2] = small_frame
    image[:height // 2, width // 2:] = cv2.rotate(small_frame, cv2.ROTATE_180)
    image[height // 2:, :width // 2] = cv2.rotate(small_frame, cv2.ROTATE_180)
    image[height // 2:, width // 2:] = small_frame
    # ret True neu doc duoc frame
    print(ret)
    cv2.imshow("cam", image)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
