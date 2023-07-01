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
from checker.views import weekly_checkup_all_list,download_facebookurl_list,download_excel2,weekly_check_facebookurl_list
from checker.views import login_view, signup_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/checker/', add_socialmediaurl, name='add_socialmediaurl'),
    path('dashboard/addfburl/', add_facebookURL, name='add_facebookURL'),
    path('dashboard/urls/', socialmediaurl_list, name='socialmediaurl_list'),
    path('refresh-url/', refresh_url, name='refresh_url'),
    path('refresh-url2/', refresh2, name='refresh2'),
    path('dashboard/urls2/',facebookurl_list,name='facebookurl_list'),
    path('dashboard/results_all/',results_all,name='results_all'),
    path('update_status/',update_status,name='update_status'),
    path('update_status2/',update_status2,name='update_status2'),
    path('dashboard/download_all_links/',downloadreport_all_links,name='downloadreport_all_links'),
    path('download-excel/', download_excel, name='download_excel'),
    path('dashboard/weekly_checkup_all_list/', weekly_checkup_all_list, name='weekly_checkup_all_list'),
    path('dashboard/download_facebookurl_list/',download_facebookurl_list,name='download_facebookurl_list'),
    path('download/excel/', download_excel2, name='download_excel2'),
    path('dashboard/weekly_check_facebookurl_list/',weekly_check_facebookurl_list,name='weekly_check_facebookurl_list')
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
