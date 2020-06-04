from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk  
import backEnd

root = Tk()  # 创建窗口
root.title('CBIR')
root.geometry('1200x700')

# 显示系统名字
sys_name = Label(root, font =("Times New Roman", 30), text = "遥感图像检索")
sys_name.place(x = 20, y = 15)

# 显示结果标题
res_name = Label(root, font =("Times New Roman", 30), text = "检索TOP12")
res_name.place(x = 400, y = 15)

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

defult_img = 'defult.png'
pil_image = Image.open(defult_img)
w, h = pil_image.size 
pil_image = resize(w, h, 300, 300, pil_image) 
photo = ImageTk.PhotoImage(pil_image) # pic.png就在工程目录里（和.py在同一个文件夹）
img_label = Label(root, imag=photo, width = 300, height = 300)
img_label.place(x=10, y=70)

##
queryImg = ""

def changeImage():#=================================从这里
    global queryImg
    queryImg = filedialog.askopenfilename(filetypes =[("tif文件","*.tif"), ("png文件","*.png"),  ("jpg文件","*.jpg")])
    # print(queryImg)
    global img_label, photo2#要改的label、替换的图片，缺一不可都要global引用！
    pil_image2 = Image.open(queryImg)
    w, h = pil_image2.size 
    pil_image2 = resize(w, h, 300, 300, pil_image2) 
    photo2 = ImageTk.PhotoImage(pil_image2)#pic.png就在工程目录里（和.py在同一个文件夹）
    img_label.configure(imag=photo2)

def retrieval():
  print(queryImg)
  if queryImg == "":
    return
  res_img_path = backEnd.retrieval(queryImg)
  showRetrievalRes(res_img_path)

## 显示结果
def showRetrievalRes(res_img_path):
  exp_size = 180
  global res_image1, Res_photo1, img_label1
  res_image1 = Image.open(res_img_path[0])
  w, h = res_image1.size 
  res_image1 = resize(w, h, exp_size, exp_size, res_image1) 
  Res_photo1 = ImageTk.PhotoImage(res_image1) # pic.png就在工程目录里（和.py在同一个文件夹）
  img_label1 = Label(root, imag=Res_photo1, width = exp_size, height = exp_size)
  img_label1.place(x=400, y=70)

  global res_image2, Res_photo2, img_label2
  res_image2 = Image.open(res_img_path[1])
  w, h = res_image2.size 
  res_image2 = resize(w, h, exp_size, exp_size, res_image2) 
  Res_photo2 = ImageTk.PhotoImage(res_image2) # pic.png就在工程目录里（和.py在同一个文件夹）
  img_label2 = Label(root, imag=Res_photo2, width = exp_size, height = exp_size)
  img_label2.place(x=600, y=70)

  global res_image3, Res_photo3, img_label3
  res_image3 = Image.open(res_img_path[2])
  w, h = res_image3.size 
  res_image3 = resize(w, h, exp_size, exp_size, res_image3) 
  Res_photo3 = ImageTk.PhotoImage(res_image3) # pic.png就在工程目录里（和.py在同一个文件夹）
  img_label3 = Label(root, imag=Res_photo3, width = exp_size, height = exp_size)
  img_label3.place(x=800, y=70)

  global res_image4, Res_photo4, img_label4
  res_image4 = Image.open(res_img_path[3])
  w, h = res_image4.size 
  res_image4 = resize(w, h, exp_size, exp_size, res_image4) 
  Res_photo4 = ImageTk.PhotoImage(res_image4) # pic.png就在工程目录里（和.py在同一个文件夹）
  img_label4 = Label(root, imag=Res_photo4, width = exp_size, height = exp_size)
  img_label4.place(x=1000, y=70)

  global res_image5, Res_photo5, img_label5
  res_image5 = Image.open(res_img_path[4])
  w, h = res_image5.size 
  res_image5 = resize(w, h, exp_size, exp_size, res_image5) 
  Res_photo5 = ImageTk.PhotoImage(res_image5) # pic.png就在工程目录里（和.py在同一个文件夹）
  img_label5 = Label(root, imag=Res_photo5, width = exp_size, height = exp_size)
  img_label5.place(x=400, y=270)

  global res_image6, Res_photo6, img_label6
  res_image6 = Image.open(res_img_path[5])
  w, h = res_image6.size 
  res_image6 = resize(w, h, exp_size, exp_size, res_image6) 
  Res_photo6 = ImageTk.PhotoImage(res_image6) # pic.png就在工程目录里（和.py在同一个文件夹）
  img_label6 = Label(root, imag=Res_photo6, width = exp_size, height = exp_size)
  img_label6.place(x=600, y=270)

  global res_image7, Res_photo7, img_label7
  res_image7 = Image.open(res_img_path[6])
  w, h = res_image7.size 
  res_image7 = resize(w, h, exp_size, exp_size, res_image7) 
  Res_photo7 = ImageTk.PhotoImage(res_image7) # pic.png就在工程目录里（和.py在同一个文件夹）
  img_label7 = Label(root, imag=Res_photo7, width = exp_size, height = exp_size)
  img_label7.place(x=800, y=270)

  global res_image8, Res_photo8, img_label8
  res_image8 = Image.open(res_img_path[7])
  w, h = res_image8.size 
  res_image8 = resize(w, h, exp_size, exp_size, res_image8) 
  Res_photo8 = ImageTk.PhotoImage(res_image8) # pic.png就在工程目录里（和.py在同一个文件夹）
  img_label8 = Label(root, imag=Res_photo8, width = exp_size, height = exp_size)
  img_label8.place(x=1000, y=270)

  global res_image9, Res_photo9, img_label9
  res_image9 = Image.open(res_img_path[8])
  w, h = res_image9.size 
  res_image9 = resize(w, h, exp_size, exp_size, res_image9) 
  Res_photo9 = ImageTk.PhotoImage(res_image9) # pic.png就在工程目录里（和.py在同一个文件夹）
  img_label9 = Label(root, imag=Res_photo9, width = exp_size, height = exp_size)
  img_label9.place(x=400, y=470)

  global res_image10, Res_photo10, img_label10
  res_image10 = Image.open(res_img_path[9])
  w, h = res_image10.size 
  res_image10 = resize(w, h, exp_size, exp_size, res_image10) 
  Res_photo10 = ImageTk.PhotoImage(res_image10) # pic.png就在工程目录里（和.py在同一个文件夹）
  img_label10 = Label(root, imag=Res_photo10, width = exp_size, height = exp_size)
  img_label10.place(x=600, y=470)

  global res_image11, Res_photo11, img_label11
  res_image11 = Image.open(res_img_path[10])
  w, h = res_image11.size 
  res_image11 = resize(w, h, exp_size, exp_size, res_image11) 
  Res_photo11 = ImageTk.PhotoImage(res_image11) # pic.png就在工程目录里（和.py在同一个文件夹）
  img_label11 = Label(root, imag=Res_photo11, width = exp_size, height = exp_size)
  img_label11.place(x=800, y=470)

  global res_image12, Res_photo12, img_label12
  res_image12 = Image.open(res_img_path[11])
  w, h = res_image12.size 
  res_image12 = resize(w, h, exp_size, exp_size, res_image12) 
  Res_photo12 = ImageTk.PhotoImage(res_image12) # pic.png就在工程目录里（和.py在同一个文件夹）
  img_label12 = Label(root, imag=Res_photo12, width = exp_size, height = exp_size)
  img_label12.place(x=1000, y=470)







 
button_change = Button(root, font = 15, text = '选择图片',command=changeImage)
button_change.place(x=102, y=400)

button_retrieval = Button(root, font = 15, text = '开始检索',command=retrieval)
button_retrieval.place(x=102, y=450)



##  结果显示区
exp_size = 180
res_image1 = Image.open(defult_img)
w, h = res_image1.size 
res_image1 = resize(w, h, exp_size, exp_size, res_image1) 
Res_photo1 = ImageTk.PhotoImage(res_image1) # pic.png就在工程目录里（和.py在同一个文件夹）
img_label1 = Label(root, imag=Res_photo1, width = exp_size, height = exp_size)
img_label1.place(x=400, y=70)

res_image2 = Image.open(defult_img)
Res_photo2 = ImageTk.PhotoImage(res_image2) # pic.png就在工程目录里（和.py在同一个文件夹）
img_label2 = Label(root, imag=Res_photo2, width = exp_size, height = exp_size)
img_label2.place(x=600, y=70)

res_image3 = Image.open(defult_img)
Res_photo3 = ImageTk.PhotoImage(res_image3) # pic.png就在工程目录里（和.py在同一个文件夹）
img_label3 = Label(root, imag=Res_photo3, width = exp_size, height = exp_size)
img_label3.place(x=800, y=70)

res_image4 = Image.open(defult_img)
Res_photo4 = ImageTk.PhotoImage(res_image4) # pic.png就在工程目录里（和.py在同一个文件夹）
img_label4 = Label(root, imag=Res_photo4, width = exp_size, height = exp_size)
img_label4.place(x=1000, y=70)

res_image5 = Image.open(defult_img)
Res_photo5 = ImageTk.PhotoImage(res_image5) # pic.png就在工程目录里（和.py在同一个文件夹）
img_label5 = Label(root, imag=Res_photo5, width = exp_size, height = exp_size)
img_label5.place(x=400, y=270)

res_image6 = Image.open(defult_img)
Res_photo6 = ImageTk.PhotoImage(res_image6) # pic.png就在工程目录里（和.py在同一个文件夹）
img_label6 = Label(root, imag=Res_photo6, width = exp_size, height = exp_size)
img_label6.place(x=600, y=270)

res_image7 = Image.open(defult_img)
Res_photo7 = ImageTk.PhotoImage(res_image7) # pic.png就在工程目录里（和.py在同一个文件夹）
img_label7 = Label(root, imag=Res_photo7, width = exp_size, height = exp_size)
img_label7.place(x=800, y=270)

res_image8 = Image.open(defult_img)
Res_photo8 = ImageTk.PhotoImage(res_image8) # pic.png就在工程目录里（和.py在同一个文件夹）
img_label8 = Label(root, imag=Res_photo8, width = exp_size, height = exp_size)
img_label8.place(x=1000, y=270)

res_image9 = Image.open(defult_img)
Res_photo9 = ImageTk.PhotoImage(res_image9) # pic.png就在工程目录里（和.py在同一个文件夹）
img_label9 = Label(root, imag=Res_photo9, width = exp_size, height = exp_size)
img_label9.place(x=400, y=470)

res_image10 = Image.open(defult_img)
Res_photo10 = ImageTk.PhotoImage(res_image10) # pic.png就在工程目录里（和.py在同一个文件夹）
img_label10 = Label(root, imag=Res_photo10, width = exp_size, height = exp_size)
img_label10.place(x=600, y=470)

res_image11 = Image.open(defult_img)
Res_photo11 = ImageTk.PhotoImage(res_image11) # pic.png就在工程目录里（和.py在同一个文件夹）
img_label11 = Label(root, imag=Res_photo11, width = exp_size, height = exp_size)
img_label11.place(x=800, y=470)

res_image12 = Image.open(defult_img)
Res_photo12 = ImageTk.PhotoImage(res_image12) # pic.png就在工程目录里（和.py在同一个文件夹）
img_label12 = Label(root, imag=Res_photo12, width = exp_size, height = exp_size)
img_label12.place(x=1000, y=470)


 
root.mainloop()
