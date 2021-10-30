import requests
from bs4 import BeautifulSoup
import json


class BeatPortTop100(object):
    def __init__(self):
        self.artist = []
        self.title = []
        self.remixers = []
        self.image = []
        self.label = []
        self.genre = []
        self.release_date = []
        self.json_data = []

    def get_list_top_100(self, url, header):
        """Use webscraping for download different data from beatport website"""
        response = requests.get(url=url, headers=header)
        soup = BeautifulSoup(response.content, 'html.parser')
        list_soup = soup.find_all(class_='bucket-item ec-item track', name='li')
        for i in list_soup:
            self.artist.append(i['data-ec-d1'])
            self.title.append(i['data-ec-name'])

            try:
                self.remixers.append(i['data-ec-d2'])
            except KeyError:
                self.remixers.append('')
            self.label.append(i['data-ec-brand'])
            self.genre.append(i['data-ec-d3'])

        list_img = soup.find_all(class_='buk-track-artwork', name='img')

        for i in list_img:
            split_url = i['data-src'].replace('95x95', '1400x1400')
            self.image.append(split_url)

        list_release_date = soup.find_all(class_='buk-track-released', name='p')
        for i in list_release_date[1:]:
            self.release_date.append(i.text)

    def make_top_100_dict(self):
        """Create a dictionnary and convert to json"""
        for i in range(len(self.artist)):
            top_100_dictionnary = {
                "artist": self.artist[i],
                "title": self.title[i],
                "remixers": self.remixers[i],
                "image": self.image[i],
                "label": self.label[i],
                "genre": self.genre[i],
                "release_date": self.release_date[i]
            }
            self.json_data.append(json.dumps(top_100_dictionnary))

    def post_top_100_by_pk(self, api_url):
        """Post with 'POST' method json data by id if API view is empty"""
        for i in range(len(self.artist)):
            requests.post(url=api_url, data=self.json_data[i])

    def put_top_100_by_pk(self, api_url):
        """Updtate with 'PUT' method json data by id"""
        for i in range(len(self.artist)):
            responses = requests.get(url=api_url + str(i + 1) + '/')

            for response in responses.json():
                """if get = webscraping and video id is not blank"""
                if self.artist[i] == response['artist'] and self.title[i] == response['title'] and \
                        self.remixers[i] == response['remixers'] and response['video_id']:
                    print("Vidéo ID existe à cet index")

                elif self.artist[i] == response['artist'] and self.title[i] == response['title'] and \
                        self.remixers[i] == response['remixers'] and not response['video_id']:
                    print("Video ID n'existe pas à cet index")

                else:
                    print("Changement de rang, mise à jour")
                    requests.put(url=api_url + str(i + 1) + '/', data=self.json_data[i])
