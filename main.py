import datetime
import time
import urllib.request
from termcolor import colored

URL_COVID19_CONFIRM = 'https://usafactsstatic.blob.core.windows.net/public/data/covid-19/covid_confirmed_usafacts.csv'
URL_COVID19_DEATH = 'https://usafactsstatic.blob.core.windows.net/public/data/covid-19/covid_deaths_usafacts.csv'

FN_COVID19_CONFIRM = 'covid_confirmed_usafacts.csv'
FN_COVID19_DEATH = 'covid_deaths_usafacts.csv'

TIME_WAIT = 180 # seconds

today = datetime.datetime.today()
yesterday = today - datetime.timedelta(days=1)

dt = yesterday.strftime('%-m/%-d/%y')
flag_covid = False
flag_death = False


def read_url(url, length=2048):
    ctt = ''
    with urllib.request.urlopen(url) as f:
        ctt = f.read(length)
    return ctt


while True:
    if flag_covid == False:
        covid_data = str(read_url(URL_COVID19_CONFIRM))
    if flag_death == False:
        death_data = str(read_url(URL_COVID19_DEATH))

    # print('* covid_data:', covid_data)
    # print('* death_data:', death_data)

    flag_covid = dt in covid_data
    flag_death = dt in death_data

    if flag_covid:
        rst_covid = colored('UPDATED!', 'white', 'on_green', attrs=['bold'])
    else:
        rst_covid = colored('NOT YET.', 'red')


    if flag_death:
        rst_death = colored('UPDATED!', 'white', 'on_green', attrs=['bold'])
    else:
        rst_death = colored('NOT YET.', 'red')

    now = datetime.datetime.today().strftime('%H:%M:%S')
    print('* %s: covid data of %s %s' % (now, dt, rst_covid))
    print('* %s: death data of %s %s' % (now, dt, rst_death))

    if flag_covid and flag_death:
        break

    time.sleep(TIME_WAIT)

print('* finally, we have both covid and death data!')
