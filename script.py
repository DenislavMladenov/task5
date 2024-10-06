import json
import requests
import sqlite3


def read_config(file_path):
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config


def fetch_data(api_url):
    response = requests.get(api_url)
    return response.json()  


def write_to_db(data, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    
    for item in data:
        cursor.execute("INSERT INTO your_table (column1, column2) VALUES (?, ?)", (item['key1'], item['key2']))
    
    conn.commit()  
    conn.close()   


def main():
    config = read_config('config.json')  
    api_url = config['api_url']           
    db_file = config['db_file']           

    data = fetch_data(api_url)            
    write_to_db(data, db_file)            


if __name__ == "__main__":
    main()