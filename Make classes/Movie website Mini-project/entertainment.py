import media
import fresh_tomatoes

dragonBallZ = media.Movie("Dragon Ball Z",
                        "A story of a boy",
                        "https://s-media-cache-ak0.pinimg.com/736x/b0/00/50/b0005011bad59c4b6a4ece6eec0ba693.jpg",
                        "https://www.youtube.com/watch?v=ajrmNsbfZhg")




avatar = media.Movie("Avatar",
                     "A marine on the alien planet",
                     "https://resizing.flixster.com/RekPVUC5CH4Vgulb0UaiXgYDbdM=/206x305/v1.bTsxMTE3Njc5MjtqOzE3MzY0OzEyMDA7ODAwOzEyMDA",
                     "https://youtu.be/5PSNL1qE6VY")

kingKong = media.Movie("King Kong",
                       "A giant monkey who rule the forest and has been captured by humans",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMjYxYmRlZWYtMzAwNC00MDA1LWJjNTItOTBjMzlhNGMzYzk3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                       "https://www.google.ht/url?sa=t&rct=j&q=&esrc=s&source=video&cd=4&cad=rja&uact=8&ved=0ahUKEwjC5I2QqqHTAhUK6yYKHew5DZAQuAIINDAD&url=http%3A%2F%2Fwww.allocine.fr%2Fvideo%2Fplayer_gen_cmedia%3D18404225%26cfilm%3D46718.html&usg=AFQjCNFjM6t4_ImCCneEMHTj40vaLANBZw&sig2=JoqbJq5a9vIMrEWttMfigA")



#print(avatar.show_trailer())
movies = [dragonBallZ, avatar, kingKong]
fresh_tomatoes.open_movies_page(movies)
