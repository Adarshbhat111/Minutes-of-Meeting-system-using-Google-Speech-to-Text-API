import speech_recognition as sr 
r=sr.Recognizer()


def adarsh(x):
    with sr.Microphone() as source:
        print("adarsh is speaking: ")
        audio=r.listen(source,phrase_time_limit=7)

        try:
            text=r.recognize_google(audio)
            print("adarsh just said: {}".format(text))
        
        except:
            print("sorry  couldnt reogninze your voice adarsh please try again try again")  

def akshatha(x) :
    with sr.Microphone() as source:
        print("akshtha is speaking: ")
        audio=r.listen(source,phrase_time_limit=7)
        
        try:
            text=r.recognize_google(audio)
            print("akshatha just said: {}".format(text))
        
        except:
            print("sorry  couldnt reogninze your voice akshatha please try again try again") 
def janardhan(x):
    with sr.Microphone() as source:
        print("janardhan is speaking: ")
        audio=r.listen(source,phrase_time_limit=7)

        try:
            text=r.recognize_google(audio)
            print("janardhan just said: {}".format(text))
        
        except:
            print("sorry  couldnt reogninze your voice janardhan please try again try again")  


y=input("welcome !!! please enter your meeting agenda:")
print("adarsh your speaker id is 1\n")
print("akshatha your speaker id is 2\n")
print("janardhan your speaker id is 3\n")  
print("to exit meeting press 0\n")
print("start your meeting\discussion about "+   y)

while 1:
    
    op=int(input('enter ur speaker id\n'))

    if op==1:
        adarsh(op)
    elif op==2:
        akshatha(op)
    elif op==3:
        janardhan(op)
    elif op==0:
        print('thankyou for ur time lets meet again')
        break
        
    else :
        print('sorry you are not part of our meeting')





  

        

    
        


    



          

       
    

                                      
 