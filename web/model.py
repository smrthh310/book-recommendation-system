import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import pickle
import random
warnings.filterwarnings('ignore')

Ratings = pd.read_csv('Ratings_explicit.csv')
Ratings = Ratings[['User-ID','ISBN','Book-Rating']]
Final_Dataset = pd.read_csv('Final_Dataset.csv')
Books = pd.read_csv('Books.csv')
Ratings_explicit = pd.read_csv('Ratings_explicit.csv')
Top_Books = pd.read_csv('Top_Books.csv')

# Load the SVD model from the file
with open('model_svd.pkl', 'rb') as model_file:
    model_svd = pickle.load(model_file)

# Load the NMF model from the file
with open('model_nmf.pkl', 'rb') as model_file:
    model_nmf = pickle.load(model_file)


class Book_Recommender:

  def __init__(self):
    self.user_list = self.usersList(10)

  def getUsers(self):
    return self.user_list
  
  def setUsers(self):
    self.user_list = self.usersList(10)

  def svd(self, user_id, n=5):
    user_books = Ratings[Ratings['User-ID'] == user_id]['ISBN'].unique()
    all_books = Ratings['ISBN'].unique()
    books_to_predict = list(set(all_books) - set(user_books))

    user_book_pairs = [(user_id, book_id, 0) for book_id in books_to_predict]
    predictions_cf = model_svd.test(user_book_pairs)

    top_n_recommendations = sorted(predictions_cf, key = lambda x: x.est, reverse = True)[:n]

    top_n_book_ids = [str(pred.iid) for pred in top_n_recommendations]

    top_n_book_ids_str = [str(element) for element in top_n_book_ids]
    b = (Books[Books['ISBN'].isin(top_n_book_ids_str)][['Book-Title', 'Book-Author', 'Year-Of-Publication', 'Image-URL-L']])
    b = b.values.tolist()
    return b

  def nmf(self, user_id, n=5):
    user_books = Ratings[Ratings['User-ID'] == user_id]['ISBN'].unique()
    all_books = Ratings['ISBN'].unique()
    books_to_predict = list(set(all_books) - set(user_books))

    user_book_pairs = [(user_id, book_id, 0) for book_id in books_to_predict]
    predictions_cf = model_nmf.test(user_book_pairs)

    top_n_recommendations = sorted(predictions_cf, key = lambda x: x.est, reverse = True)[:n]

    top_n_book_ids = [str(pred.iid) for pred in top_n_recommendations]

    top_n_book_ids_str = [str(element) for element in top_n_book_ids]
    b = (Books[Books['ISBN'].isin(top_n_book_ids_str)][['Book-Title', 'Book-Author', 'Year-Of-Publication', 'Image-URL-L']])
    b = b.values.tolist()
    return b
  
  def read_history(self, user_id):
    user_books = Ratings[Ratings['User-ID'] == user_id]['ISBN'].unique()
    all_books = Ratings['ISBN'].unique()
    books_to_predict = list(set(all_books) - set(user_books))

    user_books_str = [str(element) for element in user_books]
    a = (Books[Books['ISBN'].isin(user_books_str)][['Book-Title', 'Book-Author', 'Year-Of-Publication', 'Image-URL-L']])
    a = a.values.tolist()
    return a
  
  def trending_books(self, n=20):
    a = Top_Books.head(n)
    a = a.values.tolist()
    return a



  # def userBasedCollaborativeFilter(self, user_id):
  #   # indexes to navigate in user-book rating matrix
  #   indexes = normalized_df.index
  #   # index = indexes.get_loc(user_id)
  #   index = first_row.index[first_row['User-ID'] == user_id][0]

  #   # fetching the books that are already read be the user
  #   books_read_by_user = normalized_df.loc[user_id][normalized_df.loc[user_id]>0]

  #   # calculating the cosine distance of this user with all other users, and selecting user with highest cosine relation
  #   cos_dist = cosine_distance.iloc[index]
  #   non_zero_columns = cos_dist[cos_dist != 0]
  #   sorted_df = non_zero_columns.sort_values(ascending=False)
  #   users_with_similar_interest = sorted_df[sorted_df>.3].index
  #   books = list()
  #   for user in users_with_similar_interest[1:]:
  #     books.append(normalized_df.iloc[int(user)][normalized_df.iloc[user]>0])

  #   merged_df = pd.concat(books)
  #   max_ratings = merged_df.groupby(level=0).max()
  #   max_ratings = max_ratings.sort_values(ascending=False)
  #   for i in books_read_by_user.index:
  #     try:
  #       max_ratings.drop(i, inplace = True)
  #     except:
  #       pass

  #   return max_ratings

  def usersList(self, n=10):
    user_id = [130866, 274005, 67415, 41911, 13600, 6537, 57599, 219924, 245616, 8323	, 35718, 256765, 37493, 93985, 207417	, 259066, 201923, 209536, 900, 17353, 178587,118344, 254751, 166390, 187378, 104654, 191009, 275793, 166055, 21340, 79854,30507,82968,77499,93377,116537,41123,140423,204044,178056	]
    
    if n>1:
      users=[]
      for i in range(n):
        users.append(user_id[random.randint(0, len(user_id)-1)])
      return users
    else:
      return user_id[random.randint(0, len(user_id)-1)]




  # print(userBasedCollaborativeFilter(67544))
  # print('\t************ Books Read By the User ************')
  # for i  in range(len(a)):
  #   print(f"{i+1}. {a[i]}")

  # print("\n\n")
  # print('\t************ Books Recommended to the User ************')
  # for i  in range(len(b)):
  #   print(f"{i+1}. {b[i]}")