import urllib.request

def download_file():
    url = input("Enter the URL of the PDF you want to download : ")
    file_location = input('Enter the path of the location to download (press enter for default "Downloaded-PDFS/"): ')
    if file_location == '':
        file_location = 'Downloaded-PDFS/' # Default directory
    filename = url.split('/')[-1]
    response = urllib.request.urlopen(url)    
    file = open(file_location+filename , 'wb')
    file.write(response.read())
    file.close()
    print("The pdf is Downloaded!")
 
download_file()