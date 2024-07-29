'''
Pull down the imbd_movies dataset here and save to /data as imdb_movies_2000to2022.prolific.json
You will run this project from main.py, so need to set things up accordingly
'''

import json
import requests
import os
import analysis_network_centrality
import analysis_similar_actors_genre

# Ingest and save the imbd_movies dataset

def download_data(url, save_path):
    
    response = requests.get(url)

    with open(save_path, 'w') as file:
        file.write(response.text)
    print(f"Dataset downloaded and saved to {save_path}.")

# Call functions / instanciate objects from the two analysis .py files
def main():
    
    url = 'https://raw.githubusercontent.com/cbuntain/umd.inst414/main/data/imdb_movies_2000to2022.prolific.json'
    save_path = '/Users/taliyahmonae/Desktop/School/INST414/problem-set-1/data'

feature_matrix = create_genre_feature_matrix(filepath)

query_actor_id = 'nm0005517'
query_actor_name = 'Gabrielle Union'

if __name__ == "__main__":
    main()
    