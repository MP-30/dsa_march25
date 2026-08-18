import requests
import uuid
import threading


class ImageDownloaderByUrl(threading.Thread):
    def __init__(self,url):
        self.url = url
        threading.Thread.__init__(self)
        
    def run(self):
        
        print(f'image download start by thread {threading.current_thread().name} and {threading.current_thread().ident}')
        image = requests.get(self.url).content
        image_name = f"images/{str(uuid.uuid4())}.jpg"
        with open(image_name, "wb") as image_file:
            image_file.write(image)
            print('image downloaded')