import numpy as np
import cv2

cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)


while True:
    ret,frame=cap.read()    
    width=int(cap.get(3))  #Lấy chiều rộng  (Từ cột 0 qua phải)
    height=int(cap.get(4)) #Lấy chiều cao   (Từ hàng 0 trở xuống)

    #1. Vẽ line

    img=cv2.line(frame,(0,0),(width,height),(125,55,255),5)   #Vẽ trên frame, điểm bắt đầu, điểm kết thúc, mã màu, thickness
    img=cv2.line(frame,(width,0),(0,height),(255,0,0),5)
    img=cv2.line(frame,(width//2,0),(width//2,height),(0,255,0),5)
    img=cv2.line(frame,(0,height//2),(width,height//2),(0,0,255),5)

    #2. Vẽ hình chữ nhật
    img=cv2.rectangle(frame,(0,0),(width,height//4),(125,125,125),-1)  #thichness=-1 là full hình chữ nhật
    
    #3. Vẽ hình tròn
    img=cv2.circle(frame,(width//2,height//2),min(width,height)//2,(0,0,0),5) #thickness -1 là đổ màu full hình tròn
    
    #4. Chèn text
    font=cv2.FONT_HERSHEY_TRIPLEX
    img=cv2.putText(img,"Bo Bo",(width//4,height//2),font,3,5)
    
    
    cv2.imshow("Cua so cam",frame)
    if cv2.waitKey(1)==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()