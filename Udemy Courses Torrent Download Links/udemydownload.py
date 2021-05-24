from bs4 import BeautifulSoup
import requests
import pyperclip


course_name = input('Enter the course name : ').replace(':','').replace('#','')
torrentlinks = []
torrent_url   = 'https://meshcron.com/files/Udemy%20-%20'+ course_name.replace(' ','%20') +'.torrent'
torrent_url_2 = 'https://meshcron.com/files/FreeCourseSite.com-Udemy%20-%20'+ course_name.replace(' ','%20') +'.torrent'
torrentlinks.append(torrent_url)
torrentlinks.append(torrent_url_2)

for i, url in enumerate(torrentlinks):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'lxml')
    print('Url {} : {}'.format(i+1,url))
    if(html_text[0]!='<'):
        pyperclip.copy(url)
        print('Copied Url {}'.format(i+1))
        print('The link is copied so just paste the link in the torrent downloader and u are good to go!')
        break
    else:
        print('There is no such website found in the repository!')
