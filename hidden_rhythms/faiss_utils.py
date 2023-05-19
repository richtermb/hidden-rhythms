import faiss

class FAISSWrapper(object):
  def __init__(self, dims):
    self.index = faiss.IndexFlatL2(dims)

  def add(self, v):
    self.index.add(v)

  def set_nprobe(self, n):
    self.index.nprobe = n

  def search(self, v, n):
    return self.index.search(v, n)

  def get_ntotal(self):
    return self.index.ntotal