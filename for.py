# game = input("מה המשחק האהוב עליך? ")

# if game == "GTA":
#     print("בחירה מצוינת! גם אני אוהב עולם פתוח והרבה אקשן!")
# elif game == "Minecraft":
#     print("נראה שאתה טיפוס יצירתי 🧱")
# elif game == "FIFA":
#     print("כדורגל זה החיים! ⚽")
# else:
#     print("מעניין! אני לא מכיר את המשחק הזה, אולי תספר לי עליו?")




# num = float(input("give me a number please. "))

# if num > 100:
#     print("its a small number. ")
# elif num < 0:
#     print("this is a big number!")
# else:
#     print("this is not a number. . ")



# print(input("what is your fev food? "))

# food = ["pizza", "buffalo wings","sushi","apple pie"]

# if ("french fries") in food:
#     print("i really love sushi (: ")

# elif ("pizza") in food:
#     print("is nice, but sushi is better! ")

# elif ("sushi"):
#     print("is not in my list")
# else:
#     print("bring me my sushiii!!")


user_movie = input("What Is Your Fev Movie? ").strip().lower() 

movies = ["The Dark Knight", "Inception", "Interstellar", "The Matrix", "John Wick",
    "Mad Max: Fury Road", "Gladiator", "Avengers: Endgame", "Spider-Man: Into the Spider-Verse",
    "The Lord of the Rings: The Fellowship of the Ring", "The Shawshank Redemption",
    "The Godfather", "Pulp Fiction", "Fight Club", "Se7en", "Parasite", "Whiplash",
    "Get Out", "A Quiet Place", "Toy Story", "Coco", "Inside Out", "Finding Nemo",
    "Oppenheimer", "Barbie"] 


movies_lc = [m.lower() for m in movies]


if user_movie == "fight club":
    print("brad pitt is  the best!! ")

elif "lord_of_the_ring" in user_movie:
    print ("i love the books")

elif user_movie == "toy tory":
     print("i've seen the movie many times.")

else:
    print("not in my list :( ")

