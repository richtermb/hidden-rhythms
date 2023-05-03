import numpy as np

class Recommender(object):
  def __init__(self, n_friends, n_songs):
    self.n_friends = n_friends
    self.n_songs = n_songs
    self.friend_count = 0


  def add_friend(song_prefs):
    # song_prefs is an np.array of the vectorized songs
    assert(self.n_songs == np.shape(song_prefs)[0])
    # generate knns, etc.
    self.friend_count += 1

  def generate_shared_dp_playlist():
    assert(self.friend_count == self.n_friends)
    # run alg to generate np array of vectorized songs fufilling DP requirements