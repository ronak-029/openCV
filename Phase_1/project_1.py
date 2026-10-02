import cv2

image = cv2.imread("Ronak...png")

if image is not None:
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    user = input("Enter which image you show gray :  ")
    if user== "gray":        
        cv2.imshow("Black & White Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        cv2.imshow("Black & White Image",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    outputName = input("Enter a Output Name : ")
    if user == "gray":
        cv2.imwrite(f"{outputName}.png",gray)
        print(f"file Name {user} save Successfully")
    else:
        cv2.imwrite(f"{outputName}.png",image)
        print(f"Old file {user} save Successfully")


else:
    print("Image in not Found")
