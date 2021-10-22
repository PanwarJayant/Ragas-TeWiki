import pickle
import pandas as pd

# Makes a .pkl file which can be for loading data into the template


def main():
    moviesFile = '50 Ragas - Hindi.csv'
    moviesDF = pd.read_csv(moviesFile)
    moviesDF = moviesDF.fillna('none')
    pickle.dump(moviesDF, open('./123.pkl', 'wb'))


if __name__ == '__main__':
    main()
