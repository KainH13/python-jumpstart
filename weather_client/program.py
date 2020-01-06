import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport',
                                        'cond, temp, scale, loc')

def main():

    print_the_header()

    state = input('What US state would you like to search? ***must be in initial format, eg: CA, HI, etc.*** ')
    code = input("What zipcode within {} do you want the weather for? ").format(state)

    html = get_html_from_web(state, code)
    
    report = get_weather_from_html(html)
    
    print('The temp in {} is {} {} and {}'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
        
    ))
    # display for the forecast


def print_the_header():
    print('---------------------------------------')
    print('             WEATHER APP')
    print('---------------------------------------')
    print()


def get_html_from_web(state, zipcode):
    url = 'http://www.wunderground.com/weather/us/{}/{}'.format(state, zipcode)
    print(url)
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:250])

    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='city-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='current-temp').find(class_='wu-value').get_text()
    scale = soup.find(class_='current-temp').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state_from_location(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    # print(loc)
    # print(condition)
    # print(temp, scale)

    # return condition, temp, scale, loc
    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report

def find_city_and_state_from_location(loc : str):
    parts = loc.split(' ')
    parts = parts[:3]

    return ' '.join(parts)


def cleanup_text(text : str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()