import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):

    url = "https://api.themoviedb.org/3/movie/{}?api_key=9c06ec00c84ae317f18eb88b1a7d640c&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):

    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

# made a pickled file of db as movies_dict in form of dictionary
# that is why we're accessing it like this in the dictionary


st.header('Movie Recommender System')
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Create a select box for movie selection
selected_movie = st.selectbox(
    'Which movie would you like to watch?',
    movies['title'].values
)


if st.button('Show Recommendation'):
    recommended_movienames, recommended_movieposters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movienames[0])
        st.image(recommended_movieposters[0])
    with col2:
        st.text(recommended_movienames[1])
        st.image(recommended_movieposters[1])

    with col3:
        st.text(recommended_movienames[2])
        st.image(recommended_movieposters[2])
    with col4:
        st.text(recommended_movienames[3])
        st.image(recommended_movieposters[3])
    with col5:
        st.text(recommended_movienames[4])
        st.image(recommended_movieposters[4])
