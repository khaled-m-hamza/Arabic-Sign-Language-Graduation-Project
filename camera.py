

from flask import Flask, render_template
import cv2
import torch
import numpy as np
from bidi.algorithm import get_display
import arabic_reshaper
import keyboard





lst=['ع', 'ال', 'ا','ب','د','ظ','ض','ف','ق','غ','ه','ح','ج','ك','خ','لا','ل',
        'م','ن','ر','ص','س','ش','ت','ط','ث','ذ','ة','و','ى','ي','ز']



        
#model = torch.hub.load('ultralytics/yolov5', 'custom', path='khaled.pt')
model = torch.hub.load('ultralytics/yolov5', 'custom', path='khaled.pt')

#model = YOLO('new.pt')
class VideoCamera(object):
    def __init__(self):
        
        self.video = cv2.VideoCapture(0)
       
        self.new= [' ']
        
    
        
        
    def __del__(self):
        self.video.release()
    
    def text(self):
       y=self.new
       
       
       return y
    def get_frame(self):
        #new = []
        success, image = self.video.read()
        #obj=VideoCamera()
        results = model(image)
                 # Access the class labels
        if keyboard.is_pressed('d'):
              self.new = self.new[:-1]
              print("last element deleted")
        if keyboard.is_pressed('s'):
              self.new.append(' ')
              print("space is appended in list")
        if keyboard.is_pressed('x'):
              self.new.append(self.new[-1])
              print("the last letter is repeted")
      
        for result in results.xyxy[0]:
        
           
           num = int(result[-1])  
           label=lst[num]
        
    
           print(label)
          
           
           cv2.imshow('YOLO',np.squeeze(results.render()))
           
           
           if label != self.new[-1]:
             self.new.append(label)
             
             print("list is apeended now")
           else :
               
            print("this element allready exist")
            pass
       
                                                                                                                                                                                              
        new=self.new
        
        
        print(new)  
          
           
        
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
        
    
      







