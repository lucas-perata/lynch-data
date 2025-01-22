
def mostrar_trailer(pelicula, st):
    trailers = {
        "Eraserhead" : "https://www.youtube.com/watch?v=7WAzFWu2tVw&ab_channel=RottenTomatoesClassicTrailers", 
        "The Elephant Man": "https://www.youtube.com/watch?v=AF9gNKJi79g&ab_channel=MUBI", 
        "Dune":"https://www.youtube.com/watch?v=sJ9VAJ1f0zU&ab_channel=VintageMovieTrailers", 
        "Blue Velvet":"https://www.youtube.com/watch?v=k_BybDB_phY&ab_channel=ParkCircus", 
        "Wild at Heart":"https://www.youtube.com/watch?v=dQIdBfrF0Ik&ab_channel=Shout%21Studios", 
        "Twin Peaks: Fire Walk with Me":"https://www.youtube.com/watch?v=5qQauPG61ZI&ab_channel=FilmTrailerChannel", 
        "Lost Highway":"https://www.youtube.com/watch?v=XmFgO2fJQuI&ab_channel=AustinFilmSociety", 
        "The Straight Story":"https://www.youtube.com/watch?v=ckrwH3Qdhz0&ab_channel=ImprintFilms", 
        "Mulholland Drive":"https://www.youtube.com/watch?v=jbZJ487oJlY&ab_channel=StudiocanalUK", 
        "Inland Empire":"https://www.youtube.com/watch?v=kS2v-icgBj4&ab_channel=STUDIOCANAL"
    }
    if pelicula in trailers:
        st.video(trailers[pelicula])
