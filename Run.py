__Author__    = 'DieckyAwsm'
__Whatsapp__  = '081287467015'
__Facebook__  = 'https://www.facebook.com/DieckyAwsm'

import os,sys,time,random,re,json,datetime,shutil,urllib
try:import instaloader
except ImportError:os.system('pip install instaloader')

# ------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"

def Banner():
	print(f"""{K}
···························································
: ___           _        _                    _           :
:|_ _|_ __  ___| |_ __ _| |    ___   __ _  __| | ___ _ __ :
: | || '_ \/ __| __/ _` | |   / _ \ / _` |/ _` |/ _ \ '__|:
: | || | | \__ \ || (_| | |__| (_) | (_| | (_| |  __/ |   :
:|___|_| |_|___/\__\__,_|_____\___/ \__,_|\__,_|\___|_|   :
···························································
""")

    
os.system('clear')
Banner()
print(f"{B} Reel Videos Instagram Downloader by DieckyAwsm")
print(f"{B} Tutorial? Gaada, Tinggal Paste Username Target Doang")
print(f"{P}|=========================================================|\n")

username = input(" Masukkan Username Instagram : ")

def reel_download(username):
    X = instaloader.Instaloader(download_pictures=True,download_videos=True,download_video_thumbnails=False,download_geotags=False,download_comments=False,save_metadata=False)
    try:
        id = instaloader.Profile.from_username(X.context,username)
        for post in id.get_posts():
            if post.typename == "GraphVideo":
               X.download_post(post, target=f"{username}_reel")
               print(f" •• Downloaded: {post.shortcode}")
    
    except instaloader.exceptions.InstaloaderException as e:
    	print(f"Error: {e}")
    except:pass
    exit()
        
if __name__ == "__main__":
    reel_download(username)               