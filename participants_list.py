
from ast import While
from main import zoom
import json
import time
from datetime import datetime
import sendmail
import os


condition=True
roaster=["User1 ","User2","User3"] # assuming the professor user name is the second.

# you have to make two changes.
#1- in roaster add the user name of the professor second
#2- in send email add the professor email in second SendMem.

def main():
    flag=0 
    a=zoom(Key='user',Sec='kkk')
    s_time=datetime.now()
    professor_user=roaster[1]
    send_mail_flag=True
    send_mail_flag1=True
    user_available_flag=True
    professor_flag=True


    b1=a.getStat()
    r = json.loads(b1.text)
    print(r.get('status'))
    print(r.get('in_meeting'))
    print(r.get('id'))
    print(r.get("start_url"))
    print(r.get("join_url"))
    a.getMeetingParticipants()

    sendmail.sendGreet(r.get("join_url"))# Send a Greeting email

    while condition:
        
        b1=a.getStat()
        r = json.loads(b1.text)
        if r.get('status') == 'started':
            # H Lamp On and Lamp off
            c1=a.getMeetingParticipants()
            d = json.loads(c1.text)
            out_list=d.get('participants')
            a_key = "user_name"

            if out_list:
                values_of_key=[]
                values_of_key = [a_dict[a_key] for a_dict in out_list] # list of the meeting participants
                values_of_key = list(dict.fromkeys(values_of_key)) # remove redundancy


                e_time=datetime.now()
                c=e_time-s_time
                minutes = c.total_seconds() / 60

                answer = check_if_equal(roaster, values_of_key)

                if roaster[1] not in values_of_key and minutes > 1 and send_mail_flag:

                    sendmail.sendMem(r.get("join_url"),1)
                    print("Khaled is not in the meeting========")
                    send_mail_flag=False

                if roaster[2] not in values_of_key and minutes > 1 and send_mail_flag1:

                    sendmail.sendMem(r.get("join_url"),2)
                    print("Khaled is not in the meeting========")
                    send_mail_flag1=False

                if answer and user_available_flag:
                    os.system("afplay start.mp3")  # Say start the meeting all partic avaiable
                    user_available_flag=False

                if roaster[1] in values_of_key and professor_flag:
                    os.system("afplay greet.mp3")  # Say hello to the professor.
                    professor_flag=False

        elif r.get('status') =='waiting':
            print("Hi")
            time.sleep(1)


def check_if_equal(list_1, list_2):
    """ Check if both the lists are of same length and if yes then compare
    sorted versions of both the list to check if both of them are equal
    i.e. contain similar elements with same frequency. """
    if len(list_1) != len(list_2):
        return False
    return sorted(list_1) == sorted(list_2)



        
if __name__ == '__main__':
    main()





