import fresh_tomatoes
import media

# Instantiates some movie objects 
walk_like_a_man = media.Movie("Walk Like a Man",
									1987,
									"Boy raised by wolves is reunited as an adult with his real family.",
									"https://upload.wikimedia.org/wikipedia/en/4/4e/Walk_like_a_man_poster.jpg",
									"https://www.youtube.com/watch?v=q9Ym1YxbgUI",
									"Melvin Frank",
									)

high_and_low = media.Movie("High and Low", 
									1963,
									"An executive of a shoe company becomes a victim of extortion when his chauffeur's son is kidnapped and held for ransom.",
									"https://upload.wikimedia.org/wikipedia/en/6/6a/HIGH_AND_LOW_JP_.jpg",
									"https://www.youtube.com/watch?v=yEWnX5vxU3o",
									"Akira Kurosawa",
									5
									)

pee_wee = media.Movie("Pee-wee's Big Adventure",
										1985,
										"When eccentric man-child Pee-Wee Herman gets his beloved bike stolen in broad daylight, he sets out across the U.S. on the adventure of his life.",
										"https://upload.wikimedia.org/wikipedia/en/e/e1/Peeweebigadventure.jpg",
										"https://www.youtube.com/watch?v=ZrzqBwuxHV8",
										"Tim Burton",
										4
										)

holy_mountain = media.Movie("The Holy Mountain",
										1973,
										"In a corrupt, greed-fueled world, a powerful alchemist leads a Christ-like character and seven materialistic figures to the Holy Mountain, where they hope to achieve enlightenment.",
										"http://sociologai.lt/wp-content/uploads/2015/02/holy.jpg",
										"https://www.youtube.com/watch?v=V_k8oaeHsnc",
										"Alejandro Jodorowsky",
										5
										)

abbott_costello = media.Movie("Abbot and Costello Meet Frankenstein",
										1948,
										"Two hapless freight handlers find themselves encountering Dracula, the Frankenstein Monster and the Wolf Man.",
										"https://upload.wikimedia.org/wikipedia/en/2/23/A%26cfrank.jpg",
										"https://www.youtube.com/watch?v=Gg5N9FJc__Q",
										"Charles Barton",
										3
										)

l_age_d_Or = media.Movie("L'Age d'Or",
										1930,
										"A surrealist tale of a man and a woman passionately in love with one another, but their attempts to consummate that passion are constantly thwarted by their families, the Church, and bourgeois society.",
										"https://upload.wikimedia.org/wikipedia/en/2/2f/L'Age_d'Or.jpg",
										"https://www.youtube.com/watch?v=pXBiBeYAwcM",
										"Luis Bunuel",
										5
										)

# Creates collection of movies
movies = [walk_like_a_man, pee_wee, high_and_low, holy_mountain, abbott_costello, l_age_d_Or]
# Runs the open_movies_pages function in fresh_tomatoes, passing movies as argument
fresh_tomatoes.open_movies_page(movies)