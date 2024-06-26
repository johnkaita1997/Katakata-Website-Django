from django.conf import settings
from django.conf.urls.static import static
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
    path('videoviewer/<str:video>/<str:position>', mainviews.videoviewer, name="videoviewer"),
    path('shortcomicsviewer/<str:shortcomic>', mainviews.shortcomicsviewer, name="shortcomicsviewer"),
    path('missionpage', mainviews.missionpage, name="missionpage"),
    path('satvideos', mainviews.satvideos, name="satvideos"),
    path('satmagazines', mainviews.satmagazines, name="satmagazines"),
    path('satlongcomics', mainviews.satlongcomics, name="satlongcomics"),
    path('newsletter/<str:namer>/<str:emailer>', mainviews.newsletter, name="newsletter"),
    path('unsubscribe/<str:email>', mainviews.unsubscribe, name="unsubscribe"),
    path('contactus', mainviews.contactus, name="contactus"),
    path('createnews', mainviews.createnews, name="createnews"),
    path('editnews/<path:newsid>', mainviews.editnews, name="editnews"),
    path('news/<str:newsid>', mainviews.news, name="news"),
    path('videos/<path:video>', mainviews.videos, name="videos"),
    path('userlogin', mainviews.userlogin, name="userlogin"),
    path('userReg', mainviews.userReg, name="userReg"),
    path('logout', mainviews.logout, name="logout"),
    path('subscription', mainviews.Subscription.as_view(), name="subscription"),
    path('callback', mainviews.callback, name="callback"),
    path('mySubscription', mainviews.mySubscription, name="mySubscription"),
    path('subscriptionpage', mainviews.subscriptionpage, name="subscriptionpage"),
    path('adminpage', mainviews.adminPage, name="adminpage"),
    path('createsocialproblem', mainviews.createsocialproblems, name="createsocialproblems"),
    path('editsocialproblem/<path:socialproblemid>', mainviews.editsocialproblems, name="editsocialproblems"),
    path('consultancy', mainviews.consultancy, name="consultancy"),
    path('marketing', mainviews.marketing, name="marketing"),
    path('graphicdesign', mainviews.graphicdesign, name="graphicdesign"),
    path('uploadsamplevideo', mainviews.uploadSampleVideo, name="uploadsamplevideo"),
    path('viewsamplevideos', mainviews.viewsamplevideos, name="viewsamplevideos"),
    path('samplevideoviewer/<str:timestamp>/', mainviews.samplevideoviewer, name="samplevideoviewer"),

    # Define a URL pattern for 'editteam' with optional parameters
    path('editteam/', mainviews.editteam, name="editteam"),
    path('deletePosition/<str:positionName>/', mainviews.deletePosition, name="deleteposition"),
    path('deleteEmployee/<str:positionname>/<int:employeetimestamp>/', mainviews.deleteEmployee, name="deleteemployee"),
    path('deletecolumnist/<int:columnisttimestamp>/', mainviews.deletecolumnist, name="deletecolumnist"),
    path('deleteobjective/<int:objectivetimestamp>/', mainviews.deleteobjective, name="deleteobjective"),

    path('createproverb', mainviews.createproverbs, name="createproverbs"),
    path('editproverb/<path:proverbid>', mainviews.editproverbs, name="editproverbs"),

]