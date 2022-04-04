from django.urls import path

from main import views as mainviews

urlpatterns = [

    path('', mainviews.homepage, name="homepage"),
    path('newspage', mainviews.newspage, name="newspage"),
    path('shoppage', mainviews.shoppage, name="shoppage"),
    path('humourpage', mainviews.humourpage, name="humourpage"),
    path('cartpage', mainviews.cartpage, name="cartpage"),
    path('productdetails', mainviews.productdetails, name="productdetails"),
    path('cartoonspage', mainviews.cartoonspage, name="cartoonspage"),
    path('jabspage', mainviews.jabspage, name="jabspage"),
    path('teampage', mainviews.teampage, name="teampage"),
    path('quotespage', mainviews.quotespage, name="quotespage"),
    path('socialproblemspage', mainviews.socialproblemspage, name="socialproblemspage"),
    path('proverbspage', mainviews.proverbspage, name="proverbspage"),
    path('longcomicspage', mainviews.longcomicspage, name="longcomicspage"),
    path('imageviewer/<path:theimage>', mainviews.imageviewer, name="imageviewer"),
    path('illustrationnamespage', mainviews.illustrationnamespage, name="illustrationnamespage"),
    path('illustrationcontentpage/<str:illustrationname>', mainviews.illustrationcontentpage,name="illustrationcontentpage"),
    path('pdfviewerpage/<path:thepdf>', mainviews.pdfviewerpage, name="pdfviewerpage"),
    path('conthumournamespage', mainviews.conthumournamespage, name="conthumournamespage"),
    path('conthumourcontentpage/<str:conthumourname>', mainviews.conthumourcontentpage, name="conthumourcontentpage"),
    path('newsviewer/<str:newsid>', mainviews.newsviewer, name="newsviewer"),
    # path('androidpage', mainviews.androidpage, name="androidpage"),

    path('videoviewer/<path:video>', mainviews.videoviewer,name="videoviewer"),
    path('shortcomicsviewer/<str:shortcomic>', mainviews.shortcomicsviewer,name="shortcomicsviewer"),
    path('missionpage', mainviews.missionpage, name="missionpage"),
    path('satvideos', mainviews.satvideos, name="satvideos"),
    path('satmagazines', mainviews.satmagazines, name="satmagazines"),
    path('satlongcomics', mainviews .satlongcomics, name="satlongcomics"),
    path('newsletter/<str:namer>/<str:emailer>', mainviews.newsletter, name="newsletter"),
    path('unsubscribe/<str:email>', mainviews.unsubscribe, name="unsubscribe"),
    path('contactus', mainviews.contactus, name="contactus")
    #path('contactus', mainviews.contactus, name="contactus")

]
