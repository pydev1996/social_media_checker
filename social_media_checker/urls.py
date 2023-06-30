from django.contrib import admin
from django.urls import path, include
from checker.views import socialmediaurl_list
from checker.views import add_socialmediaurl
from checker.views import facebookurl_list
from checker.views import dashboard
from checker.views import add_facebookURL
from checker.views import update_status
from checker.views import update_status2
from checker.views import refresh_url
from checker.views import refresh2
from checker.views import results_all
from checker.views import downloadreport_all_links
from checker.views import download_excel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checker/', add_socialmediaurl, name='add_socialmediaurl'),
    path('addfburl/', add_facebookURL, name='add_facebookURL'),
    path('urls/', socialmediaurl_list, name='socialmediaurl_list'),
    path('refresh-url/', refresh_url, name='refresh_url'),
    path('refresh-url2/', refresh2, name='refresh2'),
    path('urls2/',facebookurl_list,name='facebookurl_list'),
    path('dashbord/',dashboard,name='dashbord'),
    path('results_all/',results_all,name='results_all'),
    path('update_status/',update_status,name='update_status'),
    path('update_status2/',update_status2,name='update_status2'),
    path('download_all_links/',downloadreport_all_links,name='downloadreport_all_links'),
    
    path('download-excel/', download_excel, name='download_excel'),


]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
