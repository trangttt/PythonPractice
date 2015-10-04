from urllib import request
import bs4

def easter(year):
    opener = request.build_opener()
    opener.addheaders = [('User-agent', 'Chrome/41.0.2228.0')]
    response = opener.open('http://www.wheniseastersunday.com/year/' + str(year) + '/')
    parsed_content = bs4.BeautifulSoup(response.read())
    print(parsed_content.find_all('p'))
    return parsed_content.select('.easterdate')[0].get_text()

if __name__ == "__main__":
    print(easter(2030))

