import cv2

image = cv2.imread("Ronak...png")

if image is not None:
    succuss = cv2.imwrite("output_Ronak...png", image)
    if succuss:
        print("image Save successfully as output_image")

    else:
        print("Failed Too Save Image")

else:
    print("Error : Could not Load Image")
        

