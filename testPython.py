import collections
import os
import random

import firebase_admin
import pyrebase
from firebase_admin import credentials
from firebase_admin import db

#
# import firebase_admin
# import pyrebase
# from firebase_admin import credentials
# from firebase_admin import db
#  ! [remote rejected] master -> master (pre-receive hook declined)
# heroku version
# heroku login
# ls
# git init
# git add . (space period)
# git commit -m "first commit"
#
# heroku create
# heroku git:remote -a dry-fortress-56183
# pip install gunicorn
# gunicorn kaita.wsgi
#
#
# pip install gunicorn
# pip install django-heroku
# pip install dj_database_url
# pip install python-decouple
# pip freeze
# pip freeze > requirements.txt
#
# 1YygyjIO
# on.ubabukoh@gmail.com
# tmLrZ#54opLklSGJ
#
# git push heroku master

data = os.path.abspath(os.path.dirname(__file__)) + f"/main/kaita.json"
cred = credentials.Certificate(data)
dbs = firebase_admin.db
firebase_admin.initialize_app(cred, {
    'storageBucket': 'https://katakata-cb1db.appspot.com',
    'databaseURL': 'https://katakata-cb1db-default-rtdb.firebaseio.com/'
})

config = {
    'apiKey': "AIzaSyAt_1JL01Tzn6xjgAHnJmxAiBM69fxmoDU",
    'authDomain': "katakata-cb1db.firebaseapp.com",
    'databaseURL': "https://katakata-cb1db-default-rtdb.firebaseio.com",
    'projectId': "katakata-cb1db",
    'storageBucket': "katakata-cb1db.appspot.com",
    'messagingSenderId': "191079936554",
    'appId': "1:191079936554:web:7f31ad4fc226207400c953",
    'measurementId': "G-3TGTQXFX28"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()


def loadhumour():
    big_dict = {}
    ref = dbs.reference('names')
    snapshot = ref.get()
    for value in snapshot.values():
        name = value['name']
        ref = dbs.reference(f'names/{name}/cartoons/humour')
        snapshot = ref.order_by_child("timestamp").limit_to_first(1).get()
        if snapshot:
            for value in snapshot.values():
                smalldict = {}
                smalldict['name'] = value['name']
                smalldict['image'] = value['image']
                # smalldict['url'] = value['url']
                # smalldict['orientation'] = value['orientation']
                smalldict['description'] = value['description'].replace('\n', '<br />')
                smalldict['timestamp'] = value['timestamp']
                big_dict[name] = smalldict
    return big_dict


def loadjabs():
    big_dict = {}
    ref = dbs.reference('cartoons')
    snapshot = ref.child("jabs").order_by_child("timestamp").limit_to_first(2).get()
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['name'] = value['name']
            smalldict['image'] = value['image']
            smalldict['description'] = ""
            big_dict[value['timestamp']] = smalldict
    return big_dict


def loadquotes():
    big_dict = {}
    ref = dbs.reference('cartoons')
    snapshot = ref.child("quotes").order_by_child("timestamp").limit_to_first(100).get()
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['name'] = value['name']
            smalldict['image'] = value['image']
            smalldict['description'] = ""
            big_dict[value['timestamp']] = smalldict
    return big_dict


def loadsocialproblems():
    big_dict = {}
    ref = dbs.reference('cartoons')
    snapshot = ref.child("socialproblems").order_by_child("timestamp").limit_to_first(1000).get()
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['name'] = value['name']
            smalldict['image'] = value['image']
            smalldict['description'] = value['description'].replace('\n', '<br />')
            big_dict[value['timestamp']] = smalldict
    return big_dict


def loadproverbs():
    big_dict = {}
    ref = dbs.reference('cartoons')
    snapshot = ref.child("proverbs").order_by_child("timestamp").limit_to_last(100).get()
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['name'] = value['name']
            smalldict['image'] = value['image']
            smalldict['description'] = value['description'].replace('\n', '<br />')
            big_dict[value['timestamp']] = smalldict
    return big_dict


def loadlongcomics():
    big_dict = {}
    ref = dbs.reference('names')
    snapshot = ref.get()
    for value in snapshot.values():
        name = value['name']
        ref = dbs.reference(f'names/{name}/cartoons/longcomics')
        snapshot = ref.order_by_child("timestamp").limit_to_first(1).get()
        if snapshot:
            for value in snapshot.values():
                smalldict = {}
                smalldict['name'] = value['name']
                smalldict['image'] = value['image']
                smalldict['url'] = value['url']
                smalldict['description'] = ""
                big_dict[name] = smalldict
    return big_dict


def loadillustrationnames():
    big_dict = {}
    ref = dbs.reference('cartoons')
    snapshot = ref.child("illustrationnames").order_by_child("timestamp").limit_to_first(2).get()
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['name'] = value['name']
            smalldict['image'] = value['image']
            smalldict['description'] = ""
            big_dict[value['timestamp']] = smalldict
    return big_dict


def loadillustrationcontent(illustrationname):
    big_dict = {}
    ref = dbs.reference('cartoons')
    snapshot = ref.child("illustrations").child(illustrationname).order_by_child("timestamp").limit_to_first(100).get()
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['name'] = value['name']
            smalldict['image'] = value['image']
            smalldict['description'] = ""
            big_dict[value['timestamp']] = smalldict
    return big_dict


def loadconthumournames():
    big_dict = {}
    ref = dbs.reference('names')
    snapshot = ref.get()
    for value in snapshot.values():
        name = value['name']
        ref = dbs.reference(f'names/{name}/cartoons/conthumour')
        snapshot = ref.order_by_child("timestamp").limit_to_first(1).get()
        if snapshot:
            for value in snapshot.values():
                smalldict = {}
                smalldict['name'] = value['name']
                print(value['name'])
                smalldict['image'] = value['image']
                # smalldict['url'] = value['url']
                # smalldict['description'] = ""
                big_dict[name] = smalldict
    return big_dict





def loadconthumourcontent(conthumourname):
    big_dict = {}
    ref = dbs.reference('cartoons')
    snapshot = ref.child("conthumour").child(conthumourname).order_by_child("timestamp").limit_to_first(100).get()
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['name'] = value['name']
            smalldict['image'] = value['image']
            smalldict['description'] = ""
            big_dict[value['timestamp']] = smalldict
    return big_dict


def loadvideos():
    big_dict = {}
    ref = dbs.reference('videos')
    snapshot = ref.child("combined").order_by_child("timestamp").limit_to_first(3).get()
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['name'] = value['name']
            smalldict['image'] = value['image']
            smalldict['description'] = value['description']
            smalldict['video'] = value['video']
            smalldict['episode'] = value['episode']
            big_dict[value['timestamp']] = smalldict
    return big_dict


def loadmagazines():
    big_dict = {}
    ref = dbs.reference('magazines')
    snapshot = ref.order_by_child("timestamp").limit_to_first(2).get()
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['name'] = value['name']
            smalldict['image'] = value['image']
            smalldict['url'] = value['url']
            big_dict[value['timestamp']] = smalldict
    return big_dict


def loadnewscategories():
    big_dict = {}

    ref = dbs.reference('news/newscategories')
    snapshotfirst = ref.get()

    if snapshotfirst:
        for value in snapshotfirst.values():
            smalldict = {}
            smalldict['category'] = value['name']
            smalldict['timestamp'] = value['timestamp']
            big_dict[value['timestamp']] = smalldict

    newsref = dbs.reference(f'news/news')
    newssnapshot = newsref.order_by_child("timestamp").limit_to_first(100000).get()

    for value in big_dict.values():
        category = value['category']
        timestamp = value['timestamp']
        big_dict[timestamp]['videos'] = {}

        if newssnapshot:
            for value in newssnapshot.values():
                smallviddict = {}
                if value['category'] == category:
                    smallviddict['category'] = value['category']
                    smallviddict['description']  = value['description'].replace('\n', '<br />')
                    smallviddict['fulldate'] = value['fulldate']
                    smallviddict['image'] = value['image']
                    smallviddict['location'] = value['location']
                    smallviddict['name'] = value['name']
                    smallviddict['year'] = value['year']
                    smallviddict['timestamp'] = value['timestamp']
                    big_dict[timestamp]['videos'][value['timestamp']] = smallviddict


    return big_dict


def loadnewslocations():
    big_dict = {}

    ref = dbs.reference('news/newslocations')
    snapshotfirst = ref.get()

    print("kaita a")

    if snapshotfirst:
        print("kaita b")

        for value in snapshotfirst.values():
            print("kaita c")
            smalldict = {}
            smalldict['category'] = value['name']
            smalldict['timestamp'] = value['timestamp']
            big_dict[value['timestamp']] = smalldict

    print("kaita d")

    newsref = dbs.reference(f'news/news')
    newssnapshot = newsref.order_by_child("timestamp").limit_to_first(100000).get()

    for value in big_dict.values():
        location = value['category']
        timestamp = value['timestamp']
        big_dict[timestamp]['videos'] = {}

        if newssnapshot:
            for value in newssnapshot.values():
                smallviddict = {}
                if value['location'] == location:
                    smallviddict['category'] = value['category']
                    smallviddict['description']  = value['description'].replace('\n', '<br />')
                    smallviddict['fulldate'] = value['fulldate']
                    smallviddict['image'] = value['image']
                    smallviddict['location'] = value['location']
                    smallviddict['name'] = value['name']
                    smallviddict['year'] = value['year']
                    smallviddict['timestamp'] = value['timestamp']
                    big_dict[timestamp]['videos'][value['timestamp']] = smallviddict

    return big_dict


def latestvideo():
    big_dict = {}
    ref = dbs.reference('videos/combined')
    snapshot = ref.order_by_child("timestamp").limit_to_last(1).get()
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['name'] = value['name']
            smalldict['image'] = value['image']
            big_dict[value['timestamp']] = smalldict
    return big_dict


def latestmagazine():
    big_dict = {}
    ref = dbs.reference('magazines')
    snapshot = ref.order_by_child("timestamp").limit_to_first(1).get()
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['name'] = value['name']
            smalldict['image'] = value['image']
            smalldict['url'] = value['url']
            big_dict[value['timestamp']] = smalldict
    return big_dict

def latestcartoon():
    big_dict = {}
    ref = dbs.reference('cartoons')
    snapshot = ref.child("latestcartoon").order_by_child("timestamp").limit_to_last(1).get()
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['name'] = value['name']
            smalldict['image'] = value['image']
            big_dict[value['timestamp']] = smalldict
    return big_dict


def data():
    data = {}
    data['rice'] = ["rice", 5, 100]
    data['milk'] = ["milk", 2, 100]

def fetchsliderimages():
    big_dict = []
    ref = dbs.reference('cartoons/sliderimages')
    snapshot = ref.order_by_child("timestamp").limit_to_last(100).get()
    if snapshot:
        for value in snapshot.values():
            big_dict.append(value['image'])

    image = random.choice(big_dict)
    return image


def humour():
    big_dict = {}
    ref = dbs.reference('names')
    snapshot = ref.get()
    for value in snapshot.values():
        name = value['name']
        ref = dbs.reference(f'names/{name}/cartoons/conthumour')
        snapshot = ref.order_by_child("timestamp").limit_to_first(1).get()
        if snapshot:
            for value in snapshot.values():
                smalldict = {}
                smalldict['name'] = value['name']
                smalldict['image'] = value['image']
                smalldict['timestamp'] = value['timestamp']
                big_dict[name] = smalldict
    return big_dict



def latestnews():
    big_dict = {}
    ref = dbs.reference('news/news')
    snapshot = ref.order_by_child("timestamp").limit_to_first(2).get()
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['category'] = value['category']
            smalldict['description'] = value['description'].replace('\n', '<br />')
            smalldict['fulldate'] = value['fulldate']
            smalldict['image'] = value['image']
            smalldict['location'] = value['location']
            smalldict['name'] = value['name']
            smalldict['year'] = value['year']
            smalldict['timestamp'] = value['timestamp']
            big_dict[value['timestamp']] = smalldict
    return big_dict

def latestnewsone():
    big_dict = {}
    ref = dbs.reference('news/news')
    snapshot = ref.order_by_child("timestamp").limit_to_first(1).get()
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['category'] = value['category']
            smalldict['description'] = value['description'].replace('\n', '<br />')
            smalldict['fulldate'] = value['fulldate']
            smalldict['image'] = value['image']
            smalldict['location'] = value['location']
            smalldict['name'] = value['name']
            smalldict['year'] = value['year']
            smalldict['timestamp'] = value['timestamp']
            big_dict[value['timestamp']] = smalldict
    return big_dict

# humour()
# Collect Static Heroku
# Collect Static Heroku
# Heroku Error that keeps happening heroku config:unset DISABLE_COLLECTSTATIChttps://stackoverflow.com/questions/36665889/collectstatic-error-while-deploying-django-app-to-heroku


def loadmoresinglecomics():
    big_dict = {}
    ref = dbs.reference('cartoons/humour')
    snapshot = ref.order_by_child("timestamp").limit_to_last(50).get()
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['name'] = value['name']
            smalldict['image'] = value['image']
            big_dict[value['timestamp']] = smalldict
    return big_dict



def androidvideos(number):
    big_dict = {}
    ref = dbs.reference('videos/playlistnames')
    snapshot = ref.order_by_child("timestamp").limit_to_last(number).get()
    snapshot = collections.OrderedDict(reversed(list(snapshot.items())))
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['name'] = value['name']
            smalldict['image'] = value['image']
            big_dict[value['timestamp']] = smalldict
            print("")
    return big_dict


def androidloadspecificshortcomic(shortcomicname):
    big_dict = {}
    ref = dbs.reference(f'cartoons/conthumour/{shortcomicname}')
    snapshot = ref.order_by_child("timestamp").limit_to_last(1000).get()
    # snapshot = collections.OrderedDict(reversed(list(snapshot.items())))
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['name'] = value['name']
            smalldict['image'] = value['image']
            big_dict[value['timestamp']] = smalldict
    print(big_dict)
    return big_dict



def androidloadmagazines(number):
    print("Clicked Clicked")
    big_dict = {}
    ref = dbs.reference('magazines')
    snapshot = ref.order_by_child("timestamp").limit_to_first(number).get()
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['name'] = value['name']
            smalldict['image'] = value['image']
            smalldict['url'] = value['url']
            big_dict[value['timestamp']] = smalldict
    return big_dict


def loadconthumournamesnumber():
    big_dict = {}
    ref = dbs.reference('cartoons/conthumournames')
    snapshot = ref.get()
    return len(snapshot)

def loadmoresinglecomicsnumber():
    big_dict = {}
    ref = dbs.reference('cartoons/humour')
    snapshot = ref.get()
    return len(snapshot)

def loadlongcomicsnumber():
    big_dict = {}
    ref = dbs.reference('cartoons/longcomics')
    snapshot = ref.get()
    return len(snapshot)


def longcomicsall(number):
    big_dict = {}
    ref = dbs.reference('cartoons/longcomics')
    snapshot = ref.order_by_child("timestamp").limit_to_last(number).get()
    if snapshot:
        for value in snapshot.values():
            smalldict = {}
            smalldict['name'] = value['name']
            smalldict['image'] = value['image']
            smalldict['url'] = value['url']
            big_dict[value['timestamp']] = smalldict
    return big_dict


def loadconthumournames_all():
    big_dict = {}
    ref = dbs.reference('cartoons/conthumournames')
    snapshot = ref.get()
    for value in snapshot.values():
        smalldict = {}
        smalldict['name'] = value['name']
        smalldict['image'] = value['image']
        smalldict['timestamp'] = value['timestamp']
        big_dict[value['timestamp']] = smalldict
    return big_dict


# import smtplib
# from email.message import EmailMessage #new
#
# code = 1234234
# message = EmailMessage()
# message['Subject'] = f'KATAKATA NEWSLETTERS'
# message['From'] = "ngugi@katakata.org"
# message['To'] = "kaitajohnn@gmail.com"
# message.set_content('This email is sent using python.')
# unformated_message = """\
# <!DOCTYPE html>
#     <html>
#     <body>
#
#     <h1 style="color:black;text-align:center;font-family:verdana">Thank you for Joining Katakata</h1>
#     <p style="color:black;text-align:center;font-family:courier;font-size:120%">Your confirmation code is : <br> <h2 align="center">{0}</h2></p>
#
#     </body>
#     </html>
# """
# unformated_message = unformated_message.format(code)
# message.add_alternative(unformated_message, subtype = 'html')
#
# server = smtplib.SMTP('mail.privateemail.com', 587)
# server.starttls()
# server.login('ngugi@katakata.org', 'Password')
# server.send_message(message)
#

def ngugipassword():
    snapshot = dbs.reference('credentials/ngugi').get()
    return str(snapshot).strip()

def adminpassword():
    snapshot = dbs.reference('credentials/admin').get()
    return str(snapshot).strip()

def katakatasenderpassword():
    snapshot = dbs.reference('credentials/katakatasender').get()
    return str(snapshot).strip()


def signUp():
    email = "first@gmail.com"
    password = "asdfghjkl"
    try:
        auth.create_user_with_email_and_password(email, password)
    except:
        print("Email already exists")


def login():
    email = "first@gmail.com"
    password = "asdfghjkl"
    login = auth.sign_in_with_email_and_password(email, password)
    print(login['localId'])


def getUserName(userId):
    big_dict = {}
    big_dict['name'] = dbs.reference(f'users/{userId}/name').get()
    big_dict['email'] = dbs.reference(f'users/{userId}/email').get()
    big_dict['image'] = dbs.reference(f'users/{userId}/image').get()
    return big_dict



def androidloadspecificvideo(playlistname):
    big_dict = {}
    ref = dbs.reference(f'videos/playlists/{playlistname}')
    snapshot = ref.order_by_child("timestamp").limit_to_last(1000).get()
    # snapshot = collections.OrderedDict(reversed(list(snapshot.items())))
    if snapshot:
        count = 0
        for value in snapshot.values():
            smalldict = {}
            smalldict['name'] = value['name']
            smalldict['position'] = count
            smalldict['description'] = value['description']
            smalldict['image'] = value['image']
            smalldict['video'] = value['video'].split("com/", 1)[1]
            smalldict['headername'] = value['headername']
            if 'comments' in value.keys():
                smalldict['comments'] = value['comments']
                smalldict['size'] = len(value['comments'])
                print(value['comments'])
            big_dict[value['timestamp']] = smalldict
            count = count + 1
    print(big_dict)
    return big_dict