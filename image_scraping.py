import os
import requests

# Given an image url download the image to a local folder
def download_image(url, local_folder_path): 

    if not os.path.exists(local_folder_path): 
        os.makedirs(local_folder_path)

    response = requests.get(url)

    if response.status_code == 200: 
        image_name = url.split("/")[-1]
        file_name = os.path.join(local_folder_path, image_name) #creating the image file name 

        with open (file_name, 'wb') as file: 
            file.write(response.content)

        print("Downloaded:" + url.split("/")[-1])

download_image("https://picsum.photos/id/237/200/300","/Users/ishikanimmagadda/Desktop/one more time/Image-Scraping/images")