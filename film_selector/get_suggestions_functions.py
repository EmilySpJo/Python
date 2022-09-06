import random
import csv
import os

#dictionaries of combobox genres and corresponding csv file
netflixTVDict = {
  'TV Dramas':'netflix_TV_Dramas.csv',
 'Crime TV Shows':'netflix_TV_Crime_Shows.csv',
 'Reality TV':'netflix_reality_TV.csv',
 'TV Comedies':'netflix_TV_Comedies.csv',
'TV Action & Adventure':'netflix_TV_Action.csv',
 'Kids TV':'netflix_TV_Kids.csv',
 'Docuseries':'netflix_TV_Docuseries.csv',
 'Anime Series':'netflix_TV_Anime.csv',
 'Generic TV Shows':'netflix_TV_Generic.csv',
 'Romantic TV Shows':'netflix_TV_Romantic.csv',
 'TV Horror':'netflix_TV_Horror.csv',
'TV Mysteries':'netflix_TV_Mysteries.csv',
 'British TV Shows':'netflix_TV_British .csv',
 'TV Sci-Fi & Fantasy':'netflix_TV_Sci-Fi.csv',
'International TV Shows':'netflix_TV_International.csv'
}

netflixMovDict = {'Documentaries':'netflix_mov_Documentaries.csv',
 'Family Movies':'netflix_mov_Family.csv',
 'Dramas':'netflix_mov_Dramas.csv',
 'Comedies':'netflix_mov_Comedies.csv',
'Thrillers':'netflix_mov_Thrillers.csv',
 'Horror Movies':'netflix_mov_Horror.csv',
 'Action & Adventure':'netflix_mov_Action.csv',
 'Stand-Up Comedy':'netflix_mov_Stand_up.csv',
 'Music & Musicals':'netflix_mov_Musicals.csv',
 'Generic Movies':'netflix_mov_Generic.csv',
'Romantic Movies':'netflix_mov_Romantic.csv',
 'Anime Features':'netflix_mov_Anime.csv',
 'Sci-Fi & Fantasy':'netflix_mov_SciFi.csv',
'Sports Movies':'netflix_mov_Sports.csv'
}

amazonTVDict = {'Kids':'amazon_kids_tv.csv',
 'Comedy':'amazon_comedy_tv.csv',
 'Anime':'amazon_anime_tv.csv',
 'Generic':'amazon_generic_tv.csv',
 'Action':'amazon_action_tv.csv',
 'Drama':'amazon_drama_tv.csv',
 'Sports':'amazon_sports_tv.csv',
'Western':'amazon_western_tv.csv',
 'Documentary':'amazon_documentary_tv.csv',
 'Unscripted':'amazon_unscripted_tv.csv',
 'Horror':'amazon_horror_tv.csv',
 'Arts':'amazon_arts_tv.csv',
 'Special Interest':'amazon_special_tv.csv',
 'Science Fiction':'amazon_scifi_tv.csv',
 'Young Adult Audience':'amazon_ya_tv.csv',
'Animation':'amazon_animated_tv.csv',
 'Talk Show':'amazon_talk_show_tv.csv',
 'Adventure':'amazon_adventure_tv.csv',
 'Romance':'amazon_romance_tv.csv',
'Music Videos and Concerts':'amazon_music_tv.csv'
}

amazonMovDict = {'Comedy':'amazon_comedy_movies.csv',
 'Drama':'amazon_drama_movies.csv',
 'Action':'amazon_action_movies.csv',
 'Documentary':'amazon_documentary_movies.csv',
 'Kids':'amazon_kids_movies.csv',
 'Horror':'amazon_horror_movies.csv',
 'Science Fiction':'amazon_scifi_movies.csv',
 'Music Videos and Concerts':'amazon_music_movies.csv',
 'Sports':'amazon_sports_movies.csv',
 'Faith and Spirituality':'amazon_faith_movies.csv',
 'Special Interest':'amazon_special_movies.csv',
 'Western':'amazon_western_movies.csv',
 'Arts':'amazon_arts_movies.csv',
 'Anime':'amazon_anime_movies.csv',
 'Generic':'amazon_generic_movies.csv',
 'Adventure':'amazon_adventure_movies.csv',
 'Young Adult Audience':'amazon_ya_movies.csv',
 'Romance':'amazon_romance_movies.csv',
 'Animation':'amazon_animated_movies.csv',
 'Historical':'amazon_historical_movies.csv', 
'Fantasy':'amazon_fantasy_movies.csv', 
'Unscripted':'amazon_unscripted_movies.csv', 
'Suspense':'amazon_suspense_movies.csv'
}

#take in platform, genre and media, open the relevant csv file
def suggestor(platform,media,genre):
    suggestionsDict = [] #empty list, will be returned and contain suggestions
    netflixPath = './data/Netflix/'
    amazonPath = './data/Amazon/'

   ##############NETFLIX TV SHOW HANDLING##########################
    if platform == "Netflix" and media == "TV Show":
       with open(netflixPath+netflixTVDict[genre], encoding="utf8") as csv_file:
           csv_reader = csv.reader(csv_file, delimiter=',')
           line_count = 0
           for row in csv_reader:
                   line_count += 1
           #generate 3 random values within given range - will determine selection
           rand1 = random.randint(2, line_count)
           rand2 = random.randint(2, line_count)
           while(rand1 == rand2):
                rand2 = random.randint(1, line_count)
           rand3 = random.randint(2, line_count)
           while(rand3 == rand2 or rand3 == rand1):
                rand3 = random.randint(2, line_count)

       #find and store subsequent suggested content
       with open(netflixPath+netflixTVDict[genre], encoding="utf8") as csv_file:
           csv_reader = csv.reader(csv_file, delimiter=',')
           line_count = 0
           for row in csv_reader:
               line_count += 1
               if(line_count == rand1 or line_count == rand2 or line_count == rand3):
                 suggestionsDict.append(row[1])
                 suggestionsDict.append(row[5])

   ##############NETFLIX MOVIE HANDLING##########################
    elif platform == "Netflix" and media == "Movie": 
       with open(netflixPath+netflixMovDict[genre], encoding="utf8") as csv_file:
           csv_reader = csv.reader(csv_file, delimiter=',')
           line_count = 0
           for row in csv_reader:
                   line_count += 1
           #generate 3 random values within given range - will determine selection
           rand1 = random.randint(2, line_count)
           rand2 = random.randint(2, line_count)
           while(rand1 == rand2):
                rand2 = random.randint(1, line_count)
           rand3 = random.randint(2, line_count)
           while(rand3 == rand2 or rand3 == rand1):
                rand3 = random.randint(2, line_count)

       #find and store subsequent suggested content
       with open(netflixPath+netflixMovDict[genre], encoding="utf8") as csv_file:
           csv_reader = csv.reader(csv_file, delimiter=',')
           line_count = 0
           for row in csv_reader:
               line_count += 1
               if(line_count == rand1 or line_count == rand2 or line_count == rand3):
                 suggestionsDict.append(row[1])
                 suggestionsDict.append(row[5])

   ##############AMAZON TV SHOW HANDLING##########################
    elif platform == "Amazon Prime" and media == "TV Show": 
       with open(amazonPath+amazonTVDict[genre], encoding="utf8") as csv_file:
           csv_reader = csv.reader(csv_file, delimiter=',')
           line_count = 0
           for row in csv_reader:
                   line_count += 1
           #generate 3 random values within given range - will determine selection
           rand1 = random.randint(2, line_count)
           rand2 = random.randint(2, line_count)
           while(rand1 == rand2):
                rand2 = random.randint(1, line_count)
           rand3 = random.randint(2, line_count)
           while(rand3 == rand2 or rand3 == rand1):
                rand3 = random.randint(2, line_count)

       #find and store subsequent suggested content
       with open(amazonPath+amazonTVDict[genre], encoding="utf8") as csv_file:
           csv_reader = csv.reader(csv_file, delimiter=',')
           line_count = 0
           for row in csv_reader:
               line_count += 1
               if(line_count == rand1 or line_count == rand2 or line_count == rand3):
                 suggestionsDict.append(row[1])
                 suggestionsDict.append(row[5])

##############AMAZON MOVIE HANDLING##########################
    else:
       with open(amazonPath+amazonMovDict[genre], encoding="utf8") as csv_file:
           csv_reader = csv.reader(csv_file, delimiter=',')
           line_count = 0
           for row in csv_reader:
                   line_count += 1
           #generate 3 random values within given range - will determine selection
           rand1 = random.randint(2, line_count)
           rand2 = random.randint(2, line_count)
           while(rand1 == rand2):
                rand2 = random.randint(1, line_count)
           rand3 = random.randint(2, line_count)
           while(rand3 == rand2 or rand3 == rand1):
                rand3 = random.randint(2, line_count)

       #find and store subsequent suggested content
       with open(amazonPath+amazonMovDict[genre], encoding="utf8") as csv_file:
           csv_reader = csv.reader(csv_file, delimiter=',')
           line_count = 0
           for row in csv_reader:
               line_count += 1
               if(line_count == rand1 or line_count == rand2 or line_count == rand3):
                 suggestionsDict.append(row[1])
                 suggestionsDict.append(row[5])

    #return List
    return suggestionsDict