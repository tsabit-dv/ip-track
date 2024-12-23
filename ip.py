import os
import urllib.request
import json

# For your own IP Coding
url = "http://ip-api.com/json/"
load1 = urllib.request.urlopen(url)
read1 = load1.read()
result1 = json.loads(read1)
os.system('clear')
print(r'''
\033[1;33m
        $$$$$$\ $$$$$$$\        $$$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\  
        \_$$  _|$$  __$$\       \__$$  __|$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |$$  _____|$$  __$$\ 
          $$ |  $$ |  $$ |         $$ |   $$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / $$ |      $$ |  $$ |
          $$ |  $$$$$$$  |         $$ |   $$$$$$$  |$$$$$$$$ |$$ |      $$$$$  /  $$$$$\    $$$$$$$  |
          $$ |  $$  ____/\033[1;32m          $$ |   $$  __$$< $$  __$$ |$$ |      $$  $$<   $$  __|   $$  __$$< 
          $$ |  $$ |               $$ |   $$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  $$ |      $$ |  $$ |\033[1;31m{v3.0}\033[1;31m
        $$$$$$\ $$ |               $$ |   $$ |  $$ |$$ |  $$ |\$$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ |
        \______|\__|               \__|   \__|  \__|\__|  \__| \______/ \__|  \__|\________|\__|  \__|\033[1;32m
\033[1;33m
''')
print("\033[1;33m==================================================================================================\033[1;33m")
print("\033[1;32mAuthor           : Mahfuzur Rahman\033[1;32m")
print("\033[1;32Github          : https://github.com/anonymousproo\033[1;32m")
print("\033[1;32mYouTube          : https://www.youtube.com/anonymouspro1            {IP Tracker v3.0}\033[1;32m")
print("\033[1;32mFacebook         : https://m.facebook.com/anonymousproo1\033[1;32m")
print("\033[1;32mCoded by         : ANONYMOUS PRO YTB\033[1;32m")
print("\033[1;33m==================================================================================================\033[1;33m")
print("\n\033[1;33mYour IP: \033[1;33m" + result1['query'])
print("\033[1;32mIf You Do Not Want To Track Type Exit\033[1;32m\n")

while True:
    ip = input("\033[1;36mEnter Your Target IP: \033[1;36m")

    if ip.lower() == 'exit':
        break
    else:
        # IP Coding
        api = "http://api.ipstack.com/"
        load = urllib.request.urlopen(api + ip + '?access_key=fd0c1eae3c2d27ee676af0db2b864b0e')
        read = load.read()
        result = json.loads(read)

        # ip-api
        url = "http://ip-api.com/json/"
        load1 = urllib.request.urlopen(url + ip)
        read1 = load1.read()
        result1 = json.loads(read1)

        if result1['status'] == 'success':
            # Latitude and Longitude
            lat = "{:.4f}".format(result['latitude'])
            long = "{:.4f}".format(result['longitude'])

            # More info
            more = json.dumps(result['location'])

            # Printing information
            print(f"\n\033[1;33mAll The Information Of IP Is Here \033[1;33m[{ip}] :\n")
            print(f"\033[1;33mIP: \033[1;33m{result['ip']}")
            print(f"\033[1;32mIP Type: \033[1;32m{result['type']}")
            print(f"\033[1;34mContinent Name: \033[1;34m{result['continent_name']}")
            print(f"\033[1;34mContinent Code: \033[1;34m{result['continent_code']}")
            print(f"\033[1;33mCountry: \033[1;33m{result['country_name']}")
            print(f"\033[1;33mCountry Code: \033[1;33m{result1['countryCode']}")
            print(f"\033[1;32mRegion Name: \033[1;32m{result['region_name']}")
            print(f"\033[1;32mRegion Code: \033[1;32m{result['region_code']}")
            print(f"\033[1;36mCity: \033[1;36m{result['city']}")
            print(f"\033[1;36mZip: \033[1;36m{result['zip']}")
            print(f"\033[1;33mTimeZone: \033[1;33m{result1['timezone']}")
            print(f"\033[1;33mISP: \033[1;33m{result1['isp']}")
            print("Do you want to find the exact location with Google Maps?")
            print("Then search the Google Map using the Latitude or Longitude number")
            print(f"\033[1;36mLatitude: \033[1;36m{lat}")
            print(f"\033[1;36mLongitude: \033[1;36m{long}")
            print(f"\033[1;33mMore Information Of IP \033[1;33m:\n{more}\n\n")
        else:
            print(f"\n\033[1;31mSorry, IP [{ip}] not found. Please try again.\033[1;31m\n")
