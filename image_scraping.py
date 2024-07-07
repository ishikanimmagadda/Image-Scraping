import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Given an image url download the image to a local folder
def download_image(image_url, local_folder_path): 

    if not os.path.exists(local_folder_path): 
        os.makedirs(local_folder_path)

    response = requests.get(image_url)

    if response.status_code == 200: 
        image_name = image_url.split("/")[-1]
        file_name = os.path.join(local_folder_path, image_name) #creating the image file name 

        with open (file_name, 'wb') as file: 
            file.write(response.content)

        print("Downloaded:" + image_url.split("/")[-1])
    
    else: 
        print("Error Downloading")

#download_image("https://picsum.photos/id/237/200/300","/Users/ishikanimmagadda/Desktop/one more time/Image-Scraping/images")

# Scrape a webpage and return a list of all the image urls

def get_image_urls(web_url):
    image_urls = [] 

    response = requests.get(web_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    for image in soup.find_all('img'):
        image_url = image.get('src') #src is the url part 
        #download_image(image_url, "/Users/ishikanimmagadda/Desktop/one more time/Image-Scraping/images")
        print (image_url)
        if image_url != None: 
            full_image_url = urljoin(web_url, image_url)
            image_urls.append(full_image_url)

    return image_urls

get_image_urls("https://www.amazon.in/s?bbn=1389401031&rh=n%3A1389401031%2Cp_36%3A1318505031&dc&qid=1622460176&rnid=1318502031&ref=lp_1389401031_nr_p_36_2")

# scraping urls & saving image to local file 
urls = get_image_urls("https://www.amazon.in/s?bbn=1389401031&rh=n%3A1389401031%2Cp_36%3A1318505031&dc&qid=1622460176&rnid=1318502031&ref=lp_1389401031_nr_p_36_2")

for url in urls: 
    download_image(url, "/Users/ishikanimmagadda/Desktop/one more time/Image-Scraping/images")
