import speech_recognition as sr 
r=sr.Recognizer()


def speaker1(x):
    with sr.Microphone() as source:
        print("speaker1 is speaking: ")
        audio=r.listen(source,phrase_time_limit=7)

        try:
            text=r.recognize_google(audio)
            print("Speaker1 just said: {}".format(text))
        
        except:
            print("sorry  couldnt reogninze your voice speaker1 . Can you please speak again?") 
            speaker1(x) 
  
def speaker2(x) :
    with sr.Microphone() as source:
        print("speaker2 is speaking: ")
        audio=r.listen(source,phrase_time_limit=7)
        
        try:
            text=r.recognize_google(audio)
            print("speaker2 just said: {}".format(text))
        
        except:
            print("sorry  couldnt reogninze your voice speaker2 please speak again  ?") 
            speaker2(x)

def speaker3(x):
    with sr.Microphone() as source:
        print("speaker3 is speaking: ")
        audio=r.listen(source,phrase_time_limit=7) 

        try:
            text=r.recognize_google(audio)
            print("speaker3 just said: {}".format(text))
        
        except:
            print("sorry  couldnt reogninze your voice speaker3 please speak again ?") 
            speaker3(x) 


y=input("welcome !!! please enter your meeting agenda:")
print("speaker1 your speaker id is 1\n")
print("speaker2 your speaker id is 2\n")
print("speaker3 your speaker id is 3\n")  
print("to exit meeting press 0\n")
print("start your meeting\discussion about "+ y)
print("\n")


while 1:
    
    op=int(input('enter ur speaker id\n'))

    if op==1:
        speaker1(op)
    elif op==2:
        speaker2(op)
    elif op==3:
        speaker3(op)
    elif op==0:
        print('thankyou for ur time lets meet again')
        break
        
    else :
        print('sorry you are not part of our meeting')





  

        

    
        


    



          

       
    

                                      
 
