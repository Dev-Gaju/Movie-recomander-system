import streamlit as st
import pickle
import  pandas as pd
import requests

#pip freeze >requirments.txt

def fetch_poster(movie_id ):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def movie_recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])

    recommended_movie_list =[]
    recomandations_movie_poster=[]
    for i in movies_list[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_list.append(movies.iloc[i[0]].title)
        #fetch_movie poster from api
        recomandations_movie_poster.append(fetch_poster(movie_id))
    return recommended_movie_list, recomandations_movie_poster

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.header("Movie Recommander System")

selected_movie_name = st.selectbox(
    'How would you be connected',
    (movies['title'].values))

if st.button('Recommend'):
    recommended_movie_names, recommended_movie_posters=movie_recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])