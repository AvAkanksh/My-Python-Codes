import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve
from subprocess import run

# ===========================================================
# This function will just check if the file is downloadable
# ===========================================================

def is_downloadable(url):
    """
    Does the url contain a downloadable resource
    """
    h = requests.head(url, allow_redirects=True)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


url = 'http://www.cs.toronto.edu/~hinton/coursera_lectures.html'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text,'lxml')
all_a = soup.find_all('a')
url_prefix = 'http://www.cs.toronto.edu/~hinton/'
video_links = []
names = []

for a in all_a:
    link = url_prefix+a.get('href')
    video_links.append(link)
    name = link.split('/')[-1]
    names.append(name)
    # print('Link {} :'.format(link),is_downloadable(link))

# Checking if the directory is present, if its not present it will be created

directory = 'Video_Lectures'
if not os.path.exists(directory):
            os.makedirs(directory)
                  

# =====================================================================
#                          Method 1
# =====================================================================

# for i,video in enumerate(video_links):
#     if(is_downloadable(video)): 
#         r = requests.get(video,stream=True)
#         print('Started Downloading {} video'.format(names[i]))
#         with open(directory+'/'+names[i],mode = 'wb') as file:
#             for chunk in r.iter_content(chunk_size=1024*1024):
#                 if chunk:
#                     file.write(chunk)
#             print('Downloaded {} video! '.format(names[i]))

# =====================================================================
#                          Method 2
# =====================================================================

# for i,video in enumerate(video_links):
#     if(is_downloadable(video)):   
#         print('Started Downloading {} video'.format(names[i]))
#         urlretrieve(video,directory+'/'+names[i])
#         print('Downloaded {} video! '.format(names[i]))
#         print('='*80)


# =====================================================================
#                Method 3 (Most Efficient Method)
# =====================================================================
for i,video in enumerate(video_links):
    if(is_downloadable(video)):    
        final_command = 'axel -n 5 -o {} {}'.format(directory+'/'+names[i],video)
        run(final_command,shell=True)
        print('\n'*2+'='*80+'\nCompleted Downloading {}\n'.format(names[i])+'='*80+'\n'*2)


