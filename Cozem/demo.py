import pandas as pd

def load_data():
    try: 
        data = pd.read_csv(FILE_PATH)
    except FileNotFoundError:
        data = pd.DataFrame(columns=['Name', 'Vote', 'Day'])
    return data

FILE_PATH = 'Cozem/data11.csv'
data = load_data()
print(data)
