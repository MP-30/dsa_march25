import time 
import threading
from helpers import dosomething, Dosomething
from number import numberPrinter
from imageDownloader import ImageDownloaderByUrl


start = time.perf_counter()

def print_ans():
    print('abs')


if __name__ == '__main__':

    urls = ['https://imgs.search.brave.com/G7D2MAwaV5uXomFZEyCqHGmWbajQ95kfYZpyYVxS7Oc/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9pMC53/cC5jb20vcGljanVt/Ym8uY29tL3dwLWNv/bnRlbnQvdXBsb2Fk/cy90aWdlci1leWVz/LWxvb2tpbmctZnJv/bS10aGUtYnVzaGVz/LWZyZWUtaW1hZ2Uu/anBlZz9oPTgwMCZx/dWFsaXR5PTgw'
    ,'https://imgs.search.brave.com/2Y0LgJOv7fd39ZrHzkFaX0CKdrZW1N1nkbC5Dy94U1s/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9pMC53/cC5jb20vcGljanVt/Ym8uY29tL3dwLWNv/bnRlbnQvdXBsb2Fk/cy9waW5rLWZsYW1p/bmdvLWZyZWUtcGhv/dG8uanBlZz9oPTgw/MCZxdWFsaXR5PTgw'
    
    , 'https://imgs.search.brave.com/NrlZu-RbjGqH--zt6qRLLqua63hgRZuuRQziGS5ua1U/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9waXhs/ci5jb20vaW1hZ2Vz/L2luZGV4L2FpLWlt/YWdlLWdlbmVyYXRv/ci1vbmUud2VicA'
    
    , 'https://imgs.search.brave.com/qJFCUICSuhAGFLNBvcENRsxrBEOBE46zgHMhWf4wDnA/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9waXhs/ci5jb20vaW1hZ2Vz/L2luZGV4L3Byb2R1/Y3QtaW1hZ2Utb25l/LndlYnA'
    
    , 'https://imgs.search.brave.com/WrZ82GcGEodgcTbdV4dmZ6QLp7ZbrOZ8WfR3rObHQnI/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cGl4YWJheS5jb20v/cGhvdG8vMjAyMC8w/OC8yNC8yMS80NC9t/YW4tNTUxNTE1MF82/NDAuanBn'
    ]


    threads = []
    for url in urls:
        image_downloader = ImageDownloaderByUrl(url)
        # image_downloader.run()
        image_downloader.start()
        threads.append(image_downloader)
    
    for thread in threads:
        thread.join()

    # threads = []
    # for i in range(1,101):
    #     thread = numberPrinter(i)
    #     thread.start()
    #     threads.append(thread)
        
    # for j in threads:
    #     j.join()

    # t1 = Dosomething('aditya')
    # t1.start()
    
    # t2 = Dosomething('singh')
    # t2.start()
    
    # t1.join()
    # t1.join()
    
    # names = ['aditya', 'vivek', 'rahul', 'vinayak']
    # threads = []
    # for name in names:
    #     thread = threading.Thread(target=dosomething, args=[name])
    #     # thread.start()
    #     thread.run()
    #     threads.append(thread)
            
    
    # for thread in threads:
        # thread.join()
    # print(f"main thread is {threading.current_thread().name} and id is {threading.get_ident()}")    
    # t1 = threading.Thread(target=dosomething, args=['aditya', '43', 'gender'])
    # t2 = threading.Thread(target=dosomething, args=['aditya singh', '43', 'gender'])
    # t3 = threading.Thread(target=dosomething, args=['aditya pratab', '43', 'gender'])
    # t4 = threading.Thread(target=dosomething, args=['aditya bhadauriya', '43', 'gender'])
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()   
    
    
    finish = time.perf_counter()
    print(abs(start-finish))