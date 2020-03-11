import youtube_dl
from django.core.mail import send_mail
from main.celery import app

@app.task
def convert_load(url, email, link):
    options = {
        'format': 'bestaudio/best',
        'outtmpl': 'media/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        result = ydl.extract_info(link)
        filename = result['title']

    download_link = 'http://' + url + '/media/' + filename.replace(" ", "%20") + '.mp3'
    filename = filename + '.mp3'

    send_mail(
        'Download link',
        'You can download file from this link:' + download_link,
        'settings.EMAIL_HOST_USER',
        [email],
        fail_silently=False,)
