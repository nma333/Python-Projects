#importing the module
import pytube

#Importing the YouTube class
from pytube import YouTube

#URL of the video which you have to download.
url="https://www.youtube.com/watch?v=1--qqQrimMA"
#url=str(input("Enter the video link :"))

#Variable to store the video information.
my_video=YouTube(url)

#Fetching the title of the video.
print(my_video.title)

print(my_video.thumbnail_url)

my_video=my_video.streams.get_highest_resolution()

#for stream in my_video.streams:
 #   print(stream)

my_video.download()
