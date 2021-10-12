def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb+srv://m220student:m220password@mycluster.cq2ga.mongodb.net/test"

   
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    return client['Movies']

if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()

    collection_name = dbname["Comedy"]
    
    com1 = {
        "Name" : "Rush Hour",
        "Producers": "Produced by: Roger Birnbaum, Jonathan Glickman, Arthur M. Sarkissian, Jay Stern, Robert Birnbaum, Michael Poryes",
        "Rating & Info": "'https://www.imdb.com/title/tt0120812/', 'https://www.rottentomatoes.com/m/rush_hour'"
        }
    com2  = {
        "Name" : "21 Jump Street", 
        "Producers": "Produced by: Directors: Phil Lord, Chris Miller", 
        "Rating & Info": "'https://www.imdb.com/title/tt1232829/', 'https://www.rottentomatoes.com/m/21_jump_street_2011'"
        }
    com3 = {
        "Name" : "Dope",
        "Producers": "Produced by: Nina Yang Boniovi, Forest Whitaker",
        "Rating & Info": "'https://www.rottentomatoes.com/m/dope_2015', 'https://www.imdb.com/title/tt3850214/'"
        }

    collection_name.insert_many([com1,com2,com3])

    collection_act = dbname["Action"]
    act1 = {
        "Name" : "Fast & Furios",
        "Producers": "Produced by: Justin Lin, Vin Diesel, Justin Lin, Samantha Vincent, Joe Roth, Neal H. Moritz, Clayton Townsend, Jeff Kirschenbaum",
        "Rating & Info": "'https://www.imdb.com/title/tt5433138/', 'https://www.rottentomatoes.com/m/f9'"
        }
    act2  = {
        "Name" : "Black Panther", 
        "Producers": "Produced by: Ryan Coogler, Kevin Feige", 
        "Rating & Info": "'https://www.imdb.com/title/tt1825683/', 'https://www.rottentomatoes.com/m/black_panther_2018'"
        }
    act3 = {
        "Name" : "Black Widow",
        "Producers": "Produced by: Cate Shortland",
        "Rating & Info": "'https://www.rottentomatoes.com/m/dope_2015', 'https://www.imdb.com/title/tt3850214/'"
        }

    collection_act.insert_many([act1,act2,act3])

    collection_ani = dbname["Animation"]
    ani1 = {
        "Name" : "Demon Slayer",
        "Producers": "Produced by: Shueisha",
        "Rating & Info": "'https://www.imdb.com/title/tt9335498/'"
        }
    ani2  = {
        "Name" : "Luca", 
        "Producers": "Produced by: Andrea Warren", 
        "Rating & Info": "'https://www.rottentomatoes.com/m/luca_2021'"
        }
    ani3 = {
        "Name" : "Naruto",
        "Producers": "Produced by: Shueisha",
        "Rating & Info": "'https://www.imdb.com/title/tt0409591/'"
        }

    collection_ani.insert_many([ani1,ani2,ani3])

    print(collection_name)
    print(collection_act)
    print(collection_ani)


