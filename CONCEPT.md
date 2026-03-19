# Project Recap
This project sets out to create a realistic, but whimsical, Oscar season generator. 
This generator will take in the entire database of nominated directors, actors, movies and composers
and the overall win-rate of each, and simulate an oscar season of movies that have oscar potential. 
The algorithm will implement an MCMC approach, specifically the metropolis-hastings algortihm
which will be especially equipped to sample complex distributions where the joint probability and the conditional probability distributions are not well known.
Metropolis-hastings will allow for each iteration to make a suggestion by changing multiple variables and then probabilistically deciding between the new suggestion and the current suggestion.
Key data types that will be used in this projet will be lists and dictionaries.
Lists will be utilized largely in inputs, lists of actors, movies, etc; and dictionaries will be useful in considering oscar success and interactions between items (if implemented).
ex ({'Blue Velvet': {'award nomination':'Best Director, 'Director': 'David Lynch', ...}}

# Inputs, Outputs, and Assumptions
The planned inputs into this algorithm are as follows: 
	- Award nominees (List) from the academy awards database	
	- Movies with crew roles of interest (Dict) from IMDb. See above example in recap
	- Win rate of each item (Dict). An example here could be {'David Lynch' : {'Nominations' : 4, 'Wins' : 0, 'Success Rate' : 0.0}}, 
	  making it unlikely for David Lynch to be stochastically seletced for an optimized (highest win probability) oscar movie... unfortunately
The planned outputs from this algorithm will be as follows: 
	- Dictionary of movies and their respective crew along with oscar win probability
		-ex {'Movie Title': {'Director' : 'John Ford', 'Lead Actor' : 'Sean Penn', 'Lead Actress': 'Katherine Hepburn', 'Oscar win probability : 0.57}}
	
Some key assumptions that are made when implementing this algorithm are: 
	- All crew members input into the algorithm have been nominated for an oscar 
	- All crew members have an equal chance of being suggested by the algorithm, but unequal chance of selection

# Pseudocode 
FUNCTION create usable data structure from academy award databse
	input: url of academy award database website, list of oscar categories
	output: dictionary containing award names as keys and nominees as values, with special character to indicate winner
	// I am struggling a little bit with this function. Obtaining data from a website that is not in a format I am comfortable working with (tsv, csv, txt) is outside of my comfort zone and not something I have experience with. This function is important to obtain the desired data and data type. Although, I do think this function is the least important in terms of conceptual application of the algorithm

FUNCTION create nominated movie list

//idea of this function is to make a list of all movies that have been nominated for given category
input: data from first function
output: nominated movie list
	
initialize nominee list
for year in the range of start year to end year:
	for movie nominated in category
		append to nominee list
return the nominee list

FUNCTION get movie crew

//function will take in a list of movies and create a dictionary that maps movies to crew members
input: list of movies, list of desired crew
output: dictionary where key, value = movie, dictionary of cast members
Example output: {'Movie_Title : {Actor_1: 'Actor/Actress name', Actor_2: 'Actor/Actress name', Director: 'Director name}

for movie in list of movies:
	for key in dictionary[Movie_Title]
	use IMDb python package cinemagoer to obtain actor1, actor2, etc. 
	

# Complexity and Bottleneck
A reliable aspect of complexity in this algorithm is, every single input will have the same, predefined length. 
By selecting the criteria we care about, we can control complexity in this aspect. Complexity will begin 
to increase depending on the number of awards introduced and the decision on whether or not the algorithm will care 
about interactions between crew members. Example of this would be a boost in win probability when Martin Scorsese and 
Robert De Niro are suggested by the algorithm to be in a movie together. This would significantly boost complexity since 
now we would have to consider the interactions between each crew member. We would have to take our IMDb input and search each crew member's
filmography and find crewmates that are also in the current suggestion. Understanding how that synergy and how it impacts win probability will 
be dependent on if the duo has won an oscar together, which will require an additional search of IMDb and the academy awards database. 
This complexity becomes amplified if there happens to be a trio of crew members that have worked together. 

I have three possible 'approaches' to this:
	1. Not consider synergistic probability boosts. 
			- Although not really an 'approach', I think this is the most viable way to handle this complexity. Given the potential for this 
			implementation to become highly complex, I think the benefit it gives is trivial and ultimately not worth the cost. I think the 
			algorithm is still effective without this consideration
	2. Apply a constant factor to relationships regardless of previous succcess.
			- This approach comes with two major assumptions. The first is that any previous relationship between crewmembers is viewed
			as having a positive impact on win probability. The second is all previous relationships between crewmembers is equal. Realistically, 
			these seem like bold assumptions to make, but this approach helps reduce complexity by not considering the joint success of two or more
			crewmembers.
	3. Reduce scope to only focus on a few types of relationships
			- Taking this approach, we could prioritize traditionally high-value relationships such as Lead Actor/Actress or Lead Actor/Director.
			and ignore some others like Director/Composer (although it is hard for me to deny the synergy between George Lucas and John Williams didn't
			define my childhood). We could also only search for relationships within oscar nominated movies, significantly reducing the filmography search for each
			crewmember. This seems like the most proabable approach if I want to retain the 'relationship factor' and reduce complexity as much as possible. This also works
			with the second assumption that all relationships are positive ones, since we are only searching oscar nominated films.

I also think some combination of the above approaches could be beneficial. For example, only searching oscar nominated movies for three key relationships will significantly reduce complexity 
while retaining the 'relationship factor'.

  			
			


	
