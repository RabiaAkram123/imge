################practice#############
####################################
import cv2
image = cv2.imread("C:/Users/unknown/OneDrive/Desktop/RabiaAkram/open_cv/example.jpg")
if image is None:
    print("Image not found or failed to load.")
else:
    cv2.imshow("My Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

