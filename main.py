import speech_recognition as sr
import pyttsx3
import mysql.connector
import sys

mydb = mysql.connector.connect(host="localhost", user="root",passwd="Bimleshpal@99",database="student")
mycursor=mydb.cursor()
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
print("Hello my name is Evya \nwhat do you want \n1.show data \n2.edit \n3.Delete \n4.exit")
engine.say("Hello my name is eev-ya \n\nwhat do you want \nshow data \nedit \nDelete \nexit")
engine.runAndWait()
value = 0
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    global value
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()


            if 'number' in command:
                command = command.replace('number', '')  # this is for returning command
                print(command)
                print("here is your result")
                engine.say("here is your resultr")
                engine.runAndWait()
                n = int(command)
                mycursor.execute("select * from student_info where roll_no = %s" % n)
                result = mycursor.fetchall()
                for i in result:
                    print(i)

                take_command()

            if 'show' in command :
                command = command.replace('number', '')  # this is for returning command
                print(command)
                print("tell me roll no:")
                engine.say("tell me roll number")
                engine.runAndWait()
                run_alexa()


            """if 'show' in command:  # this is for her name
                command = command.replace('alexa', '')  # this is for returning command
                print(command)
                print("tell me roll number")
                engine.say("tell me roll number")
                engine.runAndWait()
                #command = command.replace('alexa', '')  # this is for returning command
                #print(command)

                #print('listening...')
                '''voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()'''
                take_command()

                run_alexa()"""

            if 'edit' in command:  # this is for her name
                command = command.replace('alexa', '')  # this is for returning command
                print(command)

                name = input("full name :")
                str(name)
                roll = input("roll no . : ")
                clg_id = input("college id : ")
                str(clg_id)
                sem = input("current sem : ")
                pn = input("phone no : ")
                pointer = input("pointer : ")
                loc = input("location : ")
                str(loc)
                fees = input("fees (paid/not paid) : ")
                str(fees)

                # ins = ("insert into student_info values(%s,%s,%s,%s,%s,%s,%s,%s);",(roll,name,clg_id,sem,pn,float(pointer),loc,fees))
                mycursor.execute("insert into student_info values(%s,%s,%s,%s,%s,%s,%s,%s);",(roll, name, clg_id, sem, pn, float(pointer), loc, fees))
                mydb.commit()

                run_alexa()

            if 'delete' in command :
                command = command.replace('evya', '')  # this is for returning command
                print(command)

                engine.say("tell me roll number")
                engine.runAndWait()

                roll_no = input("roll no . : ")
                query = "delete from student_info where Roll_no= {}".format(roll_no)
                mycursor.execute(query )
                mydb.commit()

                run_alexa()

            if 'exit' in command:  # this is for her name
                command = command.replace('alexa', '')  # this is for returning command
                print(command)
                value = 1
                #value = 0
                #exit()
                sys.exit()

            else:
                run_alexa()

    except :
        pass
    #return command
#def callingend():
  #  end()
def run_alexa():
    #print("kjkj")
    global value
    if value == 1  :
    #if 'exit' in command :
        print("succesfully exited")
        sys.exit()
    else :
        take_command()
        #command = take_command()
    #print("hey exited")



run_alexa()
#take_command()
#def end():
  #  exit()