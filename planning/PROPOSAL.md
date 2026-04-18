# Project Title
Academy Award Winning Film Optimizer 
# Research Question 
This program will provide a generated list of movies that have been optimized to win 6 selected academy awards categories. This will explore the predictability of winning an academy award given the historical success of each 'part' (actors, directors, composers, etc...). The results from this program could be insightful in the following ways:
 - highlighting the historical over/underrepresentation of groups nominated for academy awards
 - understanding the interplay between two seemingly disparate variables (given a lead actor/actress, can composer increase liklihood of oscar win?)  

# Algorithm 
I plan to use a monte carlo markov chain algorithm (MCMC), specifically the Metropolis-Hastings algorithm. I chose an MCMC to implement since this is a multi-variate problem, and the interplay between each variable is not easily defined (given a movies cast and crew, based on historical academy awards, how likely is that movie to win an award). I chose the Metropolis-Hastings algorithm in order to better handle sampling. I initially considered Gibbs sampling, but ultimately decided it was not the best choice considering the conditional distribution between the variables (given the director and lead actress, how does the screenwriter influence academy award liklihood) is not easily defined either. The Metropolis-Hastings algorithm will allow for changes to each variable, without understanding the conditional probabilities, and still allow for the probabilistic selection of the next state.  
# Data Plan
The academy awards website contains a database of every nominee for each category and their respective winners. Since the theoretical database of all professional film crew personal would be very large, building this program just using prior academy award nominees is ideal. IMDb will also be used to obtain movie information such as genre, cast list (program could selectively favor actors/actresses and directors that have worked together prior). I anticipate tha majority of the data structures utilized in this program will be lists and dictionaries. I plan to limit the data only to movies nominated for the six following categories: Best Picture, Actor, Actress, Director, Music, Writing (discussed in pitfalls, but will briefly discuss here... categories do not match 1:1 with current categories. Since categories have changed over the years, a broad approach is required).   

I would begin by attempting to construct a movie with a cast and crew capable with the highest chance of winning one or two categories. This will be controlled by inputting only a select data set into the algorithm, perhaps a data set containing only the cast and crew from movies where the director was nominated for best director. This should have an expected output, a generated movie directed by the director with the highest academy award win probability (wins/nominations), and then an ensemble of other cast/crew who may or may not have had academy award success. Ensuring that the model is working in this way, I could expand the data going into the model, and get a single generated movie that has an optimized chance to win every category, as long as the category is represented in the data.    
# Success Criteria 
Success in this project will result in a program that is able to generate an N number of movies that are all optimized in someway to win an academy award in the 6 given categories. Expected outputs are synthesized movies, with generated genre, cast (actor and actress), director, composer, and screenwriter. A simulated ground truth could be used to check the outputs, comparison to the 'idealized' movie may inform whether or not the expected output has an optimized academy award winning probability.  

# Pitfall scan

Data-related pitfall:
  - Mentioned above in data considerations, but if data is sourced from every year the academy awards have occurred, the categories/category names have shifted. This could derial the optimizer by not having the full data set available.
  - The 'size' of the current film market could also dilute the effectiveness of the optimizer, where older films/cast members could appear more frequently in the data due to a smaller nomination pool to pull from (or vice versa, I am unsure if this is genuinely the case)

Both of these issues are related to age of data being input into the program, so to handle this, the program could only take in the nomination lists from the past x amount of years (maybe 30 - 40). 
Another approach, specifically to the issue of changing categories would be to add some ambiguity, instead of creating a list of Actors and Actresses in leas and supporting roles, just create a list of actors and actresses. 

Algorithmic isuues: 
  - The primary algorithm issue I see need to address is the fact that the algorithm should maximally optimize a movie to win every category that is fed via the data. When generating a list of N movies to be nominees for a category, the movies generated would in theory be the same, or all equally optimized.

A way to handle this could be to impose constraints on the generation of each movie via implementing a faux budget or preventing two movies from having any overlapping crew/cast. This will generate a list of nominees for a category that have a more realistic distribution of award winning probabilities.  

Evaluation issues:
   -Since program generates theoretical scenarios, ground truth may be difficult to obtain. Output will be a list of movies, but there will need to be some additional way to assess their liklihood of winning an award.
   -Evaluation should only be considered based on previous trends and calculated probabilities. A shortcoming of this model is the very real presence of cultural influence that a movie may have on voters. This model will be unable to consider any member of a film cast/crew that has not been previously nominated for an oscar, which is also unrealistic.

   Potential ways to handle this would be a separate program that will assess their overall liklihood of winning the category it was nominated for, and probabilistically select one film from the list.
 
# Planned Repository
Repository will hold main program that generates a list of potential winners, all optimized in some way; a program that selects the oscar winner from a list of candidates that are nominated; and finally a program that wil simulate the academy award show (receiving nominations and choosing a winner for each category).
# Generative AI Disclosure

Chat-GPT 5 was used to understand the key differences between the practical applications of Gibbs sampling and Metropolis-Hastings

Prompt given: 'use cases of Gibbs vs Metropolis-Hastings'

Justification: Online resources use heavy mathematical terminology when discussing MCMC approaches, which are helpful for a deeper understanding of the algorithms' mathematical application, but may be difficult to glean practical uses. Chat-GPT was used to give a high level comparison between the two, and where they pratically differ. The specific response I received:

  - Use Gibbs if conditionals are easy and you want guaranteed acceptance.
  - Use MH if conditionals are hard, or you need more flexible proposals

This helped inform my decision to go with the metropolis-hastings implementation since the conditional distribution between variables in my project will be difficult to sample from. 

