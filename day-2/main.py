import pandas as pd


def print_titles():
    titles = pd.read_csv(
        'https://raw.githubusercontent.com/prasertcbs/basic-dataset/master/netflix_titles.csv')
    print(titles.head())


def main():
    print_titles()

    with open('system.log', 'r') as file:
        for row in file:
            print(f'log: {row}')


if __name__ == '__main__':
    main()
