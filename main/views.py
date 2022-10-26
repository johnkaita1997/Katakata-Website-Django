import smtplib
import time
from datetime import datetime
from email.message import EmailMessage

from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.views.decorators.cache import never_cache, cache_control

from testPython import *

monthsummaryDict = {}


# if not 'sliderimages' in monthsummaryDict.keys():
#     monthsummaryDict['sliderimages'] = fetchsliderimages()
# if not 'longcomics' in monthsummaryDict.keys():
#     monthsummaryDict['longcomics'] = loadlongcomics(long)


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


@never_cache
@cache_control(must_revalidate=True)
def homepage(request):
    callMainData()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

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
@cache_control(must_revalidate=True)
def cartoonspage(request):
    if not 'latestcartoon' in monthsummaryDict.keys():
        monthsummaryDict['loadlongcomics'] = longcomicsall(num_LongComics())
        monthsummaryDict['latestcartoon'] = latestcartoon()
    response = render(request, "longcomicspage.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def imageviewer(request, theimage):
    response = render(request, "imageviewer.html", {"theimage": theimage})
    return response


@never_cache
@cache_control(must_revalidate=True)
def jabspage(request):
    if not 'loadjabs' in monthsummaryDict.keys():
        monthsummaryDict['loadjabs'] = loadjabs()
    response = render(request, "jabspage.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def quotespage(request):
    if not 'loadquotes' in monthsummaryDict.keys():
        monthsummaryDict['loadquotes'] = loadquotes()
        response = render(request, "quotespage.html", {"summary": monthsummaryDict})
        return response


@never_cache
@cache_control(must_revalidate=True)
def socialproblemspage(request):
    if not 'loadsocialproblems' in monthsummaryDict.keys():
        monthsummaryDict['loadsocialproblems'] = loadsocialproblems()
        response = render(request, "socialproblemspage.html", {"summary": monthsummaryDict})
        return response


@never_cache
@cache_control(must_revalidate=True)
def proverbspage(request):
    if not 'loadproverbs' in monthsummaryDict.keys():
        monthsummaryDict['loadproverbs'] = loadproverbs()
    response = render(request, "proverbspage.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def longcomicspage(request):
    monthsummaryDict['longcomics'] = loadlongcomics()
    monthsummaryDict['loadlongcomics'] = longcomicsall(num_LongComics())
    response = render(request, "longcomicspage.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def illustrationnamespage(request):
    if not 'illustrationnames' in monthsummaryDict.keys():
        monthsummaryDict['illustrationnames'] = loadillustrationnames()
    response = render(request, "illustrationnamespage.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def illustrationcontentpage(request, illustrationname):
    if not 'illustrationcontent' in monthsummaryDict.keys():
        monthsummaryDict['illustrationcontent'] = loadillustrationcontent(illustrationname)
    response = render(request, "illustrationcontentpage.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def conthumournamespage(request):
    if not 'conthumournames' in monthsummaryDict.keys():
        monthsummaryDict['conthumournames'] = loadconthumournames()
    response = render(request, "conthumournamespage.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def conthumourcontentpage(request, conthumourname):
    if not 'conthumourcontent' in monthsummaryDict.keys():
        monthsummaryDict['conthumourcontent'] = loadconthumourcontent(conthumourname)
    response = render(request, "conthumourcontentpage.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def pdfviewerpage(request, thepdf):
    if not 'thepdf' in monthsummaryDict.keys():
        monthsummaryDict['thepdf'] = thepdf
    response = render(request, "pdfviewer.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def newspage(request):
    monthsummaryDict['latestnews'] = latestnews()
    monthsummaryDict['loadnewslocations'] = loadnewslocations()
    monthsummaryDict['loadnewscategories'] = loadnewscategories()

    response = render(request, "newspage.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
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
@cache_control(must_revalidate=True)
def teampage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        usermessage = request.POST.get('message')

        if not name or not email or not usermessage:
            response = render(request, 'team.html', {"message": "Ensure all fields are filled"})
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
@cache_control(must_revalidate=True)
def shoppage(request):
    response = render(request, "shoppage.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def productdetails(request):
    response = render(request, "productdetails.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def cartpage(request):
    response = render(request, "cartpage.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def humourpage(request):
    if not 'loadhumour' in monthsummaryDict.keys():
        monthsummaryDict['loadhumour'] = loadhumour()

    if not 'loadmoresinglecomics' in monthsummaryDict.keys():
        monthsummaryDict['loadmoresinglecomics'] = loadmoresinglecomics()
    response = render(request, "humourpage.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def videos(request, video):
    response = render(request, "videos.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def shortcomicsviewer(request, shortcomic):
    if not 'shortcomics' in monthsummaryDict.keys():
        monthsummaryDict['shortcomics'] = androidloadspecificshortcomic(shortcomic)

    if not 'name' in monthsummaryDict.keys():
        monthsummaryDict['name'] = shortcomic
    response = render(request, "shortcomicsviewer.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def missionpage(request):
    response = render(request, "mission.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def satvideos(request):
    monthsummaryDict['satvideos'] = androidvideos(100000000)
    response = render(request, "satvideos.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def satmagazines(request):
    monthsummaryDict['allsatmagazines'] = androidloadmagazines(10000000)
    response = render(request, "satmagazines.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def satlongcomics(request):
    monthsummaryDict['longcomics'] = longcomicsall(100000)
    response = render(request, "satlongcomics.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
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
@cache_control(must_revalidate=True)
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
@cache_control(must_revalidate=True)
def contactus(request):
    response = render(request, "contactus.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
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
@cache_control(must_revalidate=True)
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
@cache_control(must_revalidate=True)
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
@cache_control(must_revalidate=True)
def userlogin(request):
    if request.method == "POST":
        try:
            email = request.POST.get("email").strip()
            password = request.POST.get("password").strip()

            try:
                login = auth.sign_in_with_email_and_password(email, password)
                userid = login['localId']
                if not "uid" in request.COOKIES.keys():
                    response = redirect('homepage')
                    response.set_cookie('uid', userid)
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
@cache_control(must_revalidate=True)
def userReg(request):
    if request.method == "POST":
        try:
            email = request.POST.get("email").strip()
            name = request.POST.get("name").strip()
            password = request.POST.get("password").strip()

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
                    dbs.reference(f'users/{userid}').set(userDict)
                except Exception as exception:
                    messages.error(request, _(f"An error occured!\n{exception}"))
                else:
                    if not "uid" in request.COOKIES.keys():
                        response = redirect('homepage')
                        response.set_cookie('uid', userid)
                        messages.error(request, _(f"You are already logged in"))
                        return redirect('homepage')
                    else:
                        messages.error(request, _(f"You are already logged in"))
                        return redirect('homepage')

        except Exception as exception:
            messages.error(request, _(f"An error occured!\n{exception}"))
            response = redirect('userReg')

            return response

    response = render(request, "register.html", {"summary": monthsummaryDict})
    return response


@never_cache
@cache_control(must_revalidate=True)
def videoviewer(request, video, position):

    try:
        loggedin = "uid" in request.COOKIES.keys()
        theposition = int(position)
        defaultTimestamp = list(androidloadspecificvideo(video).keys())[int(theposition)]
        defaultVideo = androidloadspecificvideo(video)[f'{defaultTimestamp}']
        monthsummaryDict['videos'] = androidloadspecificvideo(video)
        monthsummaryDict['name'] = video
        monthsummaryDict['default'] = monthsummaryDict['name'][theposition]
        monthsummaryDict['default'] = defaultVideo
        monthsummaryDict['loggedin'] = loggedin

        if request.method == "POST":
            try:
                comment = request.POST.get("comment")
                if not comment:
                    messages.error(request, _("You have entered no message."))
                    return redirect('videoviewer', video=defaultVideo['name'], position=theposition)
                else:
                    if not "uid" in request.COOKIES.keys():
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
                        userid = request.COOKIES.get('uid')

                        print(timestamp)
                        name = getUserName(userid)['name']
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
    except Exception as exception:
        response = render(request, "videoviewer.html", {"summary": monthsummaryDict, 'alert': False})
        return response

    response = render(request, "videoviewer.html", {"summary": monthsummaryDict, 'alert': False})
    return response


def logout(request):
    response = redirect('userlogin')
    response.delete_cookie('uid')
    return response