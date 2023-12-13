import requests

# Pexels API key
PEXELS_API_KEY = 'SlWiHtu8IDZVciAphF42FDRl8Nr1zZqxgG6XCqpWRdl86k8zZDmpWbES'

def fetch_images(query, per_page=5):
    url = f'https://api.pexels.com/v1/search'
    headers = {'Authorization': PEXELS_API_KEY}
    params = {'query': query, 'per_page': per_page}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json().get('photos', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching images: {e}")
        return []

def generate_html(images):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            #collage-container {
                display: flex;
                flex-wrap: wrap;
                gap: 10px;
                justify-content: center;
            }

            .collage-image {
                width: 150px;
                height: 150px;
                object-fit: cover;
                border-radius: 8px;
            }
        </style>
        <title>Image Collage</title>
    </head>
    <body>
        <div id="collage-container">
    """

    for image_info in images:
        image_url = image_info.get('src', {}).get('medium', '')
        html_content += f'<img src="{image_url}" alt="Pexels Image" class="collage-image">'

    html_content += """
        </div>
    </body>
    </html>
    """

    with open('collage.html', 'w') as html_file:
        html_file.write(html_content)

    print("Collage HTML file generated: collage.html")

if __name__ == "__main__":
    query = input("Enter the search query for images: ").strip()
    
    if not query:
        print("Invalid query. Please enter a non-empty search query.")
    else:
        num_images = 8
        images = fetch_images(query, per_page=num_images)

        if images:
            generate_html(images)
        else:
            print("No images found.")
