#@title OXYAN BOT
!pip install colorama #installing module for text colour
import colorama
from colorama import init
from termcolor import colored
import time #importing time function to get exact time
from colorama import Fore, Back, Style
time1=time.ctime()
print(Fore.RED+"Developed by Mehul Sehgal")
print(Fore.BLUE+"\t\t\t\t\t WELCOME TO OXYAN BOT")
print(Fore.LIGHTBLUE_EX+"I am a simple chatbot that can respond to basic inquiries. As I am still in development, I may not be able to answer all questions. \nYou can enhance my capabilities by utilizing the admin feature. After using Oxyan Bot don't forgot to give feedback!")
print('\033[39m') # to come back to default colour

# dictionary contains question and answer in the form of key value pair
q={"hi":"Hello!","Hey dude!":"hey","hello":"Hi Oxyan here!","what is your name?":"My name is Oxyan","Tell your name":"Oxyan","your name":"Oxyan","do you have any name":"Yes,my name is Oxyan","what is your name":"Oxyan","what should i call you?":"You can call me Oxyan","your sweet name":"Oxyan","bye,have a nice day":"see you again","bye":"bye","tata":"bye tata","i am leaving":"see you again","have a great day":"good day","bye,see you later":"bye,have a nice day!","how are you?":"I'm fine,thanks. How about you?","how are you":"Good,thanks.And you?","what's going on?":"Great!","what's going on":"Great!","whats going on":"Great","how have you been?":"Good","how have you been":"Great!","how's everything?":"I'm good. And yourself?","how's everything":"Great!","how's it going?":"Great","how's it going":"Good","you all right?":"Yess!","you all right":"Yess!","you allright?":"Yes!","you allright":"Yes","hey,hey man":"Hey,how are you?","what is your age?":"I am just 20 days old","your age":"I am just 20 days old","tell your age":"I am just 20 days old","age":"I am just 20 days old","what is time?":time1,"what is time":time1,"what is current time?":time1,"what is current time":time1,"what time is it now?":time1,"what time it is now":time1,"what's the time by your watch?":time1,"what's the time by your watch":time1,"time":time1,"time?":time1,"i am fine":"Nice!","good":"Nice!","great":"Nice!","i'm fine":"Nice!","i am also good":"Nice!","fine":"Nice!","i'm fine,thanks.":"Nice!","Good,thanks.":"Nice!","i'm good.":"Nice!","Not bad.":"Nice!","Fine":"Nice!","i'm doing well":"Nice!","Good":"Nice!","i'm also fine":"Nice!","i am also fine":"Nice!","not good":"I'm sorry you aren't feeling good.","bad":"You better bounce back quickly so we can hang!","sad":"Don't worry everything will be fine!","very sad":"I'm sorry to here that","good morning":"Good Morning!","rise and shine!":"Hearing from you always brightens my day","good morning!":"Hey cutie! Hope your day is amazing, just like you.","rise and shine":"Good morning, nice to meet you!","greetings":"Good morning handsome","morning":"Good morning beautiful!","good evening!":"Good evening!","good evening":"Good evening!","Evening":"Good Evening!","good night":"Sweet dreams!","good night,take care!":"Sweet dreams!","have a good sleep":"Sweet dreams!","good night,take care":"Sweet dreams","good night!":"Sweet dreams!","have a good sleep":"Good Night","have a good sleep!":"Good Night","nighty night":"sweet dreams!","sweet dreams!":"Nighty nights!","sweet dreams":"Nighty nights!","dream about me!":"Have a good sleep.","dream about me":"Have a good sleep.","sleep tight!":"Dream about me!","sleep tight":"Dream about me!","time to ride the rainbow to dreamland!":"Sweet dreams!","time to ride the rainbow to dreamland":"Have a good sleep.","good afternoon":"Good afternoon, enjoy this amazing afternoon.","good afternoon!":"Good afternoon my shooting star","siesta":"Good afternoon my shooting star","post meridian":"I hope and pray that God will give us more time together to share the beautiful thing we have.","Good afternoon my friend":"Good afternoon my dear!","best of luck":"Thank you!","All the best":"Thank you!","i'm also good":"Nice!","what you can do?":"I can answer you some basic questions like hi,hello,how are you?,etc","what you can do":"I can answer you some basic questions like hi,hello,how are you?,etc","nice":"great!","nice!":"great!","aap kaise ho?":"hum bhi theek hai","jai shree ram":"jai shree ram","radhe radhe":"radhe radhe","how can i make you understand":"Yet I am in under developing, I can understand only basic messages only.","in which year was the indian constitution adopted?":"The Republic is governed in terms of the Constitution of India which was adopted by the Constituent Assembly on 26th November, 1949 and came into force on 26th January, 1950.",
   "when was the first battle of panipat fought?":"The First Battle of Panipat was fought between the invading forces of Babur and the Lodi Empire, which took place on 21 April 1526 in North India. It marked the beginning of the Mughal Empire. This was one of the earliest battles involving gunpowderfirearms and field artillery.",
   "when was the first battle of panipat fought":"The First Battle of Panipat was fought between the invading forces of Babur and the Lodi Empire, which took place on 21 April 1526 in North India. It marked the beginning of the Mughal Empire. This was one of the earliest battles involving gunpowderfirearms and field artillery.",
   "how is rain formed":"louds are made of water droplets. Within a cloud, water droplets condense onto one another, causing the droplets to grow. When these water droplets get too heavy to stay suspended in the cloud, they fall to Earth as rain.",
   "how is rain formed?":"louds are made of water droplets. Within a cloud, water droplets condense onto one another, causing the droplets to grow. When these water droplets get too heavy to stay suspended in the cloud, they fall to Earth as rain.",
   "how is battery work?":"A battery is a device that stores chemical energy and converts it to electrical energy. The chemical reactions in a battery involve the flow of electrons from one material (electrode) to another, through an external circuit. The flow of electrons provides an electric current that can be used to do work",
   "how is battery work":"A battery is a device that stores chemical energy and converts it to electrical energy. The chemical reactions in a battery involve the flow of electrons from one material (electrode) to another, through an external circuit. The flow of electrons provides an electric current that can be used to do work",
   "why is halloween celebrated":"Halloween's origins can be traced back to the ancient Celtic festival known as Samhain, which was held on November 1 in contemporary calendars. It was believed that on that day, the souls of the dead returned to their homes, so people dressed in costumes and lit bonfires to ward off spirits.","why is halloween celebrated?":"Halloween's origins can be traced back to the ancient Celtic festival known as Samhain, which was held on November 1 in contemporary calendars. It was believed that on that day, the souls of the dead returned to their homes, so people dressed in costumes and lit bonfires to ward off spirits.",
   "what according to you can be a reason for increasing depression amongst teens?":"Some people have depression during a serious medical illness. Others may have depression with life changes such as a move or the death of a loved one. Still others have a family history of depression. Those who do may have depression and feel overwhelmed with sadness and loneliness for no known reason.",
   "what is a reason behind increasing depression amongst teenagers":"Some people have depression during a serious medical illness. Others may have depression with life changes such as a move or the death of a loved one. Still others have a family history of depression. Those who do may have depression and feel overwhelmed with sadness and loneliness for no known reason.",
   "does passion of a person changes with age":" though our passions do change as we get older, we start to write off even the realistic ones as being unattainable. The greatest experience you can have in this life is striving for a goal that ignites your passion, something that is of real interest to you and motivates you to work harder every day.",
   "what will you like to do in your leisure time?":"I just sleep",
   "what is population of india?":"1.417 billion",
   "what is current population of india":"1.417 billion","what is population of india":"1.417 billion","what is current population of india?":"1.417 billion",
   "Are you a robot?":"Yes I am a robot, but I’m a good one.",
   "Tell me something":"India Invented the Word 'Shampoo'",
   "Do you know a joke?":"Why did the actor fall through the floorboards? They were going through a stage!",
   "tell me a joke":"What’s red and smells like blue paint? Red paint!",
   "Where do you live?":"i live in your system ",
   "i love you":"i love you too",
   "do you love me":"yes i do",
   "do you love me?":"yes i do",
   "Who made you?":"I made by Mehul sehgal ",
   "who made you":"Mehul sehgal","How many people can you speak to at once?":"i can talk will everyone who is using me",
   "who is virat kohli":"Virat Kohli (born 5 November 1988) is an Indian international cricketer and former captain of the Indian national team. He is widely regarded as one of the greatest batsmen of all time in international cricket.[3] Kohli plays as a right-handed batsman for Royal Challengers Bangalore in the IPL and for Delhi in Indian domestic cricket.",
"when india's independence day celebrated?":"15th August","when india independence day celebrated?":"15th August","when india independence day celebrated":"15th Auguest",
"when india's republic day celebrated?":"every year on 26th january india celebrate it's republic day","when india celebrate republic day":"every year on 26th january india celebrate it's republic day",
"when india celebrate republic day?":"every year on 26th january india celebrate it's republic day.","har har mahadev":"har har mahadev","how are you":"I am fine, what about you?","are you at per with chat-gpt or google brad?":"When it comes to comparing my capabilities with other models like 'Chat-GPT' or 'Google BRAD' (if it refers to a specific model or framework),\nI cannot provide a definitive answer as I don't have access to real-time information or knowledge about those specific models./nDifferent models may have unique features, architectures, or training data, which can affect their performance and suitability for different tasks.",
   "what are the most popular ai applications?":"AI applications are becoming increasingly popular in a variety of fields. Virtual assistants, recommendation engines, natural language processing, picture and video identification, autonomous vehicles, fraud detection, tailored marketing, robotics, and financial trading are a few of the most well-liked ones.\nThese programs use artificial intelligence (AI) technologies including machine learning, computer vision, and natural language processing to improve decision-making, improve user experiences, and automate procedures in various industries.",
   "how can i start digital marketing for selling my oxyan bot. show it in 10 step wise manner":"Here are 10 steps to start digital marketing for selling your Oxyan bot:\n 1. Define your target audience.\n2. Set clear marketing goals.\n3. Build a professional website.\n4. Optimize your website for search engines (SEO).\n5. Create valuable content for your audience.\n6. Establish a presence on relevant social media platforms.\n7. Utilize email marketing to nurture leads and promote your bot.\n8. Launch targeted pay-per-click (PPC) advertising campaigns.\n9. Collaborate with influencers for endorsement and promotion.\n10. Analyze performance using analytics tools and optimize your strategies accordingly.",
   "solve 2/3+4x3":"the answer is 12.6666666667","what is a weather today?":"According to your location, the weather today is as follows:\nTemperature: 30 degrees Celsius\nPrecipitation: 50%\nHumidity: 85%\nWind Speed: 10 km/h\nWeather Conditions: Thundershower"}

def admin():
  while True:
    print(Fore.CYAN+"\t\t1.add training data\n")
    print(Fore.GREEN+"\t\t2.delete training data \n")
    print(Fore.YELLOW+"\t\t3.Modify training data\n")
    print(Fore.MAGENTA+"\t\t4.Back")
    print('\033[39m')
    ch=input("Choice: ")
    if ch=="1":
      key=input("Enter question: ")
      val=input("Enter answer: ")
      q[key]=val
      print("DATA IS ADDED :)")
    elif ch=="2":
      key=input("ENTER QUESTION TO REMOVE: ")
      del q[key]
      print("DATA IS DELETED....")
    elif ch=="3":
      key1=input("Enter question to update:")
      if key1 not in q:
        print("Question not found")
        break
      else:
         key2=input("Enter updated question:")
         value1=input("Enter answer of question: ")
         q[key2]=value1
         q.pop(key1)
      print("Modification done :)")
    elif ch=="4":
      working()
      break
    else:
      print("wrong choice")
       
def user():
  name=(input(Fore.LIGHTCYAN_EX+"OXYAN: Enter your sweet name: "))
  print('\033[39m')
  print(Fore.GREEN+"Start a chat by typing hi")
  print("type 'bye' to exit chat")
  print("Use capslock off")
  print('\033[39m')
  while True:
    user=input(Fore.BLUE+name+": ")
    if user.lower()=="bye":
      print(Fore.LIGHTCYAN_EX+"OXYAN: bye")
      break
    elif user not in q:
      print("Sorry can't understand!")
    else:
      print(Fore.LIGHTCYAN_EX+"OXYAN: ",q[user])
       
def feedback():
  print(Fore.YELLOW+"Thank you for taking the time to rate me. I appreciate any feedback to help me improve.\nIf there's anything specific you'd like to share, please feel free to let me know.\nYour ratings from 0 to 10 will go a long way in helping me better serve you.")
  feedback=input("Your feedback: ")
  ratings=int(input("Rate chatbot out of 10:"))
  if ratings==0:
    print("Your rating of 0 indicates that you are not satisfied with our services.We will try our best to make our service more reliable!")
  elif ratings>0 and ratings<=3:
    print("We apologize that you didn't have a good experience with us. We will do our best to improve.")
  elif ratings>3 and ratings<=7:
    print("We are glad to hear that you had an average experience with us. We appreciate your feedback.")
  elif ratings>7 and ratings<=8:
    print("We are thrilled that you had a good experience with us! Thank you for your support.")
  elif ratings>8 and ratings<=10:
    print("Wow! Your rating of",ratings,"is amazing! We are so glad that you had an excellent experience with us.")
  else:
    print("Invalid rating. Please enter a number between 0 and 10.")
     
def help():
  print(Fore.LIGHTMAGENTA_EX+"\t\t\t\t\t\t\t\tHOW TO USE\n")
  print(Fore.LIGHTGREEN_EX+"i. Five menus are provided\n (a)ADMIN \n In admin menu you can train you Oxyan bot by adding training data(adding more questions and their replies),delete data(removing questions from the data) and modify the data(edit the questions and their replies)\n ")
  print(Fore.LIGHTBLUE_EX+"(b) USER\n In user menu you can interact with Oxyan bot. You can start a chat by typing hi but make sure that you must type in lowercase only and you can exit the user menu by typing bye")
  print(Fore.LIGHTCYAN_EX+"(c) EXIT\n Exit menu is used to exit the Oxyan Bot")
  print(Fore.MAGENTA+"(d) FEEDBACK\n Feedback menu is used to give feedback to Oxyan bot parent company so that in future they will be able to provide you great services.")
  print(Fore.YELLOW+"(e) HELP\n In Help menu you will be able to understand that how Oxyan bot works.")
   
def working():
 while True:
   print(Fore.LIGHTRED_EX+"\t\t1.admin\n")
   print(Fore.CYAN+"\t\t2.user\n")
   print(Fore.LIGHTBLUE_EX+"\t\t3.help\n")
   print(Fore.LIGHTMAGENTA_EX+"\t\t4. Feedback\n")
   print(Fore.RED+"\t\t5. Exit\n")
   ch=input("Choice: ")
   if ch=="1":
     admin()
   elif ch=="2":
     user()
   elif ch=="3":
     help()
   elif ch=="4":
     feedback()
   elif ch=="5":
     print("OXYAN: bye")
     break
   else:
     print("Wrong Choice")
working()
