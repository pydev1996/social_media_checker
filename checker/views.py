from django.http import JsonResponse
import requests
from .models import SocialMediaURL
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import re
df=pd.read_excel("C:/Users/dell/Downloads/social_media_checker/checker/test.xlsx")
urls2=df.iloc[:,0].values.tolist()
urls2=[str(i) for i in urls2]


def is_valid_youtube_url(url):
    # Extract video ID from the URL
    video_id = extract_video_id(url)
    if video_id is None:
        return False

    # Create a YouTube Data API client
    api_service_name = "youtube"
    api_version = "v3"
    api_key = "AIzaSyA5X5Dxyn3QbvEcQCLQrEZTWvDA6wrOLeE"  # Replace with your own API key
    youtube = build(api_service_name, api_version, developerKey=api_key)

    try:
        # Send a request to the API to get video details
        response = youtube.videos().list(
            part="snippet",
            id=video_id
        ).execute()

        # Check if the video exists
        if response.get("items"):
            return True
        else:
            return False

    except HttpError:
        return False

def extract_video_id(url):
    # Extract video ID from various URL formats
    video_id = None
    patterns = [
        r"(?:https?:\/\/)?(?:www\.)?youtu\.?be(?:\.com)?\/(?:watch\?v=|embed\/|v\/|shorts\/|playlist\?list=)?([a-zA-Z0-9_-]{11})",
        r"([a-zA-Z0-9_-]{11})"
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            video_id = match.group(1)
            break
    return video_id

# Example usage



from django.shortcuts import render, redirect
from .forms import SocialMediaURLForm
from .forms import facebookURLForm
from .models import facebookURL

def add_socialmediaurl(request):
    if request.method == 'POST':
        form = SocialMediaURLForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Replace 'success' with the URL name for the success page
    else:
        form = SocialMediaURLForm()
    
    context = {'form': form}
    return render(request, 'add_socialmediaurl.html', context)
def add_facebookURL(request):
    if request.method == 'POST':
        form = facebookURLForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
                    
            # Replace 'success' with the URL name for the success page
    else:
        form = facebookURLForm()
    
    context = {'form': form}
    
    return render(request, 'add_facebookurl.html', context)
from django.shortcuts import render
from .models import SocialMediaURL


def socialmediaurl_list(request):
    urls = SocialMediaURL.objects.all()
    youtube_urls = SocialMediaURL.objects.filter(hisposturl__icontains='youtube.com')
    tiktok_urls = SocialMediaURL.objects.filter(hisposturl__icontains='/www.tiktok.com/')
    twitter_urls = SocialMediaURL.objects.filter(hisposturl__icontains='twitter.com/')
    print(twitter_urls)
    context = {'urls':urls,
                'youtube_urls': youtube_urls,
                'twitter_urls': twitter_urls,
               'tiktoc_urls':tiktok_urls}
    return render(request, 'socialmediaurl_list.html',context)
from django.http import HttpResponse
def refresh_url(request):
    urls = SocialMediaURL.objects.all()
    
    for i in urls:
        
            if "youtube.com/watch?v="  in str(i) or "youtube.com/shorts" in str(i) :
                if is_valid_youtube_url(str(i)):
                    status = SocialMediaURL.objects.get(hisposturl=str(i))
                    status.status = 'ON'
                    status.save()
                else:
                    status = SocialMediaURL.objects.get(hisposturl=str(i))
                    status.status = 'OFF'
                    status.save()
            if "/www.tiktok.com/" in str(i):
                
            
                max_retries = 3
                retry_delay = 2
                
                for j in range(max_retries):
                    try:
                        response = requests.head(str(i))
            
                        
                        if response.status_code == 200:
                            status = SocialMediaURL.objects.get(hisposturl=str(i))
                            status.status = 'ON'
                            status.save()
                        else:
                            status = SocialMediaURL.objects.get(hisposturl=str(i))
                            status.status = 'OFF'
                            status.save()
                        break
                    except requests.exceptions.ConnectionError:
                        if j < max_retries - 1:
                            time.sleep(retry_delay)
                            continue
                        status = SocialMediaURL.objects.get(hisposturl=str(i))
                        status.status = 'OFF'
                        status.save()
    return HttpResponse("Refresh complete")        
def rfresh2():
    usr="6301708990"
    pwd="Naveen@111"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument("--start-maximized")
    options.add_argument('--headless')
    options.add_experimental_option( "prefs", {'protocol_handler.excluded_schemes.tel': False})
    driver = webdriver.Chrome("C:/chromedriver.exe",chrome_options=options)
    driver.get('https://www.facebook.com/')
    sleep(1)
    username_box = driver.find_element(By.XPATH,'//*[@id="email"]') 
    username_box.send_keys(usr)
    sleep(1)
    password_box = driver.find_element(By.XPATH,'//*[@id="pass"]')
    password_box.send_keys(pwd)
    login_box = driver.find_element('xpath','/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
    login_box.click()
    sleep(2)
    urls = facebookURL.objects.all()
    
    for i in urls:
        
        if "/www.facebook.com" in str(i) or '/m.facebook.com/ in str(i)':
                driver.get(str(i))
                
                
                try:
                    d=driver.find_element(By.XPATH,'//*[@id="facebook"]/body')
                    print("-------")
                    print(d.text)
                    print("-------")
                    if "This content isn't available at the moment" in d.text:
                        print("OFF")
                        status=facebookURL.objects.get(url=str(i))
                        status.status="OFF"
                        status.save()
                    else:
                        print("ON")
                        status=facebookURL.objects.get(url=str(i))
                        status.status="ON"
                        status.save()
                except:
                    print("ON")
                    status=facebookURL.objects.get(url=str(i))
                    status.status="ON"
                    status.save()   
    

                
            
        

def facebookurl_list(request):
    urls = facebookURL.objects.all()
    context={"urls":urls}
    return render(request, 'facebookurl_list.html', context)
from django.shortcuts import render
from .models import facebookURL, SocialMediaURL

from django.shortcuts import render
from .models import facebookURL, SocialMediaURL

def dashboard(request):
    urls = facebookURL.objects.all()
    urls2 = SocialMediaURL.objects.all()
    profile=0
    groups=0
    pages=0
    for i in urls:
        if 'profile' in str(i):
            profile+=1
        elif 'group' in str(i):
            groups+=1
        elif 'pages' in str(i):
            pages+=1
    total = len(urls) + len(urls2)
    fb_status_values = facebookURL.objects.values_list('status', flat=True)
    youtube_status_values = SocialMediaURL.objects.values_list('status', flat=True)

    combined_status_values = list(fb_status_values) + list(youtube_status_values)

    total_on_count = combined_status_values.count('ON')
    total_off_count = combined_status_values.count('OFF')

    fb_on_count = list(fb_status_values).count('ON')
    fb_off_count = list(fb_status_values).count('OFF')

    youtube_on_count = 0
    youtube_off_count = 0
    tiktoc_on_count = 0
    tiktoc_off_count = 0
    y_status=[]
    t_status=[]
    for i in urls2:
        if "youtube.com/watch?v=" in str(i):
            y_status.append(i.status)
            if i.status=='ON':
                youtube_on_count+=1
            else:
                youtube_off_count+=1
        if "/www.tiktok.com/" in str(i):
            
            t_status.append(i.status)
            if i.status=='ON':
                tiktoc_on_count+=1
            else:
                tiktoc_off_count+=1

    print(tiktoc_off_count)
    context = {
        'total_on_count': total_on_count,
        'total_off_count': total_off_count,
        'fb_total_links':len(urls),
        'youtube_total_links':len(y_status),
        'tiktoc_total_links':len(t_status),
        'fb_on_count': fb_on_count,
        'fb_off_count': fb_off_count,
        'youtube_on_count': youtube_on_count,
        'youtube_off_count': youtube_off_count,
        'tiktoc_on_count': tiktoc_on_count,
        'tiktoc_off_count': tiktoc_off_count,
        'total': total,
        'profile':profile,
        'groups':groups,
        'pages':pages

    }

    return render(request, 'dashboard.html', context)
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

def update_status(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        status = request.POST.get('status')
        print(url)
        print(status)

        # Perform the necessary logic to update the status in your database
        # Replace the following code with your actual implementation
        try:
            report = get_object_or_404(facebookURL, url=url)
            report.status = status
            report.save()
            return JsonResponse({'success': True})

        except facebookURL.DoesNotExist:
            return JsonResponse({'success': False})

    return JsonResponse({'success': False})
def update_status2(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        new_status = request.POST.get('status')

        # Perform the necessary logic to update the status in the backend
        # Replace the following lines with your actual implementation
        # For example, update the status in the database
        # or update a corresponding model object
        
        # Assuming you have a Report model
        report=get_object_or_404(SocialMediaURL, hisposturl=url)
        report = SocialMediaURL.objects.get(hisposturl=url)
        report.status = new_status
        report.save()

        # Return a JSON response indicating the success of the update
        response = {
            'status': 'success',
            'message': 'Status updated successfully.',
        }
        return JsonResponse(response)

    # Handle cases other than POST requests
    response = {
        'status': 'error',
        'message': 'Invalid request method.',
    }
    return JsonResponse(response)
 








