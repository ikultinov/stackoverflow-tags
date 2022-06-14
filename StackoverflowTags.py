import requests


def getting_questions_on_tag():
    url = 'https://api.stackexchange.com/2.3/questions?fromdate=1654905600&todate=1655164800&order=desc&sort=activity&tagged=%22Python%22&site=stackoverflow'
    response = requests.get(url)
    for i in response.json()['items']:
        print(i.get('title'))


if __name__ == '__main__':
    getting_questions_on_tag()
