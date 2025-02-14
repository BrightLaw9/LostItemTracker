import bs4
import requests
import os

def scrape_and_download_images(image_description): 
    # Get the image search results page
    res = requests.get('https://www.google.com/search?q=' + image_description + '&source=lnms&tbm=isch')
    res.raise_for_status()

    # Parse the page
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find all the image elements
    image_elements = soup.select('img')

    if not os.path.exists('./images'): 
        os.mkdir('./images')

    count = 0
    # Download the images
    for i, image_element in enumerate(image_elements):
        if count > 10: 
            break
        image_url = image_element.get('src')
        if image_url.startswith('http'):
            image_res = requests.get(image_url)
            image_res.raise_for_status()
            with open(f'./images/image_{image_description}' + str(i) + '.jpg', 'wb') as image_file:
                for chunk in image_res.iter_content(100000):
                    image_file.write(chunk)
            count += 1

scrape_and_download_images('backpacks')
scrape_and_download_images('wallets')