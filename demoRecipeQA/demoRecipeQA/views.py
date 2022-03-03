from django.shortcuts import render
import requests
import sys
import subprocess
from subprocess import run,PIPE
from django.core.files.storage import FileSystemStorage
def button(request):
      return render(request,'home.html')
def output(request):
      data=requests.get("https://www.google.com/")
      print(data.text)
      data=data.text
      return render(request,'home.html',{'data':data})
def external(request):
      inp= request.POST.get('param')
      image=request.FILES.get('image',False)
      print("image is ",image)
      fs=FileSystemStorage()
      if image!= False :
          filename=fs.save(image.name,image)
          fileurl=fs.open(filename)
          templateurl=fs.url(filename)
      #     testurl='C:\Users\palad\OneDrive\Desktop\ProjectVed\demo_RecipeQA\demoRecipeQA\data\images\egg-drop-chicken-noodle-soup\egg-drop-chicken-noodle-soup_2_0.jpg'
          print("file raw url",filename)
          print("file full url", fileurl)
          print("template url",templateurl)
          out= subprocess.Popen([sys.executable,'C:\\Users\\palad\\OneDrive\\Desktop\\ProjectVed\\demo_RecipeQA\\demoRecipeQA\\querysys.py',str(fileurl)],shell=False,stdout=subprocess.PIPE)
          text = out.communicate()[0].decode('utf-8').split("\r\n")
          print("text",text)
      #     for i in text.splitlines():
      #           a = i
      #     a = list(a[1:-1].split(","))
          a = []
          names = []
          images = []
          for each in text:
                a.append(each[3:].split(" "))
                
          for each in a:
                if each!=['']:
                  names.append(each[0:2][0])
                  images.append(each[0:2][1])
                  

          
          return render(request,'home.html',{'mainData':out.stdout,'UploadedImage':templateurl,'mainData':out.stdout,'data':names[0],'images':images[0].replace("C:\\Users\\palad\\OneDrive\\Desktop\\ProjectVed\\demo_RecipeQA\\demoRecipeQA",""),'data1':names[1],'images1':images[1].replace("C:\\Users\\palad\\OneDrive\\Desktop\\ProjectVed\\demo_RecipeQA\\demoRecipeQA",""),'data2':names[2],'images2':images[2].replace("C:\\Users\\palad\\OneDrive\\Desktop\\ProjectVed\\demo_RecipeQA\\demoRecipeQA","")})
      #     return render(request,'home.html',{'data':a[0],'image':a[1],'com':a[2]})
      else:
      #     out= run([sys.executable,'C:\\Users\\palad\\OneDrive\\Desktop\\ProjectVed\\demo_RecipeQA\\demoRecipeQA\\querysys.py',inp],shell=False,stdout=PIPE)
      #     return render(request,'home.html',{'data':out.stdout})
          out= subprocess.Popen([sys.executable,'C:\\Users\\palad\\OneDrive\\Desktop\\ProjectVed\\demo_RecipeQA\\demoRecipeQA\\querysys.py',inp],stdout=subprocess.PIPE)
          text = out.communicate()[0].decode('utf-8').split("\r\n")
          print("text",text)
      #     for i in text.splitlines():
      #           a = i
      #     a = list(a[1:-1].split(","))
          a = []
          names = []
          images = []
          for each in text:
                a.append(each[3:].split(" "))
                
          for each in a:
                if each!=['']:
                  names.append(each[0:2][0])
                  images.append(each[0:2][1])
                  

          
          return render(request,'home.html',{'mainData':out.stdout,'data':names[0],'images':images[0].replace("C:\\Users\\palad\\OneDrive\\Desktop\\ProjectVed\\demo_RecipeQA\\demoRecipeQA",""),'data1':names[1],'images1':images[1].replace("C:\\Users\\palad\\OneDrive\\Desktop\\ProjectVed\\demo_RecipeQA\\demoRecipeQA",""),'data2':names[2],'images2':images[2].replace("C:\\Users\\palad\\OneDrive\\Desktop\\ProjectVed\\demo_RecipeQA\\demoRecipeQA","")})
      #     return render(request,'home.html',{'data':a[0],'image':a[1],'com':a[2]})