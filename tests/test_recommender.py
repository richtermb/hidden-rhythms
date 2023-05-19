import numpy as np
import os

from hidden_rhythms import recommender, dataset

if __name__ == "__main__":
  # dims = 10
  group_total = 5
  songs_per_friend = 10

  print("Initializing recommender...")
  recommender = recommender.Recommender(group_total, songs_per_friend)

  print("Loading dataset...")
  dirname = os.path.dirname(__file__)
  zip_path = os.path.join(dirname, "../hidden_rhythms/tracks.csv.zip")
  df = dataset.load_tracks_dataset(zip_path)
  recommender.load_tracks_dataframe(df)

  print("Adding member preferences...")
  for i in range(group_total):
    friend_songs = dataset.choose_random_songs(df, songs_per_friend)
    print("Adding friend", i, friend_songs)
    friend_index = recommender.add([dataset.vectorize(row) for _, row in friend_songs.iterrows()])

  print("Generating shared playlist...")

  group_means = recommender.compute_group_mean_vec()
  print("Group means:", group_means)

  group_variances = recommender.compute_group_variance_vec()
  print("Group variances:", group_variances)

  sensitivity = recommender.global_variance_sensitivity()
  print("Sensitivities:", sensitivity)

  # print("Means", recommender.compute_means())

  
