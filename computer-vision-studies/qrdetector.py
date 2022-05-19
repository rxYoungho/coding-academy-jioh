import cv2
 
image = cv2.imread('/Users/Danny/Desktop/GitHub/coding-academy-jioh/computer-vision-studies/qr.png')
 
qrCodeDetector = cv2.QRCodeDetector()
 
decodedText, points, _ = qrCodeDetector.detectAndDecode(image)
 
if points is not None:
 
    nrOfPoints = len(points)
 
    for i in range(nrOfPoints):
        nextPointIndex = (i+1) % nrOfPoints
        cv2.line(image, tuple(points[i][0]), tuple(points[nextPointIndex][0]), (255,0,0), 5)
 
    print(decodedText)    
 
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
     
 
else:
    print("QR code not detected")