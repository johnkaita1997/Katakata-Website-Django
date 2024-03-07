
import json
import smtplib
from email.message import EmailMessage

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt

from testPython import *

monthsummaryDict = {}

# @cache_control(must_revalidate=True)

mtnUsername = getCredentials()['mtnusername']
mtnpassword = getCredentials()['mtnpassword']
mtnproductid = getCredentials()['mtnproductid']
mtnnetwork = getCredentials()['mtnnetwork']

def num_Videos():
    snapshot = dbs.reference('numbers/videos').get()
    return snapshot


def num_Magazines():
    snapshot = dbs.reference('numbers/magazines').get()
    return snapshot

def num_LongComics():
    snapshot = dbs.reference('numbers/longcomics').get()
    return snapshot


def num_LongShortcomics():
    snapshot = dbs.reference('numbers/shortcomics').get()
    return snapshot


def num_LongSinglecomics():
    snapshot = dbs.reference('numbers/singlecomics').get()
    return snapshot


def callMainData():
    if not 'androidvideos' in monthsummaryDict.keys():
        monthsummaryDict['androidvideos'] = androidvideos(num_Videos())
    if not 'loadhumour' in monthsummaryDict.keys():
        monthsummaryDict['loadhumour'] = loadhumour()
    if not 'loadmoresinglecomics' in monthsummaryDict.keys():
        monthsummaryDict['loadmoresinglecomics'] = loadmoresinglecomics()
    if not 'loadlongcomics' in monthsummaryDict.keys():
        monthsummaryDict['loadlongcomics'] = longcomicsall(num_LongComics())
    if not 'allmagazines' in monthsummaryDict.keys():
        monthsummaryDict['allmagazines'] = androidloadmagazines(3)
    if not 'latestnews' in monthsummaryDict.keys():
        monthsummaryDict['latestnews'] = latestnews()
    if not 'conthumournames' in monthsummaryDict.keys():
        monthsummaryDict['conthumournames'] = loadconthumournames_all()
    if not 'longcomicsnumber' in monthsummaryDict.keys():
        monthsummaryDict['longcomicsnumber'] = num_LongComics()
    if not 'shortcomicsnumber' in monthsummaryDict.keys():
        monthsummaryDict['shortcomicsnumber'] = loadconthumournamesnumber()
    if not 'singlecomicsnumber' in monthsummaryDict.keys():
        monthsummaryDict['singlecomicsnumber'] = loadmoresinglecomicsnumber()
    monthsummaryDict['sliderimages'] = getSliderImages()


@never_cache
def homepage(request):

    callMainData()
    if not "login" in request.COOKIES.keys():
        monthsummaryDict['isloggedIn'] = False
    else:
        monthsummaryDict['isloggedIn'] = True

    if "login" in request.COOKIES.keys():
        userid = request.COOKIES.get('login')
        useremail = fetchUserData(userid)['email']
        if 'kat' in useremail:
            monthsummaryDict['showadmin'] = True

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        pornlanguage = any(word in name for word in fetchPornWords())
        emailpornlanguage = any(word in email for word in fetchPornWords())
        if not name or not email or not name:
            messages.error(request, _(f"Ensure all fields are entered"))
            return redirect('homepage')
        elif pornlanguage:
            messages.error(request, _(f"Your inputs were filtered"))
            return redirect('homepage')
        elif emailpornlanguage:
            messages.error(request, _(f"Your inputs were filtered"))
            return redirect('homepage')

        emaillist = []
        snapshot = dbs.reference('newsletter').get()
        for value in snapshot.values():
            themail = value['email']
            emaillist.append(themail)
        if email in emaillist:
            response = render(request, 'index.html',
                              {"message": "You are already subscribed.", "summary": monthsummaryDict})
            return response
        else:
            monthsummaryDict['sirname'] = name
            monthsummaryDict['siremail'] = email

            import random
            code = '{:05}'.format(random.randrange(100, 10 ** 3))

            message = EmailMessage()
            message['Subject'] = f'KATAKATA NEWSLETTERS'
            message['From'] = "katakata@katakata.org"
            message['To'] = email
            message.set_content('This email is sent using python.')
            unformated_message = """\
            <!DOCTYPE html>
                <html>
                <body>

                <h1 style="color:black;text-align:center;font-family:verdana">Thank you for Joining Katakata</h1>
                <p style="color:black;text-align:center;font-family:courier;font-size:120%">Your confirmation code is : <br> <h2 align="center">{0}</h2></p>

                </body>
                </html>
            """
            unformated_message = unformated_message.format(code)
            message.add_alternative(unformated_message, subtype='html')

            unformated_message = unformated_message.format(code)
            message.add_alternative(unformated_message, subtype='html')

            server = smtplib.SMTP('mail.privateemail.com', 587)
            server.starttls()
            server.login('katakata@katakata.org', katakatasenderpassword())
            server.send_message(message)

            dbs.reference(f'codes/{code}/name').set(code)

            response = render(request, 'newsletter.html', {'summary': monthsummaryDict})
            return response

    response = render(request, "index.html", {"summary": monthsummaryDict})
    return response


@never_cache
def cartoonspage(request):
    if not 'latestcartoon' in monthsummaryDict.keys():
        monthsummaryDict['loadlongcomics'] = longcomicsall(num_LongComics())
        monthsummaryDict['latestcartoon'] = latestcartoon()
    response = render(request, "longcomicspage.html", {"summary": monthsummaryDict})
    return response


@never_cache
def imageviewer(request, theimage):
    response = render(request, "imageviewer.html", {"theimage": theimage})
    return response


@never_cache
def jabspage(request):
    if not 'loadjabs' in monthsummaryDict.keys():
        monthsummaryDict['loadjabs'] = loadjabs()
    response = render(request, "jabspage.html", {"summary": monthsummaryDict})
    return response


@never_cache
def quotespage(request):
    if not 'loadquotes' in monthsummaryDict.keys():
        monthsummaryDict['loadquotes'] = loadquotes()
    response = render(request, "quotespage.html", {"summary": monthsummaryDict})
    return response


@never_cache
def socialproblemspage(request):
    if not 'loadsocialproblems' in monthsummaryDict.keys():
        monthsummaryDict['loadsocialproblems'] = loadsocialproblems()
    response = render(request, "socialproblemspage.html", {"summary": monthsummaryDict})
    return response


@never_cache
def proverbspage(request):
    if not 'loadproverbs' in monthsummaryDict.keys():
        monthsummaryDict['loadproverbs'] = loadproverbs()
    response = render(request, "proverbspage.html", {"summary": monthsummaryDict})
    return response


@never_cache
def longcomicspage(request):
    monthsummaryDict['longcomics'] = loadlongcomics()
    monthsummaryDict['loadlongcomics'] = longcomicsall(num_LongComics())
    response = render(request, "longcomicspage.html", {"summary": monthsummaryDict})
    return response


@never_cache
def illustrationnamespage(request):
    if not 'illustrationnames' in monthsummaryDict.keys():
        monthsummaryDict['illustrationnames'] = loadillustrationnames()
    response = render(request, "illustrationnamespage.html", {"summary": monthsummaryDict})
    return response


@never_cache
def illustrationcontentpage(request, illustrationname):
    if not 'illustrationcontent' in monthsummaryDict.keys():
        monthsummaryDict['illustrationcontent'] = loadillustrationcontent(illustrationname)
    response = render(request, "illustrationcontentpage.html", {"summary": monthsummaryDict})
    return response


@never_cache
def conthumournamespage(request):
    monthsummaryDict['conthumournames'] = loadconthumournames()
    response = render(request, "conthumournamespage.html", {"summary": monthsummaryDict})
    return response


@never_cache
def conthumourcontentpage(request, conthumourname):
    monthsummaryDict['conthumourcontent'] = loadconthumourcontent(conthumourname)
    response = render(request, "conthumourcontentpage.html", {"summary": monthsummaryDict})
    return response


@never_cache
def pdfviewerpage(request, thepdf):
    if not 'thepdf' in monthsummaryDict.keys():
        monthsummaryDict['thepdf'] = thepdf
    response = render(request, "pdfviewer.html", {"summary": monthsummaryDict})
    return response


@never_cache
def newspage(request):
    monthsummaryDict['latestnews'] = latestnews()
    monthsummaryDict['loadnewslocations'] = loadnewslocations()
    monthsummaryDict['loadnewscategories'] = loadnewscategories()

    response = render(request, "newspage.html", {"summary": monthsummaryDict})
    return response


@never_cache
def newsviewer(request, newsid):
    identity = int(newsid) * -1

    newsdict = {}
    newsdict['category'] = dbs.reference(f'news/news/{identity}/category').get()
    newsdict['description'] = dbs.reference(f'news/news/{identity}/description')
    newsdict['date'] = dbs.reference(f'news/news/{identity}/fulldate').get()
    newsdict['image'] = dbs.reference(f'news/news/{identity}/image').get()
    newsdict['location'] = dbs.reference(f'news/news/{identity}/location').get()
    newsdict['name'] = dbs.reference(f'news/news/{identity}/name').get()
    newsdict['timestamp'] = dbs.reference(f'news/news/{identity}/timestamp').get()
    newsdict['name'] = dbs.reference(f'news/news/{identity}/name').get()

    response = render(request, "newsviewer.html", {"summary": newsdict})
    # comment
    return response


@never_cache
def teampage(request):

    columnists = getColumnists()
    positions = getPositions()
    objectives = getObjectives()
    mission = getMission()

    monthsummaryDict['columnists'] = columnists
    monthsummaryDict['positions'] = positions
    monthsummaryDict['objectives'] = objectives
    monthsummaryDict['mission'] = mission

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        usermessage = request.POST.get('message')

        pornlanguage = any(word in usermessage for word in fetchPornWords())

        if not name or not email or not usermessage:
            response = render(request, 'team.html', {"message": "Ensure all fields are filled"})
            return response
        elif pornlanguage:
            response = render(request, 'team.html', {"message": ""})
            return response
        else:
            # formattedmessage = "From "
            # message = """From: From Person <from@fromdomain.com>
            # To: To Person <to@todomain.com>
            # MIME-Version: 1.0
            # Content-type: text/html
            # Subject: SMTP HTML e-mail test
            #
            # This is an e-mail message to be sent in HTML format
            #
            # <b>This is HTML message.</b>
            # <h1>This is headline.</h1>
            # """

            subject = f'{name} - {email}'
            sender_email = 'katakata@katakata.org'
            sender_password = katakatasenderpassword()
            receiver_email = ["katakatacartoons@gmail.com"]

            try:
                message = 'Subject: {}\n\n{}'.format(subject, usermessage)

                server = smtplib.SMTP('mail.privateemail.com', 587)
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, receiver_email, message)
                print('Email has been sent')
                monthsummaryDict['usermessage'] = usermessage
                response = render(request, 'thankyou.html', {'summary': monthsummaryDict})
                return response

            except Exception as ex:
                response = render(request, 'index.html', {"message": str(ex), 'summary': monthsummaryDict})
                return response

    response = render(request, "team.html", {"summary": monthsummaryDict})
    return response


@never_cache
def shoppage(request):
    response = render(request, "shoppage.html", {"summary": monthsummaryDict})
    return response


@never_cache
def productdetails(request):
    response = render(request, "productdetails.html", {"summary": monthsummaryDict})
    return response


@never_cache
def cartpage(request):
    response = render(request, "cartpage.html", {"summary": monthsummaryDict})
    return response


@never_cache
def humourpage(request):
    if not 'loadhumour' in monthsummaryDict.keys():
        monthsummaryDict['loadhumour'] = loadhumour()

    if not 'loadmoresinglecomics' in monthsummaryDict.keys():
        monthsummaryDict['loadmoresinglecomics'] = loadmoresinglecomics()
    response = render(request, "humourpage.html", {"summary": monthsummaryDict})
    return response


@never_cache
def videos(request, video):
    response = render(request, "videos.html", {"summary": monthsummaryDict})
    return response


@never_cache
def shortcomicsviewer(request, shortcomic):
    if not 'shortcomics' in monthsummaryDict.keys():
        monthsummaryDict['shortcomics'] = androidloadspecificshortcomic(shortcomic)

    if not 'name' in monthsummaryDict.keys():
        monthsummaryDict['name'] = shortcomic
    response = render(request, "shortcomicsviewer.html", {"summary": monthsummaryDict})
    return response


@never_cache
def missionpage(request):
    mission = getMission()
    objectives = getObjectives()
    monthsummaryDict['mission'] = mission
    monthsummaryDict['objectives'] = objectives
    monthsummaryDict['sliderimages'] = getMissionSlerImages()
    response = render(request, "mission.html", {"summary": monthsummaryDict})
    return response


@never_cache
def satvideos(request):
    monthsummaryDict['satvideos'] = androidvideos(100000000)
    response = render(request, "satvideos.html", {"summary": monthsummaryDict})
    return response


@never_cache
def satmagazines(request):
    monthsummaryDict['allsatmagazines'] = androidloadmagazines(10000000)
    response = render(request, "satmagazines.html", {"summary": monthsummaryDict})
    return response


@never_cache
def satlongcomics(request):
    monthsummaryDict['longcomics'] = longcomicsall(100000)
    response = render(request, "satlongcomics.html", {"summary": monthsummaryDict})
    return response


@never_cache
def newsletter(request, namer, emailer):
    if not 'namer' in monthsummaryDict.keys():
        monthsummaryDict['namer'] = namer
    if not 'emailer' in monthsummaryDict.keys():
        monthsummaryDict['emailer'] = emailer

    if request.method == 'POST':
        code = request.POST.get('code')
        snapshot = dbs.reference(f'codes/{code}').get()
        if snapshot:

            print("Snapshot is available")

            dbs.reference(f'codes/{code}').delete()

            name = monthsummaryDict['namer']
            email = monthsummaryDict['emailer']
            data = {
                "name": name,
                "email": email,
                "removelink": f'katakata.org/unsubscribe/{email}'
            }
            dbs.reference(f'newsletter').push().set(data)

            response = render(request, "subscribed.html", {"summary": monthsummaryDict})
            return response
        else:
            response = render(request, "newsletter.html", {"message": 'Code is invalid or has expired'})
            return response

    response = render(request, "newsletter.html", {"summary": monthsummaryDict})
    return response


@never_cache
def unsubscribe(request, email):
    snapshot = dbs.reference(f'newsletter').get()
    for value in snapshot.keys():
        theemail = dbs.reference(f'newsletter/{value}/email').get()
        if theemail == email:

            try:
                dbs.reference(f'newsletter/{value}').delete()
                response = render(request, "unsubscribed.html")
                return response
            except:
                response = render(request, 'index.html',
                                  {"message": "Unsubscription failed. An error occured.", "summary": monthsummaryDict})
                return response

    response = render(request, "index.html", {"summary": monthsummaryDict})
    return response


@never_cache
def contactus(request):
    response = render(request, "contactus.html", {"summary": monthsummaryDict})
    return response


@never_cache
def createnews(request):
    def getnlocations():
        bundle = []
        ref = dbs.reference('news/newslocations')
        snapshot = ref.order_by_child("timestamp").limit_to_last(10000000).get()
        if snapshot:
            for value in snapshot.values():
                name = value['name']
                bundle.append((name))
        else:
            return [""]

        print(bundle)
        return bundle

    def getncategories():
        bundle = []
        ref = dbs.reference('news/newscategories')
        snapshot = ref.order_by_child("timestamp").limit_to_last(10000000).get()
        if snapshot:
            for value in snapshot.values():
                name = value['name']
                bundle.append((name))
        else:
            return [""]
        return bundle

    if request.method == "POST":
        try:
            newsname = request.POST.get("newstitle")
            newsdescription = request.POST.get("summernote")
            newslocation = request.POST.get("newslocation")
            newscategory = request.POST.get("newscategory")
            newsdate = request.POST.get("dateonfews")
            imageUrl = request.POST.get("url")

            if not imageUrl:
                response = render(request, "createnewspage.html", {"message": "You did not upload or save your Image"})
                return response

            timestamp = int(time.time())

            locationdict = {}
            locationdict["timestamp"] = timestamp
            locationdict["name"] = newslocation

            categorydict = {}
            categorydict["timestamp"] = timestamp
            categorydict["name"] = newscategory
            categorydict["image"] = imageUrl

            if newslocation not in getncategories():
                dbs.reference(f'news/newslocations/{newslocation}').set(locationdict)
            if newscategory not in getncategories():
                dbs.reference(f'news/newscategories/{newscategory}').set(categorydict)

            year = datetime.today().strftime('%Y')
            month = datetime.today().strftime('%b')
            day = datetime.today().strftime('%d')
            monthyear = f'{month}-{year}'

            print("There")

            bundle = {}
            bundle["image"] = imageUrl
            bundle["name"] = newsname
            bundle["description"] = newsdescription
            bundle["location_category"] = f'{newslocation}_{newscategory}'
            bundle["timestamp"] = -timestamp
            bundle["location"] = newslocation
            bundle["category"] = newscategory
            bundle["fulldate"] = newsdate
            bundle["year"] = year
            bundle["month"] = month
            bundle["day"] = day
            bundle["monthyear"] = monthyear

            dbs.reference(f'news/news/{timestamp}').set(bundle)
        except:
            response = render(request, "createnewspage.html", {"message": "An error occured! News was not uploaded"})
            return response
        else:
            response = render(request, "index.html", {"message": "News uploaded sucessfuly"})
            return response

    if not 'newslocations' in monthsummaryDict.keys():
        monthsummaryDict['newslocations'] = getnlocations()
    if not 'newscategories' in monthsummaryDict.keys():
        monthsummaryDict['newscategories'] = getncategories()
    response = render(request, "createnewspage.html", {"summary": monthsummaryDict})
    return response


@never_cache
def editnews(request, newsid):
    def getnlocations():
        bundle = []
        ref = dbs.reference('news/newslocations')
        snapshot = ref.order_by_child("timestamp").limit_to_last(10000000).get()
        if snapshot:
            for value in snapshot.values():
                name = value['name']
                bundle.append((name))
        else:
            return [""]

        print(bundle)
        return bundle

    def getncategories():
        bundle = []
        ref = dbs.reference('news/newscategories')
        snapshot = ref.order_by_child("timestamp").limit_to_last(10000000).get()
        if snapshot:
            for value in snapshot.values():
                name = value['name']
                bundle.append((name))
        else:
            return [""]
        return bundle

    thedict = {}

    category = dbs.reference(f'news/news/{newsid}').child("category").get()
    description = dbs.reference(f'news/news/{newsid}').child("description").get()
    fulldate = dbs.reference(f'news/news/{newsid}').child("fulldate").get()
    image = dbs.reference(f'news/news/{newsid}').child("image").get()
    location = dbs.reference(f'news/news/{newsid}').child("location").get()
    name = dbs.reference(f'news/news/{newsid}').child("name").get()
    timestamp = newsid

    thedict["category"] = category
    thedict["description"] = description
    thedict["fulldate"] = fulldate
    thedict["image"] = image
    thedict["location"] = location
    thedict["name"] = name
    thedict["timestamp"] = timestamp
    thedict["newslocations"] = getnlocations()
    thedict["newscategories"] = getncategories()

    if request.method == "POST":
        try:

            imageUrl = request.POST.get("url")

            if imageUrl:
                print("Image is there")
                image = imageUrl
            else:
                print("image is not there")

            newsname = request.POST.get("newstitle")
            newsdescription = request.POST.get("summernote")
            newslocation = request.POST.get("newslocation")
            newscategory = request.POST.get("newscategory")
            newsdate = request.POST.get("dateonfews")
            imageUrl = image

            locationdict = {}
            locationdict["timestamp"] = timestamp
            locationdict["name"] = newslocation

            categorydict = {}
            categorydict["timestamp"] = timestamp
            categorydict["name"] = newscategory
            categorydict["image"] = imageUrl

            if newslocation not in getnlocations():
                dbs.reference(f'news/newslocations/{newslocation}').set(locationdict)
            if newscategory not in getncategories():
                dbs.reference(f'news/newscategories/{newscategory}').set(categorydict)

            year = datetime.today().strftime('%Y')
            month = datetime.today().strftime('%b')
            day = datetime.today().strftime('%d')
            monthyear = f'{month}-{year}'

            print("There")

            bundle = {}
            bundle["image"] = imageUrl
            bundle["name"] = newsname
            bundle["description"] = newsdescription
            bundle["location_category"] = f'{newslocation}_{newscategory}'
            bundle["timestamp"] = -int(timestamp)
            bundle["location"] = newslocation
            bundle["category"] = newscategory
            bundle["fulldate"] = newsdate
            bundle["year"] = year
            bundle["month"] = month
            bundle["day"] = day
            bundle["monthyear"] = monthyear

            dbs.reference(f'news/news/{timestamp}').set(bundle)

        except:
            response = render(request, "editnewspage.html", {"message": "An error occured! News was not uploaded"})
            return response
        else:
            response = render(request, "index.html", {"message": "News edited sucessfuly"})
            return response

    response = render(request, "editnewspage.html", {"summary": thedict})
    return response


@never_cache
def news(request, newsid):
    identity = int(newsid) * -1

    newsdict = {}
    newsdict['category'] = dbs.reference(f'news/news/{identity}/category').get()
    newsdict['description'] = dbs.reference(f'news/news/{identity}/description').get()
    newsdict['date'] = dbs.reference(f'news/news/{identity}/fulldate').get()
    newsdict['image'] = dbs.reference(f'news/news/{identity}/image').get()
    newsdict['location'] = dbs.reference(f'news/news/{identity}/location').get()
    newsdict['name'] = dbs.reference(f'news/news/{identity}/name').get()
    newsdict['timestamp'] = dbs.reference(f'news/news/{identity}/timestamp').get()
    newsdict['name'] = dbs.reference(f'news/news/{identity}/name').get()

    response = render(request, "news.html", {"summary": newsdict})
    # comment
    return response


@never_cache
def userlogin(request):
    if request.method == "POST":
        try:
            email = request.POST.get("email").strip()
            password = request.POST.get("password").strip()

            try:
                login = auth.sign_in_with_email_and_password(email, password)
                userid = login['localId']
                if not "login" in request.COOKIES.keys():
                    response = redirect('homepage')
                    response.set_cookie('login', userid, max_age=31536000)
                    messages.error(request, _("Login was successful"))
                    return response
                else:
                    messages.error(request, _("You are already logged in!"))
                    return redirect('homepage')

            except Exception as exception:
                messages.error(request, _(f"An error occured!\n{exception}"))
                return redirect('userlogin')

        except Exception as exception:
            messages.error(request, _(f"An error occured!\n{exception}"))
            return redirect('userlogin')

    response = render(request, "login.html", {"summary": monthsummaryDict})
    return response


@never_cache
def userReg(request):
    if request.method == "POST":
        try:
            email = request.POST.get("email").strip()
            name = request.POST.get("name").strip()
            password = request.POST.get("password").strip()
            mobile = "00000"

            imageUrl = request.POST.get("url")

            if not imageUrl:
                print("Image is not there")
            else:
                try:
                    auth.create_user_with_email_and_password(email, password)
                    login = auth.sign_in_with_email_and_password(email, password)
                    userid = login['localId']

                    userDict = {}
                    userDict['image'] = imageUrl
                    userDict['name'] = name
                    userDict['uid'] = userid
                    userDict['email'] = email
                    userDict['mobile'] = mobile
                    dbs.reference(f'users/{userid}').set(userDict)
                except Exception as exception:
                    messages.error(request, _(f"An error occured!\n{exception}"))
                else:
                    if not "login" in request.COOKIES.keys():
                        response = redirect('homepage')
                        response.set_cookie('login', userid, max_age=31536000)
                        messages.error(request, _(f"Account Created Successfully"))
                        return redirect('homepage')
                    else:
                        messages.error(request, _(f"You are already logged in"))
                        return redirect('homepage')

        except Exception as exception:
            messages.error(request, _(f"An error occured!\n{exception}"))
            response = redirect('userReg')

            return response

    return render(request, "register.html", {"summary": monthsummaryDict})


@never_cache
def videoviewer(request, video, position):
    # try:
    #     response = redirect('subscriptionpage')
    #     response.set_cookie('video', video, max_age=31536000)
    #
    #     print("Try")
    #     mobile = request.COOKIES.get('mobile')
    #     if not mobile:
    #         print("Try harder")
    #         return response
    #
    #     subscribed = isFirebaseAvailable(mobile)
    #     if not subscribed:
    #         messages.error(request, _("Subscription is required to view videos."))
    #         return response
    #     else:
    #         transactionId = fetchFromFirebase(mobile)
    #
    #         if not isUserSubscribed(transactionId):
    #             print("You are not subscribed")
    #             return response
    #         else:
    #             print("You are subscribed")
    #             print("You are subscribed")
    #             theposition = int(position)
    #             defaultTimestamp = list(androidloadspecificvideo(video).keys())[int(theposition)]
    #             defaultVideo = androidloadspecificvideo(video)[f'{defaultTimestamp}']
    #             monthsummaryDict['videos'] = androidloadspecificvideo(video)
    #             monthsummaryDict['name'] = video
    #             monthsummaryDict['default'] = monthsummaryDict['name'][theposition]
    #             monthsummaryDict['default'] = defaultVideo
    #             monthsummaryDict['loggedin'] = subscribed
    #             defaultVideoName = defaultVideo['name']
    #             defaultVideoTimeStamp = int(defaultTimestamp) * -1
    #
    #             viewsDictionary = {}
    #             viewsDictionary['view'] = "One"
    #             dbs.reference(f'videos/playlists/{defaultVideoName}/{defaultVideoTimeStamp}/views').push().set(viewsDictionary)
    #             numberofViews = len(dbs.reference(f'videos/playlists/{defaultVideoName}/{defaultVideoTimeStamp}/views').get())
    #             print(f'{numberofViews} is number of views')
    #             monthsummaryDict['numberofviews'] = numberofViews
    #
    #             if request.method == "POST":
    #                 try:
    #                     comment = request.POST.get("comment")
    #                     if not comment:
    #                         messages.error(request, _("You have entered no message."))
    #                         return redirect('videoviewer', video=defaultVideo['name'], position=theposition)
    #                     else:
    #                         if not "login" in request.COOKIES.keys():
    #                             messages.error(request, _("Login is required to post comments."))
    #                             return redirect('userlogin')
    #                         else:
    #                             theposition = int(position)
    #                             defaultTimestamp = list( androidloadspecificvideo(video).keys() )[int(theposition)]
    #                             defaultVideo = androidloadspecificvideo(video)[f'{defaultTimestamp}']
    #                             defaultVideoName = defaultVideo['name']
    #                             defaultVideoTimeStamp = int(defaultTimestamp) * -1
    #
    #                             print(defaultVideoTimeStamp)
    #
    #                             timestamp = int(time.time())
    #                             commentObject = {}
    #                             userid = request.COOKIES.get('login')
    #
    #                             name = getUserName(userid)['login']
    #                             email = getUserName(userid)['email']
    #                             image = getUserName(userid)['image']
    #                             print(f"user is ${userid}\n{name}\n{email}\n{image}")
    #
    #                             commentObject["timestamp"] = timestamp
    #                             commentObject['comment'] = comment
    #                             commentObject['name'] = name
    #                             commentObject['email'] = email
    #                             commentObject['image'] = image
    #
    #                             dbs.reference(f'videos/playlists/{defaultVideoName}/{defaultVideoTimeStamp}/comments/{timestamp}').set(
    #                                 commentObject)
    #                             return redirect('videoviewer', video=defaultVideo['name'], position=theposition)
    #
    #                 except Exception as exception:
    #                     messages.error(request, _(f'Error ${exception}'))
    #                     return redirect('videoviewer', video=defaultVideo['name'], position=theposition)
    # except Exception as exception:
    #     print(f'Exception is {exception}')
    #     return redirect('videoviewer', video=video, position=0)

    print("You are subscribed")
    print("You are subscribed")
    theposition = int(position)
    defaultTimestamp = list(androidloadspecificvideo(video).keys())[int(theposition)]
    defaultVideo = androidloadspecificvideo(video)[f'{defaultTimestamp}']
    monthsummaryDict['videos'] = androidloadspecificvideo(video)
    monthsummaryDict['name'] = video
    monthsummaryDict['default'] = monthsummaryDict['name'][theposition]
    monthsummaryDict['default'] = defaultVideo
    # monthsummaryDict['loggedin'] = subscribed
    defaultVideoName = defaultVideo['name']
    defaultVideoTimeStamp = int(defaultTimestamp) * -1

    viewsDictionary = {}
    viewsDictionary['view'] = "One"
    dbs.reference(f'videos/playlists/{defaultVideoName}/{defaultVideoTimeStamp}/views').push().set(viewsDictionary)
    numberofViews = len(dbs.reference(f'videos/playlists/{defaultVideoName}/{defaultVideoTimeStamp}/views').get())
    print(f'{numberofViews} is number of views')
    monthsummaryDict['numberofviews'] = numberofViews

    if request.method == "POST":
        try:
            comment = request.POST.get("comment")
            if not comment:
                messages.error(request, _("You have entered no message."))
                return redirect('videoviewer', video=defaultVideo['name'], position=theposition)
            else:
                if not "login" in request.COOKIES.keys():
                    messages.error(request, _("Login is required to post comments."))
                    return redirect('userlogin')
                else:
                    theposition = int(position)
                    defaultTimestamp = list(androidloadspecificvideo(video).keys())[int(theposition)]
                    defaultVideo = androidloadspecificvideo(video)[f'{defaultTimestamp}']
                    defaultVideoName = defaultVideo['name']
                    defaultVideoTimeStamp = int(defaultTimestamp) * -1

                    print(defaultVideoTimeStamp)

                    timestamp = int(time.time())
                    commentObject = {}
                    userid = request.COOKIES.get('login')

                    name = getUserName(userid)['login']
                    email = getUserName(userid)['email']
                    image = getUserName(userid)['image']
                    print(f"user is ${userid}\n{name}\n{email}\n{image}")

                    commentObject["timestamp"] = timestamp
                    commentObject['comment'] = comment
                    commentObject['name'] = name
                    commentObject['email'] = email
                    commentObject['image'] = image

                    dbs.reference(
                        f'videos/playlists/{defaultVideoName}/{defaultVideoTimeStamp}/comments/{timestamp}').set(
                        commentObject)
                    return redirect('videoviewer', video=defaultVideo['name'], position=theposition)

        except Exception as exception:
            messages.error(request, _(f'Error ${exception}'))
            return redirect('videoviewer', video=defaultVideo['name'], position=theposition)


    return render(request, "videoviewer.html", {"summary": monthsummaryDict})



def logout(request):
    response = redirect('userlogin')
    messages.error(request, _(f"You have been logged out"))
    response.delete_cookie('login')
    return response


class Subscription(View):
    def get(self, request):
        msisdn = request.GET.get("msisdn", None)
        network = request.GET.get("network")
        username = request.GET.get("username")
        password = request.GET.get("password")
        print(msisdn, network, username, password)
        response = render(request, "subscribe.html", {"summary": monthsummaryDict})
        return response


@csrf_exempt
def callback(request):
    print("Am hit")
    mydict = {}
    data = json.loads(request.body.decode('utf-8'))
    if not data:
        mydict['success'] = False
        print("Data is not available")
    else:
        mydict['success'] = True
        subscriptionType = data["type"]
        network = data["mno"]
        mobile = data["msisdn"]
        shortcode = data["shortcode"]
        productid = data["productid"]
        transactionid = data["transactionid"]
        amount = data["amount"]
        renewaltype = data["renewaltype"]
        subscribetext = data["subscribetext"]
        time = data["requesttime"]
        status = data["status"]

        import time as thetime
        timestamp = int(thetime.time())
        thestamp = datetime.fromtimestamp(timestamp)
        formatted = thestamp.strftime("%d-%b-%Y")
        date = formatted
        month = getDates()['month']
        year = getDates()['year']
        combined = getDates()['combined']

        paymentDict = {}
        paymentDict['date'] = date
        paymentDict['month'] = month
        paymentDict['year'] = year
        paymentDict['combined'] = combined
        paymentDict['network'] = network
        paymentDict['mobile'] = mobile
        paymentDict['shortcode'] = shortcode
        paymentDict['productid'] = productid
        paymentDict['transactionid'] = transactionid
        paymentDict['amount'] = amount
        paymentDict['renewaltype'] = renewaltype
        paymentDict['subscribetext'] = subscribetext
        paymentDict['time'] = time
        paymentDict['status'] = status
        paymentDict['timestamp'] = timestamp

        if subscriptionType == "SUB":
            pushToFirebase(transactionid, mobile)
            if status == "SUCCESS":
                dbs.reference(f'payments/successful/{timestamp}').set(paymentDict)
                dbs.reference(f'transactions/{timestamp}').set(paymentDict)
                dbs.reference(f'subscriptions/{transactionid}').set(paymentDict)
            else:
                dbs.reference(f'payments/failed/{timestamp}').set(paymentDict)
                dbs.reference(f'transactions/{timestamp}').set(paymentDict)

        elif subscriptionType == "UNSUB":
            dbs.reference(f'transactions/{timestamp}').set(data)
            dbs.reference(f'unsubscriptions/{transactionid}').set(paymentDict)

    result = json.dumps(mydict)
    return HttpResponse(result, content_type="application/json")






def mySubscription(request):
    if request.method == 'POST':
        try:
            mobile = request.POST.get("mobile").replace(" ", "")
            transactionid = fetchFromFirebase(mobile)
            if not transactionid:
                messages.error(request, _("You are not subscribed"))
                return redirect('subscriptionpage')
            dbs.reference(f'subscriptions/{transactionid}').delete()
            myurl = f"http://52.206.231.182/routesms/bill_v2/unsub/?username={mtnUsername}&password={mtnpassword}&phoneNo={mobile}&productID={mtnproductid}&network={mtnnetwork}"
            import requests
            r = requests.get(url=myurl)
            data = r.json()
            timestamp = int(time.time())
            messages.error(request, _(f"You have been unsubscribed"))
            dbs.reference(f'transactions/{timestamp}').set(data)
            return redirect('homepage')
        except Exception as exception:
            messages.error(request, _(f"An error occured.\n\n{exception}"))
            return redirect('mySubscription')

    if not "mobile" in request.COOKIES.keys():
        messages.error(request, _("Please enter your mobile for access control."))
        return redirect('subscriptionpage')
    else:
        mobile = request.COOKIES.get('mobile')
        transactionid = fetchFromFirebase(mobile)
        if not transactionid:
            messages.error(request, _("You are not subscribed here"))
            return redirect('subscriptionpage')
        if not isUserSubscribed(transactionid):
            return redirect('subscriptionpage')
        else:
            response = render(request, "mysubscription.html", {"username": "User"})
            return response


@never_cache
def subscriptionpage(request):
    userDict = {}
    userDict['name'] = "User"

    video = request.COOKIES.get('video')
    if video is None:
        print("Video Not There")
    else:
        print("Video There")

    if request.method == "POST":
        print("Arrived")
        mobile = request.POST.get("mobile")
        mobile = mobile.replace(" ", "")

        if isFirebaseAvailable(mobile):
            transactionid = fetchFromFirebase(mobile)
            if isUserSubscribed(transactionid):
                if "video" in request.COOKIES.keys():
                    video = request.COOKIES.get('video')
                    bigResponse = redirect('videoviewer', video=video, position=0)
                    bigResponse.set_cookie('uid', transactionid, max_age=31536000)
                    if not "mobile" in request.COOKIES.keys():
                        bigResponse.set_cookie('mobile', mobile, max_age=31536000)
                    else:
                        bigResponse.delete_cookie('mobile')
                        bigResponse.set_cookie('mobile', mobile, max_age=31536000)
                    return bigResponse
                else:
                    theResponse = redirect('videoviewer', video=video, position=0)
                    theResponse.set_cookie('uid', transactionid, max_age=31536000)
                    if not "mobile" in request.COOKIES.keys():
                        theResponse.set_cookie('mobile', mobile, max_age=31536000)
                        print("Done 3")
                    else:
                        theResponse.delete_cookie('mobile')
                        theResponse.set_cookie('mobile', mobile, max_age=31536000)
                        print("Done 4")
                    print("mop")
                    return theResponse

        myurl = f"http://52.206.231.182/routesms/bill_v2/?username={mtnUsername}&password={mtnpassword}&phoneNo={mobile}&productID={mtnproductid}&network={mtnnetwork}"
        import requests
        r = requests.get(url=myurl)
        try:
            data = r.json()

            userid = data['transaction_id']

            subRequest = {}
            subRequest['code'] = data['code']
            subRequest['result'] = data['result']
            subRequest['transaction_id'] = data['transaction_id']
            subRequest['msisdn'] = data['msisdn']
            subRequest['transaction_time'] = data['transaction_time']
            subRequest['mobile'] = mobile
            subRequest['uid'] = userid
            timestamp = int(time.time())
            subRequest['timestamp'] = timestamp
            thestamp = datetime.fromtimestamp(timestamp)
            formatted = thestamp.strftime("%d-%b-%Y")
            subRequest['date'] = formatted
            subRequest['month'] = getDates()['month']
            subRequest['year'] = getDates()['year']
            subRequest['combined'] = getDates()['combined']

            print(f'JSON DATA is {data}')

            subscriptionDict = {}
            subscriptionDict['transid'] = data['transaction_id']
            subscriptionDict['transtamp'] = timestamp
            subscriptionDict['transamount'] = 50

            dbs.reference(f'transactions/{timestamp}').set(subRequest)
            transactionid = data['transaction_id']

            pushToFirebase(transactionid, mobile)

            bigResponse = redirect('homepage')
            bigResponse.set_cookie('uid', transactionid, max_age=31536000)
            if not "mobile" in request.COOKIES.keys():
                bigResponse.set_cookie('mobile', mobile, max_age=31536000)
                print("Done 1")
            else:
                bigResponse.delete_cookie('mobile')
                bigResponse.set_cookie('mobile', mobile, max_age=31536000)
                print("Done 2")
            return bigResponse

        except Exception as exception:
            ourResponse = redirect('subscriptionpage')
            if not "mobile" in request.COOKIES.keys():
                ourResponse.set_cookie('mobile', mobile, max_age=31536000)
                print("Done 5")
            else:
                ourResponse.delete_cookie('mobile')
                ourResponse.set_cookie('mobile', mobile, max_age=31536000)
                print("Done 6")

            messages.error(request, _(f"An error occured {exception}"))
            return ourResponse

    return render(request, "subscriptionpage.html", {"summary": monthsummaryDict})


@never_cache
def adminPage(request):
    if not "login" in request.COOKIES.keys():
        messages.error(request, _("Admin Login is required to visit admin page."))
        return redirect(userlogin)
    else:
        userid = request.COOKIES.get('login')
        useremail = fetchUserData(userid)['email']

        if 'kat' in useremail:
            summaryDict = {}
            summaryDict['universalAmount'] = universalAmount()
            summaryDict['numbertotalSuccessfulPayments'] = numbertotalSuccessfulPayments()
            summaryDict['universalTransactions'] = universalTransactions()

            summaryDict['paymentsNumberForToday'] = paymentsNumberForToday()
            summaryDict['paymentsAmountForToday'] = paymentsAmountForToday()
            summaryDict['todayTransactions'] = todayTransactions()

            summaryDict['unsubscriptions'] = unsubscriptions()
            summaryDict['unsubscriptionTransactions'] = universalUnsubscriptionsTransactions()

            summaryDict['between'] = ""

            if request.method == "POST":
                startdate = datetime.strptime(request.POST.get("startdate"), '%Y-%m-%d').strftime("%d-%b-%Y")
                enddate = datetime.strptime(request.POST.get("enddate"), '%Y-%m-%d').strftime("%d-%b-%Y")
                summaryDict['universalTransactions'] = transactionsForSpecificDay(startdate, enddate)
                summaryDict['unsubscriptionTransactions'] = unsubscriptionTransactionsSpecificDay(startdate, enddate)
                summaryDict['between'] = f"btn {startdate} - {enddate}"
                summaryDict['total'] = totalAmountSpecificDay(startdate, enddate)

            response = render(request, "adminindex.html", {"summary": summaryDict})
            return response

        else:
            messages.error(request, _("You are not authorized to visit this page"))
            return redirect(homepage)



@never_cache
def createsocialproblems(request):

    if request.method == "POST":
        try:
            socialproblemname = request.POST.get("socialproblemtitle")
            socialproblemdescription = request.POST.get("summernote")
            imageUrl = request.POST.get("url")

            if not imageUrl:
                response = render(request, "index.html", {"message": "Social problem not posted! You did not upload image"})
                return response
            else:
                print(f"Found imageurl as {imageUrl}")

            timestamp = int(time.time())

            bundle = {}
            bundle["image"] = imageUrl
            bundle["name"] = socialproblemname
            bundle["description"] = socialproblemdescription
            bundle["timestamp"] = -timestamp

            dbs.reference(f'view/socialproblems/image').set(bundle)
            dbs.reference(f'cartoons/socialproblems/{timestamp}').set(bundle)

        except:
            response = render(request, "createsocialproblems.html", {"message": "An error occured! Social Problem was not uploaded"})
            return response
        else:
            response = render(request, "index.html", {"message": "Social Problem uploaded sucessfuly"})
            return response

    response = render(request, "createsocialproblems.html", {"summary": monthsummaryDict})
    return response



@never_cache
def editsocialproblems(request, socialproblemid):

    thedict = {}

    description = dbs.reference(f'cartoons/socialproblems/{socialproblemid}').child("description").get()
    image = dbs.reference(f'cartoons/socialproblems/{socialproblemid}').child("image").get()
    name = dbs.reference(f'cartoons/socialproblems/{socialproblemid}').child("name").get()
    timestamp = socialproblemid

    thedict["description"] = description
    thedict["image"] = image
    thedict["name"] = name
    thedict["timestamp"] = timestamp

    if request.method == "POST":
        try:
            imageUrl = request.POST.get("url")
            if imageUrl:
                print("Image is there")
                image = imageUrl
            else:
                print("image is not there")

            socialproblemsname = request.POST.get("socialproblemtitle")
            socialproblemsdescription = request.POST.get("summernote")
            imageUrl = image

            bundle = {}
            bundle["image"] = imageUrl
            bundle["name"] = socialproblemsname
            bundle["description"] = socialproblemsdescription
            bundle["timestamp"] = -int(timestamp)

            dbs.reference(f'cartoons/socialproblems/{timestamp}').set(bundle)

        except:
            response = render(request, "editsocialproblemspage.html", {"message": "An error occured! Social Problem was not uploaded"})
            return response
        else:
            response = render(request, "index.html", {"message": "Social Problem edited sucessfuly"})
            monthsummaryDict['loadsocialproblems'] = loadsocialproblems()
            return response

    response = render(request, "editsocialproblemspage.html", {"summary": thedict})
    return response



@never_cache
def consultancy(request):
    response = render(request, "consultancy.html", {"summary": monthsummaryDict})
    return response


@never_cache
def editteam(request):

    columnists = getColumnists()
    positions = getPositions()
    objectives = getObjectives()
    mission = getMission()
    positiontitles = getPositionTitles()

    monthsummaryDict['columnists'] = columnists
    monthsummaryDict['positions'] = positions
    monthsummaryDict['objectives'] = objectives
    monthsummaryDict['mission'] = mission
    monthsummaryDict['positiontitles'] = positiontitles

    if request.method == 'POST':
        title = request.POST.get('title')
        name = request.POST.get('name')
        positionname = request.POST.get('positionname')
        columnistname = request.POST.get('columnistname')
        columnistdescription = request.POST.get('columnistdescription')
        objective = request.POST.get('objective')
        mission = request.POST.get('mission')

        if name:
            if not title or not name:
                response = render(request, 'team-edit.html', {"message": "Ensure all fields are filled"})
                return response
            else:
                timestamp = int(time.time())
                thedict = {
                    'title' : title,
                    'name': name,
                    'timestamp': timestamp
                }
                dbs.reference(f'positions/{title}/employee/{timestamp}').set(thedict)

                messages.success(request, 'Field added succesfully')
                return redirect('editteam')

        if positionname:
           timestamp = int(time.time())
           thedict = {
               'title': positionname,
               'timestamp': timestamp,
               'position': 9
           }
           dbs.reference(f'positions/{positionname}').set(thedict)
           messages.success(request, 'Field added succesfully')
           return redirect('editteam')

        if columnistname:
            timestamp = int(time.time())
            thedict = {
                'description': columnistdescription,
                'timestamp': timestamp,
                'name': columnistname
            }
            dbs.reference(f'columnists/{timestamp}').set(thedict)
            messages.success(request, 'Field added succesfully')
            return redirect('editteam')

        if objective:
            timestamp = int(time.time())
            thedict = {
                'timestamp': timestamp,
                'name': objective
            }
            dbs.reference(f'objectives/{timestamp}').set(thedict)
            messages.success(request, 'Field added succesfully')
            return redirect('editteam')

        if mission:
            dbs.reference(f'profile/mission').set(mission)
            messages.success(request, 'Field added succesfully')
            return redirect('editteam')


    response = render(request, "team-edit.html", {"summary": monthsummaryDict})
    return response



@never_cache
def deleteEmployee(request, positionname, employeetimestamp):
    if positionname:
        print("Here")
        dbs.reference(f'positions/{positionname}/employee/{employeetimestamp}').delete()
        messages.success(request, 'Field deleted succesfully')
        return redirect('editteam')



@never_cache
def deletePosition(request, positionName):
    if positionName:
        print("Here")
        dbs.reference(f'positions/{positionName}').delete()
        messages.success(request, 'Field deleted succesfully')
        return redirect('editteam')


@never_cache
def deletecolumnist(request, columnisttimestamp):
    if columnisttimestamp:
        print("Here")
        dbs.reference(f'columnists/{columnisttimestamp}').delete()
        messages.success(request, 'Field deleted succesfully')
        return redirect('editteam')


@never_cache
def deleteobjective(request, objectivetimestamp):
    if objectivetimestamp:
        dbs.reference(f'objectives/{objectivetimestamp}').delete()
        messages.success(request, 'Field deleted succesfully')
        return redirect('editteam')











@never_cache
def createproverbs(request):

    if request.method == "POST":
        try:
            proverbname = request.POST.get("proverbtitle")
            proverbdescription = request.POST.get("summernote")
            imageUrl = request.POST.get("url")

            if not imageUrl:
                response = render(request, "index.html", {"message": "Proverb not posted! You did not upload image"})
                return response
            else:
                print(f"Found imageurl as {imageUrl}")

            timestamp = int(time.time())

            bundle = {}
            bundle["image"] = imageUrl
            bundle["name"] = proverbname
            bundle["description"] = proverbdescription
            bundle["timestamp"] = -timestamp

            dbs.reference(f'view/proverbs/image').set(bundle)
            dbs.reference(f'cartoons/proverbs/{timestamp}').set(bundle)

        except:
            response = render(request, "createproverbs.html", {"message": "An error occured! Proverb was not uploaded"})
            return response
        else:
            response = render(request, "index.html", {"message": "Proverb uploaded sucessfuly"})
            return response

    response = render(request, "createproverb.html", {"summary": monthsummaryDict})
    return response



@never_cache
def editproverbs(request, proverbid):

    thedict = {}

    description = dbs.reference(f'cartoons/proverbs/{proverbid}').child("description").get()
    image = dbs.reference(f'cartoons/proverbs/{proverbid}').child("image").get()
    name = dbs.reference(f'cartoons/proverbs/{proverbid}').child("name").get()
    timestamp = proverbid

    thedict["description"] = description
    thedict["image"] = image
    thedict["name"] = name
    thedict["timestamp"] = timestamp

    if request.method == "POST":
        try:
            imageUrl = request.POST.get("url")
            if imageUrl:
                print("Image is there")
                image = imageUrl
            else:
                print("image is not there")

            proverbsname = request.POST.get("proverbtitle")
            proverbsdescription = request.POST.get("summernote")
            imageUrl = image

            bundle = {}
            bundle["image"] = imageUrl
            bundle["name"] = proverbsname
            bundle["description"] = proverbsdescription
            bundle["timestamp"] = -int(timestamp)

            dbs.reference(f'cartoons/proverbs/{timestamp}').set(bundle)

        except:
            response = render(request, "editproverb.html", {"message": "An error occured! Proverb was not uploaded"})
            return response
        else:
            response = render(request, "index.html", {"message": "Proverb edited sucessfuly"})
            monthsummaryDict['loadproverbs'] = loadproverbs()
            return response

    response = render(request, "editproverb.html", {"summary": thedict})
    return response
