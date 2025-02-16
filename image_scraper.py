import bs4
import requests
import os

NUM_IMAGE_SCRAPE = 30
images_dir = 'images4'
def scrape_and_download_images(image_description, image_class): 
    # Get the image search results page
    res = requests.get('https://www.google.com/search?q=' #+ 'unattended ' 
                       + image_description + 
                       #'without a person' + 
                       '&source=lnms&tbm=isch')
    res.raise_for_status()

    # Parse the page
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find all the image elements
    image_elements = soup.select('img')

    if not os.path.exists(f'./{images_dir}/{image_class}'): 
        os.makedirs(f'./{images_dir}/{image_class}')

    count = 0
    cur_num_images = len(os.listdir(f'./{images_dir}/{image_class}'))
    # Download the images
    for i, image_element in enumerate(image_elements):
        if count > NUM_IMAGE_SCRAPE: 
            break
        image_url = image_element.get('src')
        if image_url.startswith('http'):
            image_res = requests.get(image_url)
            image_res.raise_for_status()
            with open(f'./{images_dir}/{image_class}/image_' + str(i+cur_num_images) + '.jpg', 'wb') as image_file:
                for chunk in image_res.iter_content(100000):
                    image_file.write(chunk)
            count += 1

#scrape_and_download_images('backpacks at airport', 'backpacks')
#scrape_and_download_images('backpacks at school', 'backpacks')
#scrape_and_download_images('backpacks white background', 'backpacks')
#scrape_and_download_images('backpacks on bench', 'backpacks')
#scrape_and_download_images('backpacks at restaraunt', 'backpacks')
#scrape_and_download_images('wallets in restaraunt seat', 'wallets')
#scrape_and_download_images('wallets at cash register counter', 'wallets')
#scrape_and_download_images('smartphones on restaraunt seats', 'phones')
#scrape_and_download_images('baggage unattended at airport', 'baggage')
#scrape_and_download_images('baggage no background', 'baggage')
#scrape_and_download_images('smartphones on a bench', 'phones')
#scrape_and_download_images('purse on a bench', 'purse')
#scrape_and_download_images('purse no background', 'purse')
#scrape_and_download_images('purse on a restaraunt seat', 'purse')
#scrape_and_download_images('water bottle no background', 'water bottle')
scrape_and_download_images('phones white background', 'phones')
scrape_and_download_images('phones no background', 'phones')
#scrape_and_download_images('laptop on a bench alone', 'laptop')
#scrape_and_download_images('water bottle on a desk with no hands or person', 'water bottle')
#scrape_and_download_images('phone charger on a bench with no person', 'charger')  
#scrape_and_download_images('laptop charger on a bench with no person', 'charger')  