from django.shortcuts import render
from django.views.decorators.cache import never_cache, cache_control

from testPython import loadhumour, loadjabs, loadquotes, loadsocialproblems, loadproverbs, loadlongcomics, \
    loadillustrationnames, loadillustrationcontent, loadconthumournames, loadconthumourcontent, \
    loadmagazines, loadnewscategories, dbs, loadnewslocations, latestcartoon, latestmagazine, latestnews, \
    latestvideo, fetchsliderimages, latestnewsone, loadmoresinglecomics

monthsummaryDict = {}
monthsummaryDict['sliderimages'] = fetchsliderimages()
monthsummaryDict['longcomics'] = loadlongcomics()

@never_cache
@cache_control(must_revalidate=True)
def homepage(request):
    monthsummaryDict['loadmagazines'] = loadmagazines()
    monthsummaryDict['latestcartoon'] = latestcartoon()
    monthsummaryDict['latestmagazine'] = latestmagazine()
    monthsummaryDict['latestvideo'] = latestvideo()
    monthsummaryDict['latestnewsone'] = latestnewsone()
    response = render(request, "index.html", {"summary": monthsummaryDict})
    return response

@never_cache
@cache_control(must_revalidate=True)
def cartoonspage(request):
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
    monthsummaryDict['loadjabs'] = loadjabs()
    response = render(request, "jabspage.html", {"summary": monthsummaryDict})
    return response

@never_cache
@cache_control(must_revalidate=True)
def quotespage(request):
    monthsummaryDict['loadquotes'] = loadquotes()
    response = render(request, "quotespage.html", {"summary": monthsummaryDict})
    return response

@never_cache
@cache_control(must_revalidate=True)
def socialproblemspage(request):
    monthsummaryDict['loadsocialproblems'] = loadsocialproblems()
    response = render(request, "socialproblemspage.html", {"summary": monthsummaryDict})
    return response

@never_cache
@cache_control(must_revalidate=True)
def proverbspage(request):
    monthsummaryDict['loadproverbs'] = loadproverbs()
    response = render(request, "proverbspage.html", {"summary": monthsummaryDict})
    return response

@never_cache
@cache_control(must_revalidate=True)
def longcomicspage(request):
    monthsummaryDict['longcomics'] = loadlongcomics()
    response = render(request, "longcomicspage.html", {"summary": monthsummaryDict})
    return response

@never_cache
@cache_control(must_revalidate=True)
def illustrationnamespage(request):
    monthsummaryDict['illustrationnames'] = loadillustrationnames()
    response = render(request, "illustrationnamespage.html", {"summary": monthsummaryDict})
    return response

@never_cache
@cache_control(must_revalidate=True)
def illustrationcontentpage(request, illustrationname):
    monthsummaryDict['illustrationcontent'] = loadillustrationcontent(illustrationname)
    response = render(request, "illustrationcontentpage.html", {"summary": monthsummaryDict})
    return response

@never_cache
@cache_control(must_revalidate=True)
def conthumournamespage(request):
    monthsummaryDict['conthumournames'] = loadconthumournames()
    response = render(request, "conthumournamespage.html", {"summary": monthsummaryDict})
    return response

@never_cache
@cache_control(must_revalidate=True)
def conthumourcontentpage(request, conthumourname):
    monthsummaryDict['conthumourcontent'] = loadconthumourcontent(conthumourname)
    response = render(request, "conthumourcontentpage.html", {"summary": monthsummaryDict})
    return response

@never_cache
@cache_control(must_revalidate=True)
def pdfviewerpage(request, thepdf):
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
    newsdict['description'] = dbs.reference(f'news/news/{identity}/description').get().replace('\n', '<br />')
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
    monthsummaryDict['loadhumour'] = loadhumour()
    monthsummaryDict['loadmoresinglecomics'] = loadmoresinglecomics()
    response = render(request, "humourpage.html", {"summary": monthsummaryDict})
    return response