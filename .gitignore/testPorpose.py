
    import pywhatkit as kit
    import cv2
    Handwritten=input("ENter your text: ")
    kit.text_to_handwriting(Handwritten, save_to="test.png")
    img=cv2.imread("test.png")
    cv2.imshow("img of writing",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()