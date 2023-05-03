import os

from hidden_rhythms import dataset

if __name__ == "__main__":
	dirname = os.path.dirname(__file__)
	zip_path = os.path.join(dirname, "../hidden_rhythms/tracks.csv.zip")
	print("Testing dataset at {}...".format(zip_path))
	df = dataset.load_tracks_dataset(zip_path)
	print("Getting first row...")
	print(dataset.vectorize(df.iloc[0]))
