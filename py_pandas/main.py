import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        df_temp = pd.read_csv(symbol_to_path(symbol),
                              index_col="Date",
                              parse_dates=True,
                              usecols=['Date', 'Adj Close'],
                              na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)

    df = df.dropna()
    return df


def normalize_data(df):
    return df/df.ix[0, :]


def plot_data(df, title="Stock prices"):
    df.plot()
    plt.title(title)
    plt.show()


def plot_selected(df, columns, start_index, end_index):
    plot_data(df.ix[start_index:end_index, columns], title='selected stocks')


def get_max_close(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol))
    return df['Close'].max()


def get_mean_volume(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol))
    return df['Volume'].mean()


def test_run():
    # for symbol in ['AAPL', 'IBM']:
    #     print("max close")
    #     print("%s, %d" % (symbol, get_max_close(symbol)))
    #     print("mean volume")
    #     print("%s, %d" % (symbol, get_mean_volume(symbol)))
    # df = pd.read_csv('data/AAPL.csv')
    # # print(df['Adj Close'])
    # df[['Close','Adj Close']].plot()
    # plt.show()

    # start_date = '2017-01-10'
    # end_date = '2018-01-10'
    # dates = pd.date_range(start_date, end_date)
    # symbols = ['IBM', 'AAPL']
    # df1 = get_data(symbols, dates)
    # # print(df1[['SPY', 'IBM']])
    # # print(df1.ix['2018-01-22':'2018-01-24', ['SPY', 'IBM']])
    # plot_data(normalize_data(df1), title='aaaa')


    """numpy array"""
    # print(np.array([(2, 3, 4), (5, 6, 7)]))

    # array of 1s, integer
    # print(np.ones((5,4), dtype=np.int))

    #Random integers
    print(np.random.randint(0, 10, size=5))
    print(np.random.randint(0, 10, size=(2, 3)))

def test_run_numpy():
    np.random.seed(693)
    a = np.random.randint(0, 10, size=(5, 4))
    print(a)
    print("Sum of each column:", a.sum(axis=0))
    print("sum of each row:", a.sum(axis=1))

if __name__ == "__main__":
    # test_run()
    test_run_numpy()