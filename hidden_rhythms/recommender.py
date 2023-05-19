import numpy as np

from hidden_rhythms.faiss_utils import FAISSWrapper
from hidden_rhythms.dataset import vectorize

class Recommender(object):
  def __init__(self, group_count, songs_per_member):
    self.group_count = group_count
    self.songs_per_member = songs_per_member
    self.member_count = 0 # current number of members
    self.songs = []
    self.song_db = FAISSWrapper(10) # initialize with 10 dimensions
    
  def load_tracks_dataframe(self, df):
    for i, row in df.iterrows():
      v = vectorize(row)
      self.song_db.add(v)
  
  def knn_track_dataset(self, v, n):
    return self.song_db.search(v, n)
  
  def add_preference_matrix(self, song_prefs):
    # song_prefs is a 2d numpy array of shape (songs_per_member, 10)
    assert(self.songs_per_member == np.shape(song_prefs)[0])
    assert(self.member_count < self.group_count)

    # generate knns, etc.
    for v in song_prefs:
      self.songs.append(v)
    
    member_idx = self.member_count
    self.member_count += 1
    return member_idx

  def global_variance_sensitivity(self):
    assert(self.member_count == self.group_count)

    differences = []
    reference_group_variance_vec = self.compute_group_variance_vec()

    # for each member, compute the difference in group variance for 
    # the member preference dataset with and without that member

    for i in range(self.group_count):
      difference_vec = np.abs(reference_group_variance_vec - self.compute_group_variance_vec(omit_member_idx=i))
      differences.append(difference_vec)

    print("Differences", differences)

  def songs_without_member(self, member_idx):
    return self.songs[:member_idx * self.songs_per_member] + self.songs[(member_idx + 1) * self.songs_per_member:]
  
  def get_member_songs(self, member_idx):
    return self.songs[member_idx * self.songs_per_member : (member_idx + 1) * self.songs_per_member]
  
  def generate_shared_playlist(self):
    assert(self.friend_count == self.n_friends)
    # run alg to generate np array of vectorized songs fufilling DP requirements
  
  def compute_member_mean_vec(self, member_idx):
    a = np.array(self.get_member_songs(member_idx))
    return np.mean(a, axis=0)
  
  def compute_member_variance_vec(self, member_idx):
    a = np.array(self.get_member_songs(member_idx))
    return np.var(a, axis=0)
  
  def compute_group_mean_vec(self, omit_member_idx=-1):
    a = np.array(self.songs)
    if omit_member_idx != -1:
      a = np.array(self.songs_without_member(omit_member_idx))
    return np.mean(a, axis=0)

  def compute_group_variance_vec(self, omit_member_idx=-1):
    a = np.array(self.songs)
    if omit_member_idx != -1:
      a = np.array(self.songs_without_member(omit_member_idx))
    return np.var(a, axis=0)
