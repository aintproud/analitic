import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set()
# 3. Загрузите данные в формате pandas DataFrame:

smp500 = pd.read_csv("^spx_d (1).csv")
bitcoin = pd.read_excel("GDAX.BTC-USD_790301_230316.xlsx")
bitcoin.drop(range(362),inplace=True)
bitcoin.drop(range(2915, 2990),inplace=True)
bitcoin = bitcoin.iloc[:,[2,7]]
bitcoin.columns = ['Date', 'Close']
bitcoin['Date'] = bitcoin['Date'].map(lambda x:str(x)[0:4]+'-'+str(x)[4:6]+'-'+str(x)[6:8]) 
smp500 = smp500[['Date','Close']]

print(smp500)
print(bitcoin)

smp500.dropna(inplace=True)
bitcoin.dropna(inplace=True)

smp500.head()
bitcoin.head()

sns.displot(smp500["Close"])
sns.displot(bitcoin["Close"])

sns.displot(smp500["Close"], kde = False,
            color= "limegreen")
sns.displot(bitcoin["Close"], kde = False,
            color= "limegreen")
# 4. Используйте функции seaborn для визуализации данных, например:
sns.displot(smp500["Close"], kde = False,
            color= "limegreen",
            bins = 10,
            hist_kws = {"alpha": 0.75,
                        "edgecolor" : "black"})
sns.displot(bitcoin["Close"], kde = False,
            color= "limegreen",
            bins = 10,
            hist_kws = {"alpha": 0.75,
                        "edgecolor" : "black"})

sns.displot(smp500["Close"], kde = False,
            color= "limegreen",
            bins = 10,
            hist_kws = {"alpha": 0.75,
                        "edgecolor" : "black"},
            kde_kws = {"color":"red"})
sns.displot(bitcoin["Close"], kde = False,
            color= "limegreen",
            bins = 10,
            hist_kws = {"alpha": 0.75,
                        "edgecolor" : "black"},
            kde_kws = {"color":"red"})


plt.title('My Plot')
plt.xlabel('Close')
plt.ylabel('Y Label')

plt.vlines(x = smp500["Close"].mean(), ymin=0, ymax=80, color = "red", linestyles="dotted")
plt.vlines(x = bitcoin["Close"].mean(), ymin=0, ymax=80, color = "red", linestyles="dotted")

plt.vlines(x = smp500["Close"].mean(), ymin=0, ymax=500, color = "red", linestyles="dotted")
plt.vlines(x = bitcoin["Close"].mean(), ymin=0, ymax=500, color = "red", linestyles="dotted")

sns.kdeplot(smp500["Close"], shade= True)

plt.xlabel('Close')
plt.ylabel('Y Label')
plt.title('Close of responsents')

sns.kdeplot(bitcoin["Close"], shade= True)

plt.xlabel('Close')
plt.ylabel('Y Label')
plt.title('Close of responsents')


sns.displot(smp500["Close"], hist = False, rug= True)
plt.xlabel('Close')
plt.ylabel('Y Label')
plt.title('Close of responsents')


sns.displot(bitcoin["Close"], hist = False, rug= True)
plt.xlabel('Close')
plt.ylabel('Y Label')
plt.title('Close of responsents')


g = sns.FacetGrid(smp500, row = "Open", col = "Date", margin_titles = True)
g.map(plt.hist, "Close", color="streelblue")
g1 = sns.FacetGrid(bitcoin, row = "Open", col = "Date", margin_titles = True)
g1.map(plt.hist, 'Close', color="streelblue")

# cтолбиклвая диаграма
tab = bitcoin["TIME"].value_counts()
tab1 = bitcoin["TIME"].value_counts()

sns.barplot(x=tab1.index, y=tab1.values)
plt.xticks(rotation=90)
plt.xlabel('Time')
plt.ylabel('Count')
plt.title('Number of Bitcoin trades per hour')

# столбиковая диаграмма
df = pd.read_csv('bitcoin_trades.csv')
# Преобразование столбца с датой-временем в тип datetime и установка его в качестве индекса
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
# Группировка по часам и подсчет количества сделок в каждом часе
tab1 = df.resample('H').size()
# Сортировка индекса по возрастанию
tab1 = tab1.sort_index()
# Построение столбиковой диаграммы
sns.barplot(x=tab1.index, y=tab1.values)
plt.xticks(rotation=90)
plt.xlabel('Time')
plt.ylabel('Count')
plt.title('Number of Bitcoin trades per hour')
plt.show()




