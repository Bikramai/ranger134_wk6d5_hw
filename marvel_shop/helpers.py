import decimal
import requests 
import requests_cache 
import json 




#setup our api cache location (this is going to make a temporary database storage for our api calls)

# requests_cache.install_cache('image_cache', backend='sqlite')



# here I need to change the api call let me ask to my friend since i donot knoe this part
# def get_image(search):
#     url = "https://google-search72.p.rapidapi.com/imagesearch/"

#     querystring = {"q": search,"gl":"us","lr":"lang_en","num":"10","start":"0"}

#     headers = {
#         "X-RapidAPI-Key": "5bb8b6eab7msh7111c8bf2c05cd2p139b99jsn519fe659662c",
#         "X-RapidAPI-Host": "google-search72.p.rapidapi.com"
#     }

#     response = requests.get(url, headers=headers, params=querystring)

#     data = response.json()
#     # print(data)

#     img_url = ""

#     if 'items' in data.keys():
#            img_url = data['items'][0]['originalImageUrl'] 

#     return img_url



# requests_cache.install_cache('image_cache', backend='sqlite') 

def marvel(search):


    url = "https://marvel-heroic-api-unlock-the-mcu-legendary-characters.p.rapidapi.com/name"

    querystring = {"q": search}

    headers = {
        "X-RapidAPI-Key": "55def16c37mshf2200fdea0b6328p1d9d57jsn0004b8652316",
        "X-RapidAPI-Host": "marvel-heroic-api-unlock-the-mcu-legendary-characters.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()

    img_url = ""

    if 'items' in data.keys():
           img_url = data['items'][0]['originalImageUrl'] 

    return img_url

# from marvel import Marvel

# class Marvel:
#     def __init__(self, name, publisher):
#         self.name = name
#         self.publisher = publisher
#         self.comics = []  # Add a 'comics' attribute to store a list of comics

#     def add_comic(self, comic):
#         self.comics.append(comic)

#     def get_comics(self):
#         return self.comics


# marvel = Marvel(PUBLIC_KEY="39bafc2be0b62e0c8e757b95d8703ad9", 
#                 PRIVATE_KEY="38439925c3c160c9eb712af4acc85532b8f8787c")

# characters = Marvel.characters #this is an object

# all_characters == characters.all()

# print(all_characters)








class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal): #if the object is a decimal we are going to encode it 
                return str(obj)
        return json.JSONEncoder(JSONEncoder, self).default(obj) #if not the JSONEncoder from json class can handle it 
            