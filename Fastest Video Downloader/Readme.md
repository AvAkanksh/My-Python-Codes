# Fastest Video Downloder using python script

Usually there are 2 methods to download a video using python script 

## Method 1:

```python
import requests

url = 'http://www.something.com/folder/video.mp4'  # this is just a sample url
r = requests.get(url,stream=True)
with open('abc.mp4','wb') as file:
    for chunk in r.iter_content(chunk_size=1024*1024):
        if chunk:
            file.write(chunk)
```
- But using this approach the download rate is very slow

## Method 2:

```python
import requests
from urllib.request import urlretrieve

url = 'http://www.something.com/folder/video.mp4'  # this is just a sample url
urlretrieve(url,'abc.mp4')
```
- Even by this approach the download rate is very slow

## Method 3(My Method):
This is the fastest way to download videos using python script

> Requirements:
> 
> _Run this command in terminal_ 
> - sudo apt install axel

axel is a terminal download manager 

```python
from subprocess import run

url = 'http://www.something.com/folder/video.mp4'
filename = 'abc.mp4'
run('axel -o {} {}'.format(filename,url))
```

This approach is very much easy and very very fast when compared to the other usual methods which are found on internet.

filesize = 50 MB

my internet speed = 30 mbps or 30 Mb/s

|Method|Time taked to download the file|Speed|
|:----:|:-----------------------------:|:---:|
|1|3 mins 50 secs|100kbps|
|2|3 mins 30 secs|120kbps|
|3|25 seconds|2.1MB/s|

note that in my method 3 the speed is 2.1 MBps which is 8*2.1Mbps = 17Mbps

This is because B = Byte , b = bit and 1 Byte = 8 bits

# Note

The attached python file contains the script which has web scrapping and then downloading the video content from the website. You can modify the code accordingly and use it as per your convience.

scrape.py is a script which can download the Gefforey Hinton's Videos Coursera Video lectures which are there on his website.