import io  
from PIL import Image, ImageTk  
import tkinter as tk  
 
def resize(w, h, w_box, h_box, pil_image):  
  ''' 
  resize a pil_image object so it will fit into 
  a box of size w_box times h_box, but retain aspect ratio 
  对一个pil_image对象进行缩放，让它在一个矩形框内，还能保持比例 
  '''  
  f1 = 1.0*w_box/w # 1.0 forces float division in Python2  
  f2 = 1.0*h_box/h  
  factor = min([f1, f2])  
  #print(f1, f2, factor) # test  
  # use best down-sizing filter  
  width = int(w*factor)  
  height = int(h*factor)  
  return pil_image.resize((width, height), Image.ANTIALIAS)  
  
 
root = tk.Tk()  
# size of image display box you want  
#期望图像显示的大小  
w_box = 50  
h_box = 50  
 
  
# open as a PIL image object  
#以一个PIL图像对象打开  
pil_image = Image.open(r'airplane00.tif')  
  
# get the size of the image  
#获取图像的原始大小  
w, h = pil_image.size  
  
# resize the image so it retains its aspect ration  
# but fits into the specified display box  
#缩放图像让它保持比例，同时限制在一个矩形框范围内  
pil_image_resized = resize(w, h, w_box, h_box, pil_image)  
  
  
# convert PIL image object to Tkinter PhotoImage object  
# 把PIL图像对象转变为Tkinter的PhotoImage对象  
tk_image = ImageTk.PhotoImage(pil_image_resized)  
  
# put the image on a widget the size of the specified display box  
# Label: 这个小工具，就是个显示框，小窗口，把图像大小显示到指定的显示框   
label = tk.Label(root, image=tk_image, width=w_box, height=h_box)  
#padx,pady是图像与窗口边缘的距离   
label.pack(padx=5, pady=5)  

label2 = tk.Label(root, image=tk_image, width=w_box, height=h_box)  
#padx,pady是图像与窗口边缘的距离   
label2.pack(padx=5, pady=20)  

root.mainloop()  
