import streamlit as st
import pickle as pk
import pandas as pd
import difflib
#import requests
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://netflixjunkie.com/wp-content/uploads/2021/11/Netflix-Background-1-1140x600.jpg");
background-size: cover;
}
[data-testid="stHeader"]{
    background-colour: rgba(255, 255, 255);
}
[data-testid="stToolbar]{
    right:2rem;
}
[data-testid="stWrite"]{
    background-colour: rgba(255, 255, 255);
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)
#def fetchposter(movie_id):
    #response=requests.get('https://api.themoviedb.org/3/discover/movie{}?api_key=15d2ea6d0dc1d476efbca3eba2b9bbfb'.format(movie_id))
    #data = response.json()
    #print(data)
    #return "https://image.tmdb.org/t/p/original" +data['poster_path']

def recommend(movie):
    movie_name=movie
    titles=movies['title'].to_list()
    matching=difflib.get_close_matches(movie_name,titles)
    closest_match=matching[0]
    index=movies[movies.title == closest_match]['index'].values[0]
    similar_score=list(enumerate(similarity[index]))
    sorted_similar_movies = sorted(similar_score, key = lambda x:x[1], reverse = True) 
    title_from_index=[]
    movie_posters=[]
    for m in sorted_similar_movies:
        index = m[0]
        #poster_index=movies[movies.index==index]['id'].values[0]
        title_from_index.append(movies[movies.index==index]['title'].values[0])
        #movie_posters.append(fetchposter(poster_index))
    return title_from_index#,movie_posters
similarity=pk.load(open('similarity.pkl','rb'))
movie_list=pk.load(open('moviesdict.pkl','rb'))
movies=pd.DataFrame(movie_list)

st.title("Movie Recommendation System")


#st.image("Netflix.png",use_column_width="always")
option= st.text_input("Enter Movie Name", key="name")

if st.button("Recommend"):
    recommendations=recommend(option)
    col1,col2,col3,col4,col5,col6=st.columns(6)
    with col1:
        st.write("**"+recommendations[0]+"**")    
    with col2:
        st.write("**"+recommendations[1]+"**")
    with col3:
        st.write("**"+recommendations[2]+"**")
    with col4:
        st.write("**"+recommendations[3]+"**")
    with col5:
        st.write("**"+recommendations[4]+"**")
    with col6:
        st.write("**"+recommendations[5]+"**")
