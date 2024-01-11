import cv2
from cv2 import getTickCount, getTickFrequency

cap = cv2.VideoCapture(0)  # dev表示Jetson Nnao上USB的设备号，上面查看摄像头挂载情况那里提到我的USB是video2，故我这里dev = 2

cap.set(3,1280)     # 设置参数 宽
cap.set(4,960)      # 高
cap.get(3)      # 得到宽度
cap.get(4)      # 得到高度
print(cap.get(3))   # 输出
print(cap.get(4))

while (1):
    ret, frame = cap.read()  # ret:True/False,代表有没有读到图片  frame:当前截取一帧的图片
    # image_Gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      #灰度处理

    # 计算FPS
    loop_time = getTickCount()
    total_time = loop_time / (getTickFrequency())
    FPS = int(1 / total_time)

    # 在图像左上角添加FPS文本
    fps_text = f"FPS: {FPS :.2f}"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    text_color = (0, 0, 255)  # 红色
    text_position = (10, 30)  # 左上角位置
    cv2.putText(frame, fps_text, text_position, font, font_scale, text_color, font_thickness)

    # 显示图像
    cv2.imshow('Local Camera', frame)
    # cv2.imshow("Video_Gray", image_Gray)  # 在窗口中显示灰度视频

    # 如果使用的是64位的计算机，cv.waitKey()函数的返回值与0xff按位相与操作，取其低八位，再与27（Esc的ASCII码为27）比较，
    # 或者这样cv2.waitKey(10) & 0xff == ord(‘q’)，ord函数是取其ASCII编码，当然换成其他的字符也行只要ASCII码对应就行。
    # cv.waitKey()是一个键盘绑定函数。其参数是以毫秒为单位的时间。该函数等待任何键盘事件指定的毫秒
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

