from django.shortcuts import render
import datetime,random
# Create your views here.
def astro(res):
    time=datetime.datetime.now()
    name=input("Enter the ur name:")
    lst=['Tomorrow u will get job',
         'U wil marry after the 5 yaers',
         'Ur very good ',
         'ur weight is good ',
         'Your body is is thin',
         'UR voice becomes hard',
         'Radha krisha likes u',
         'U got MNC company job']
    future=random.choice(lst)
    h=int(time.strftime('%H'))
    if(h<12):
        wish="Good Morning"
    elif(h<16):
        wish="Good Afternoon"
    elif(h<21):
        wish="Good Evening"
    else:
        wish="Good Night"
    my_dict={'time':time,'wish':wish,'name':name,'future':future}
    return render(res,'astroapp/astro.html',my_dict)