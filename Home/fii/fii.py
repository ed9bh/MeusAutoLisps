# %%
from os import chdir, mkdir, listdir
from os.path import isdir
from glob import glob
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
from pandas.plotting import register_matplotlib_converters
from time import sleep

# try:
# from selenium import webdriver
# sleep(1)
# SLNM = True
# print('Selenium Carregado...')
# pass
# except ModuleNotFoundError:
# SLNM = False
# print('Não foi possivel carregar Selenium...')

register_matplotlib_converters()
plt.style.use("seaborn")
# %%
Base_Dir = r'A:\_Projetos\AnotacoesEstudosBackPythonLSP/Home/fii'
folder = 'logFiles'

data_sheet = pd.read_excel(Base_Dir + '/' + 'Lista_FII.xlsx')
chdir(Base_Dir)

if isdir(folder) == False:
    mkdir(folder)
    pass

# %%
# #Web_Search_Link = 'https://www.fundsexplorer.com.br/funds/'
# Rent_XPath = '//*[@id="main-indicators-carousel"]/div/div/div[2]/span[2]'

# %%

for item in data_sheet['Ticker']:
    try:
        ticker = f'{item}11.SA'

        print(f'Começando {ticker}...', end='')
        df = pdr.DataReader(ticker, data_source='yahoo', start='2019-06-01')

        # Media Movel Aritimetica

        df['MMA10'] = df['Adj Close'].rolling(10).mean()
        df['MMA30'] = df['Adj Close'].rolling(30).mean()
        df['MMA60'] = df['Adj Close'].rolling(60).mean()

        # Graficos

        plt.plot(df['Adj Close'], color='Blue', label='Adj Close')
        plt.plot(df['MMA10'], color='Yellow', label='MMA_10')
        plt.plot(df['MMA30'], color='Orange', label='MMA_30')
        plt.plot(df['MMA60'], color='Red', label='MMA_60')

        plt.gcf().autofmt_xdate()
        date_format = mpl_dates.DateFormatter('%b, %d, %Y')
        plt.gca().xaxis.set_major_formatter(date_format)

        plt.legend()

        plt.title(f'Estudo do \"{ticker}\"')

        plt.savefig(folder + '/' + ticker + '.png')

        plt.close()

        # if SLNM is True:
        # browser = webdriver.Chrome(r'A:\chromedriver.exe')
        # pass

        # browser.get(Web_Search_Link + item + '11')

        # sleep(1)

        # #AluguelMes = browser.find_element_by_xpath(Rent_XPath)

        # browser.quit()

        with open(folder + '/Report.txt', 'a+') as ReportFile:
            ReportFile.write(item + '11')
            # ReportFile.write('\t')
            # ReportFile.write(AluguelMes.text)
            ReportFile.write('\t')
            ReportFile.write(str(df['Adj Close'][-1]))
            ReportFile.write('\n')

        print('Finalizado...')

        sleep(30)

        pass
    except Exception as error:
        print(error)
        sleep(10)
        pass
