## Movie Recommendation System
Recommender System is a system that seeks to predict or filter preferences according to the user’s choices. Recommender systems are utilized in a variety of areas including movies, music, news, books, research articles, search queries, social tags, and products in general. 
Recommender systems produce a list of recommendations in any of the two ways – 
 

Collaborative filtering: Collaborative filtering approaches build a model from the user’s past behavior (i.e. items purchased or searched by the user) as well as similar decisions made by other users. This model is then used to predict items (or ratings for items) that users may have an interest in.
Content-based filtering: Content-based filtering approaches uses a series of discrete characteristics of an item in order to recommend additional items with similar properties. Content-based filtering methods are totally based on a description of the item and a profile of the user’s preferences. It recommends items based on the user’s past preferences.
Let’s develop a basic recommendation system using Python and Pandas. 
Let’s focus on providing a basic recommendation system by suggesting items that are most similar to a particular item, in this case, movies. It just tells what movies/items are most similar to the user’s movie choice.
To download the files, click on the links – .tsv file, Movie_Id_Titles.csv.
Import dataset with delimiter “\t” as the file is a tsv file (tab-separated file). 
 



# import pandas library 
import pandas as pd 
  
# Get the data 
column_names = ['user_id', 'item_id', 'rating', 'timestamp'] 
  
path = 'https://media.geeksforgeeks.org/wp-content/uploads/file.tsv'
  
df = pd.read_csv(path, sep='\t', names=column_names) 
  
# Check the head of the data 
df.head() 
