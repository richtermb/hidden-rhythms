import pandas as pd
import numpy as np
import zipfile

def load_tracks_dataset(zipped_tracks_csv_path):
  csv_file_name = 'tracks.csv'

  df = None
  # Open the zip file
  with zipfile.ZipFile(zipped_tracks_csv_path, 'r') as zip_ref:
      # Extract the CSV file to a temporary directory
      with zip_ref.open(csv_file_name) as csv_file:
          # Load the CSV file into a pandas DataFrame
          df = pd.read_csv(csv_file)

  return df

def vectorize(pd_row):
  return np.array([[
    pd_row.danceability,
    pd_row.energy,
    pd_row.key,
    pd_row.loudness,
    pd_row.speechiness,
    pd_row.acousticness,
    pd_row.instrumentalness,
    pd_row.liveness,
    pd_row.valence,
    pd_row.tempo
  ]])

def choose_random_songs(df, n):
  return df.sample(n)