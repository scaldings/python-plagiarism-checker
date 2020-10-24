from googlesearch import search
from bs4 import BeautifulSoup
import requests


def plagiarism_check(qry: str):
    x_searches = []
    for x in search(query=qry, num=10, stop=10, pause=2.0):
        x_searches.append(x)

    for x in range(0, len(x_searches) - 1):
        url = x_searches[x]
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        all_p = soup.find_all('p')

        for y in range(0, len(all_p)):
            if qry in str(all_p[y]):
                return url


def main():
    query = str(input('Enter the text you want to check: '))
    link = plagiarism_check(query)

    if link is None:
        print('No link has been found.')
    else:
        print(f'A similarity has been found: {link}')


if __name__ == '__main__':
    main()
