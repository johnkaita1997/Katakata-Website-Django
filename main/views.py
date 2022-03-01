from django.shortcuts import render

from testPython import loadhumour, loadjabs, loadquotes, loadsocialproblems, loadproverbs, loadlongcomics, \
    loadillustrationnames, loadillustrationcontent, loadconthumournames, loadconthumourcontent, loadvideos, \
    loadmagazines, loadnewscategories, dbs, loadnewslocations, latestcartoon, latestmagazine, latestnews, latestvideo

monthsummaryDict = {}
monthsummaryDict['loadhumour'] = loadhumour()
monthsummaryDict['loadjabs'] = loadjabs()
monthsummaryDict['loadquotes'] = loadquotes()
monthsummaryDict['loadsocialproblems'] = loadsocialproblems()
monthsummaryDict['loadproverbs'] = loadproverbs()
monthsummaryDict['longcomics'] = loadlongcomics()
monthsummaryDict['illustrationnames'] = loadillustrationnames()
monthsummaryDict['conthumournames'] = loadconthumournames()
monthsummaryDict['loadvideos'] = loadvideos()
monthsummaryDict['loadmagazines'] = loadmagazines()
monthsummaryDict['loadnewscategories'] = loadnewscategories()
monthsummaryDict['loadnewslocations'] = loadnewslocations()
monthsummaryDict['latestnews'] = latestnews()
monthsummaryDict['latestcartoon'] = latestcartoon()
monthsummaryDict['latestmagazine'] = latestmagazine()
monthsummaryDict['latestvideo'] = latestvideo()

def homepage(request):
    response = render(request, "index.html", {"summary": monthsummaryDict})
    return response


def cartoonspage(request):
    response = render(request, "humourpage.html", {"summary": monthsummaryDict})
    return response


def imageviewer(request, theimage):
    response = render(request, "imageviewer.html", {"theimage": theimage})
    return response


def jabspage(request):
    response = render(request, "jabspage.html", {"summary": monthsummaryDict})
    return response


def quotespage(request):
    response = render(request, "quotespage.html", {"summary": monthsummaryDict})
    return response


def socialproblemspage(request):
    response = render(request, "socialproblemspage.html", {"summary": monthsummaryDict})
    return response


def proverbspage(request):
    response = render(request, "proverbspage.html", {"summary": monthsummaryDict})
    return response


def longcomicspage(request):
    response = render(request, "longcomicspage.html", {"summary": monthsummaryDict})
    return response


def illustrationnamespage(request):
    response = render(request, "illustrationnamespage.html", {"summary": monthsummaryDict})
    return response


def illustrationcontentpage(request, illustrationname):
    monthsummaryDict['illustrationcontent'] = loadillustrationcontent(illustrationname)
    response = render(request, "illustrationcontentpage.html", {"summary": monthsummaryDict})
    return response


def conthumournamespage(request):
    response = render(request, "conthumournamespage.html", {"summary": monthsummaryDict})
    return response


def conthumourcontentpage(request, conthumourname):
    monthsummaryDict['conthumourcontent'] = loadconthumourcontent(conthumourname)
    response = render(request, "conthumourcontentpage.html", {"summary": monthsummaryDict})
    return response


def pdfviewerpage(request, thepdf):
    monthsummaryDict['thepdf'] = thepdf
    response = render(request, "pdfviewer.html", {"summary": monthsummaryDict})
    return response

def newspage(request):
    response = render(request, "newspage.html", {"summary": monthsummaryDict})
    return response

def newsviewer(request, newsid):
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

    response = render(request, "newsviewer.html", {"summary": newsdict})
    return response


def teampage(request):
    response = render(request, "team.html", {"summary": monthsummaryDict})
    return response
