class category: 

    def __init__(self, df, category):
        
        self.category = category
        self.df = df[df['category'].str.contains(self.category)]
        self.movie_list = list(self.df['film'])

class nominee: 

    def __init__(self, name, df, cat, role, cat_to_role_dict):

        self.name = name
        self.role = role
        self.cat_to_role_dict = cat_to_role_dict
        self.o_df = df

        self.c = category(df, cat)
        # Isolate only the oscar movies the nominee has appeared in for this category (even if not the awards intended recipient)

        

    
    def _get_filmography(self):

        tmdb = TMDb()
        person = Person()
        movie = Movie()

        tmdb.api_key = 'f49d2ebf0d11031312ade120f61c513d'

        nominee_search = person.search(self.name)

        nomID = nominee_search[0].id

        url = f"https://api.themoviedb.org/3/person/{nomID}/combined_credits"
        params = {"api_key": tmdb.api_key}
        
        data = requests.get(url, params=params).json()

        movies = data['cast']

        filmography = [m["title"] for m in movies if "title" in m]

        filmography = [f.lower() for f in filmography]

        

        

        return filmography
    
    def set_self_df(self):

        if self.cat_to_role_dict[self.c.category] == self.role:
            self.df = self.o_df[(self.o_df['role'] == self.role) & (self.o_df['name'] == self.name)]
        else: 
            self.df = self.o_df[self.o_df['film'].isin(self._get_filmography())] 

        return self.df   
        

    def nom_cat_appearances(self):

        self.df = self.set_self_df()

        self.nom_category_appearance = self.df[
        self.df['film'].isin(self.c.df['film']) & 
        self.df['category'].isin(self.c.df['category'])
        ]    

        return self.nom_category_appearance
    

    def oscars_score(self):

        '''
        function calculates a weight based on oscar nominations and wins. Wins are heavily favored, but nominations are not counted against as they would be in a probabilistic determination 
        of success 
        
        param: self <- object of nominee class
        returns: weighted oscar score
        
        '''


        self.nom_category_appearance = self.nom_cat_appearances()
        
        # Isolate only the winners from the category nominations the nominee has appeared in 
        outcomes = list(self.nom_category_appearance['winner'])

        # initialize oscar score
        oscar_score = 0

        # If nominee has no previous nominations for category
        if len(outcomes) == 0:
            return 0
        else:
            # Iterate through each movie's outcome and add weighted score to oscar score
            for decision in outcomes:
                if self.cat_to_role_dict[self.c.category] == self.role:
                    if decision == True: 
                    #arbitrary weighting, favorable weighting for a win
                        oscar_score += 5
                    else: 
                        oscar_score += 3
                elif self.cat_to_role_dict[self.c.category] != self.role:
                    if decision == True:
                        oscar_score += 1
                    else: 
                        oscar_score += 0.5
                else: 
                    #arbitrary weighting, less favorable but still positive weighting for a nomination
                    oscar_score += 0

        return oscar_score

    def synergy_boost(self, crew_list):

        '''
        Function considers past professional relationships with other nominees and calculates a synergy boost.

        param1: self <- object of nominee class
        param2: crew_list <- list of other crew members on movie, each item in list is an instance of the nominee class

        returns: new score with added synergy boost
        '''
        
        self.df = self.set_self_df(

        )
        # Initialize empy list for common movies
        all_common_movies = []

        # Initialize synergy score
        synergy_score = 0 

        # Iterate through crew list
        for member in crew_list:
            # Exclude self
            if member.name != self.name:
                # Takes the intersection between self and other crew members filmoraphy
                common_movies = set(member._get_filmography()) & set(self._get_filmography())
                # if 1 or more movies in common
                if len(common_movies) > 0:
                    # iterate through common movies
                    for movies in common_movies: 
                        # add to list of common movies shared between self and all other nominees 
                        all_common_movies.append(movies)        
                else:
                    # If no movies in common return a synergy score of 0
                    return 0
            else: 
                continue
                
        for movie in all_common_movies:
            row = self.df[self.df["film"] == movie]

            if row.empty:
                continue  # movie wasn’t nominated at all

            if row["winner"].iloc[0] is True:
                synergy_score += 0.6
            else:
                synergy_score += 0.2

        return synergy_score
    
    def __repr__(self):
        
        return self.name
    
class rand_movie: 

    def __init__(self, category, talent_pool, oscar_df, cat_to_role_dict):

        self.category = category

        self.talent_pool = talent_pool

        self.crew_list = list(self.credits().values())

        self.cat_to_role_dict = cat_to_role_dict

        self.nominee = cat_to_role_dict[category]

        self.oscar_df = oscar_df



    def hire_crew(self, role):

        pool = list(self.talent_pool[role])

        rng = np.random.default_rng(seed=56)

        i = rng.integers(low = 0,  high = len(pool))

        name = pool[i]

        return nominee(name, self.oscar_df, self.category, role, self.cat_to_role_dict)
    


    def credits(self):

        

        self.actor = self.hire_crew('actor')

        self.actress = self.hire_crew('actress')

        self.director = self.hire_crew('director')

        self.writer = self.hire_crew('writer')

        self.crew_dict = {
            'actor': self.actor, 
            'actress': self.actress,
            'director': self.director,
            'writer': self.writer, 
        }

        return self.crew_dict
    
    def movie_oscar_score(self): 
        
        crew_list = list(self.crew_dict.values())
        score = 0 

        for crew in self.crew_dict.values():  
            oscar_score = crew.oscars_score()
            synergy_score = crew.synergy_boost(crew_list)
            score += oscar_score + synergy_score
    
        return score  
    
    def __repr__(self): 

        return str(list(self.crew_dict.values()))