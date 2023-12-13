import requests
from PIL import Image
from io import BytesIO

# Pexels API key
PEXELS_API_KEY = 'SlWiHtu8IDZVciAphF42FDRl8Nr1zZqxgG6XCqpWRdl86k8zZDmpWbES'

# Function to fetch images from Pexels API
def fetch_images(query, per_page=5):
    url = f'https://api.pexels.com/v1/search?query={query}&per_page={num_images}'
    headers = {'Authorization': PEXELS_API_KEY}
    params = {'query': query, 'per_page': per_page}
    response = requests.get(url, headers=headers, params=params)
   

    if response.status_code == 200:
        return response.json().get('photos', [])
    else:
        print(f"Error fetching images: {response.status_code}")
        return []

# Function to create a collage from images
def create_collage(images, collage_size=(1600, 800), image_size=(400, 400)):
    collage = Image.new('RGB', collage_size)

    for idx, image_info in enumerate(images):
        image_url = image_info.get('src', {}).get('medium', '')
        response = requests.get(image_url)
        
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img = img.resize(image_size)
            collage.paste(img, ((idx % 4) * image_size[0], (idx // 4) * image_size[1]))

    collage.show()

if __name__ == "__main__":
    query = input("Enter the search query for images: ")
    num_images = 2
    images = fetch_images(query, per_page=8)
    print(images)

    if images:
        create_collage(images)
    else:
        print("No images found.")
