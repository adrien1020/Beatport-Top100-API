from beatport_top100 import BeatPortTop100
import requests
import json

HEARDER = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


def load_json(source):
    """load sources_data.json file"""
    with open(source, 'r') as json_file:
        data = json.load(json_file)

        for url in data['source']:
            beatPortTop100 = BeatPortTop100()
            beatPortTop100.get_list_top_100(url=url['website'], header=HEARDER)
            beatPortTop100.make_top_100_dict()

            response = requests.get(url=url['api'])

            if not response.json():
                print("POST")
                print(url['api'])
                beatPortTop100.post_top_100_by_pk(api_url=url['api'])
            else:
                print("PUT")
                print(url['api'])
                beatPortTop100.put_top_100_by_pk(api_url=url['api'])


if __name__ == "__main__":
    load_json(source='sources_data.json')
