import numpy as np

class Recommender(object):
  def __init__(self, n_friends, songs_per_friend):
    self.n_friends = n_friends
    self.songs_per_friend = songs_per_friend
    self.friend_count = 0
    self.songs = []

  def add(self, song_prefs):
    # song_prefs is an np.array of the vectorized songs
    assert(self.songs_per_friend == np.shape(song_prefs)[0])
    # generate knns, etc.
    for v in song_prefs:
      self.songs.append(v)


    self.friend_count += 1

  def generate_shared_dp_playlist(self):
    assert(self.friend_count == self.n_friends)
    # run alg to generate np array of vectorized songs fufilling DP requirements

  def compute_songs_mean(self):
    a = np.array(self.songs)
    return np.mean(a, axis=0)

  def compute_songs_median(self):
    a = np.array(self.songs)
    median = np.median(a, axis=0)

  def compute_songs_variance(self):
    a = np.array(self.songs)
    return np.var(a, axis=0)

  def corrcoef(self):
    a = np.array(self.songs)
    return np.corrcoef(a, rowvar=False)
