import random

def main():
    print("Hello! Welcome to Yes or No Therapy. This is obviously not your traditionally therapy. This is a program to guide you to success in your life.\n The best part is all you have to do is 'yes' or 'no'.\n Disclaimer: Unfortunately this program wasn't built for complex issues it is a simple program to help with simple guidance towards users to gidn solutions to their own life.\n ONE LAST THING: MAKE SURE YOU DON'T PRESS SPACE BEFORE TYPING IN THE LETTER.")
    choice = input("Would you like to proceed? ['yes'  'no']: ")
    if(choice == 'yes'):
        name = input('Great! What is your name?: ')
        session(name)
    elif(choice == 'no'):
        print("It's fine see you another time THANK YOU!!")



def session(user_name):
    choice = input("So, "+ user_name + " How do you feel?\n Pick an emotion you are currently feeling: [a: 'I feel sad'     b: 'I feel worried'     c: 'I feel angry' d: 'I don't know']")
    if choice == 'd':
        choice = input('It is completely fine to not know how you feel. This is an amazing opportunity because the problem is one but the solutions for it is infinite.\n Here is an exercise you should try. Try writing down here the best description of how you feel. Try your best! DO NOT PRESS ENTER UNTIL YOU ARE FINISHED.')
        choice = input("Awesome I hope you came up with some brilliant findings with your inner self. Once you feel that you have found something that matches the emotions of sadness, worry, or anger. You can press 'y' to restart the session and you will be able to navigate from there. Enjoy! [Press y to restart]")
        if choice == 'y':
            main()
    elif choice == 'a':
        choice = input('Are you sad all the time? [y: yes     n: no]:')
        if choice == 'y':
            choice = input('It is possible someone can feel an emotion,\nbut the way our emotions work, you are likely to feel many emotions, not the same one forever\nSo can you tell me if recently there was a time where u had even a LITTLE bit of joy?\n[y: yes     n: no]:')
            if choice == 'y':
                choice = input('Awesome, I have an exercise for you, write down all the things in your life that make you happy(even if it is a little bit. Once you do that, do those things everyday and what your life feel a lot more joyful\n DONT CLICK ENTER UNTIL YOU ARE FINISHED')
                print('Great! Thank you ' + user_name + ' I am glad you finished the exercise, Unfortunately this is the end of the session. My job was to guide you to find the answer to your issues yourself.\n  I hope  I was able to do that for you. With the power of writing things down you will find yourself answering your own questions and finding your own solutions. Enjoy your life and always stay positive!')
        elif choice == 'n':
            choice = input('Great, there is a lot of room now to fix this. I have an exercise for you to try to improve on this. [y: proceed]') 
            if choice == 'y':
                choice = input('What I want you to start doing is pay attention to what makes you happy \nand what makes you sad and write it down. You do not feel sad all the time\n so that means you are going to make sure you prioritize doing things that will make you happy. DO NOT PRESS ENTER UNTIL YOU ARE DONE')
                print('Great! Thank you ' + user_name + ' I am glad you finished the exercise, Unfortunately this is the end of the session. My job was to guide you to find the answer to your issues yourself.\n  I hope  I was able to do that for you. With the power of writing things down you will find yourself answering your own questions and finding your own solutions. Enjoy your life and always stay positive!')
    elif choice == 'b':
        choice = input('Do you feel that you messed up something in the future? [y: yes     n: no]:')
        if choice == 'y':
            choice = input('Everyone in their life has made a mistake in the past that they regreted doing? However, overtime it individuals will get over it as long as they focus on their personal growth. Do you feel like you are growing and improving in life? [y: yes     n: no]:')
            if choice == 'y':
                choice = input('Great! I have an exercise for you to do for you to continue to grow to the point where you will be able to overcome any emotional struggle in your life.\n [y: proceed]:')
                if choice == 'y':
                    choice = input('I want you to take some time to list out things that you do in your daily life that \nhelp you grow and be a better person, after you to write that down start working towards these new goals you have written. You will find yourself feeling a lot better overtime. DO NOT PRESS ENTER UNTIL YOU ARE FINISHED')
                    print('Great! Thank you ' + user_name + ' I am glad you finished the exercise, Unfortunately this is the end of the session. My job was to guide you to find the answer to your issues yourself.\n  I hope  I was able to do that for you. With the power of writing things down you will find yourself answering your own questions and finding your own solutions. Enjoy your life and always stay positive!')
        elif choice == 'n':
            choice = input('Usually worry comes from a future outcome so I want you to think a bit deeper into the worry. Try to do this deep thinking exercise[y: proceed')
            if choice == 'y':
                choice = input('I want you to list out a few things you are worried about. After you do that, look at your list and try to find the things you can work on to help improve your future.\n You will feel more confident DO NOT PRESS ENTER UNTIL DONE:')
                print('Great! Thank you ' + user_name + ' I am glad you finished the exercise, Unfortunately this is the end of the session. My job was to guide you to find the answer to your issues yourself.\n  I hope  I was able to do that for you. With the power of writing things down you will find yourself answering your own questions and finding your own solutions. Enjoy your life and always stay positive!')
    elif choice == 'c':
        choice = input('Are you angry about the past? y: yes     n: no]:')
        if choice == 'y':
            choice = input('Makes sense usually people are angry over something that has happened.\nDo you feel any control over this situation that makes you angry? [y: yes     n: no]:')
            if choice == 'y':
                choice = input('This is amazing that you feel this way, you are now on a good pace when it comes to fixing this emotion.\n I have an amazing exercise for you to tackle all the challege because I know you are confident enough to take on any battle that comes your way [y: proceed]')
                if choice == 'y':
                    choice == input('I want you to list out all the things you have control over. Most likely if your mind feels like you have control over something. That means that you are definitely going to be able to fix it. DO NOT PRESS ENTER UNTIL YOU ARE DONE.')
                    print('Great! Thank you ' + user_name + ' I am glad you finished the exercise, Unfortunately this is the end of the session. My job was to guide you to find the answer to your issues yourself.\n  I hope  I was able to do that for you. With the power of writing things down you will find yourself answering your own questions and finding your own solutions. Enjoy your life and always stay positive!')
        elif choice == 'n':
            choice = input('Majority of the time when people are angry and they think it is for the future, usually it actually is because of a previous event that triggered the emotion.\nIt could be you are angry at a potential future event but the reason for the emotion has to do with something you have dealt with\nthat is leading you to feel this way.\n With that being said I have an exercise that will help you find out what that past event is that is making you angry? [y: proceed]')
            if choice == 'y':
                choice = input('Awesom, I want you to write down here what are the previous events that trigger you. Once you can come up with the list I want you to do some deep thinking into why it is affecting you in this way and you will realize that the past is not worth it to ruin your mood for the present and future because the past is uncontrollable now.: DO NOT PRESS ENTER UNITL YOU ARE DONE')
                print('Great! Thank you ' + user_name + ' I am glad you finished the exercise, Unfortunately this is the end of the session. My job was to guide you to find the answer to your issues yourself.\n  I hope  I was able to do that for you. With the power of writing things down you will find yourself answering your own questions and finding your own solutions. Enjoy your life and always stay positive!')





        

main()




    


        





    



