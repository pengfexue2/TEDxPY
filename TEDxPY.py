#coding:'utf-8'
import time
import os
import win32gui, win32ui, win32con, win32api
from PIL import Image
import pytesseract
import webbrowser

def window_capture(filename):
    hwnd = 0
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    MoniterDev = win32api.EnumDisplayMonitors(None,None)
    #w = MoniterDev[0][2][2]
    # #h = MoniterDev[0][2][3]
    w = 380
    h = 150
    saveBitMap.CreateCompatibleBitmap(mfcDC,w,h)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0,0),(w,h),mfcDC,(20,140),win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC,filename)
start = time.time()
window_capture('haha.jpg')
text=pytesseract.image_to_string(Image.open('haha.jpg'),lang='chi_sim')
list =''.join(text.split())
url = 'http://www.baidu.com/s?wd=%s' % list
webbrowser.open(url)
end = time.time()
print(end-start)

#此python代码于1月11日凌晨根据百万英雄的录播视频写成，在此测试效果

#本人初学python,新开微信公众号 TEDxPY 以记录python学习、开发过程

#关注公众号，回复"自动搜题"即可获取源码

#人生苦短，我用python,欢迎对python感兴趣的各位多多指教！




































