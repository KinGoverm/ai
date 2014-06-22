from scikits.crab import datasets


movies = datasets.load_sample_movies()
songs = datasets.load_sample_songs()
print movies.data
print movies.user_ids
print movies.item_ids

from scikits.crab.models import MatrixPreferenceDataModel
#Build the model
model = MatrixPreferenceDataModel(movies.data)

from scikits.crab.metrics import pearson_correlation
from scikits.crab.similarities import UserSimilarity
#Build the similarity
similarity = UserSimilarity(model, pearson_correlation)

print similarity[1]

from scikits.crab.metrics.pairwise import euclidean_distances
similarity = UserSimilarity ( model , euclidean_distances)

print similarity[5]


from scikits.crab.recommenders.knn import UserBasedRecommender

#Build the User based recommender
recommender = UserBasedRecommender(model, similarity, with_preference=True)
#Recommend items for the user 5 (Toby)
recommender.recommend(5)

