import os

os.system('pip install you-get')
path = r'C:\Users\zzliv\Desktop'

url_video = 'https://www.youtube.com/watch?v=uMZe8XVVcWs'
os.system('you-get -i '+ url_video )
os.system('you-get --itag=18  -O KFC -o '+ path + ' '+ url_video )

# Download bigger video, you can pause and continue like Xunlei
url_video = 'https://www.bilibili.com/video/av6778814/?from=search&seid=14154322691319558545'
os.system('you-get -o '+ path + ' '+ url_video)