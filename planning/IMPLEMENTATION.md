# Project Snapshot
This project aims to create a simulated oscar season for the 'Big Five' awards (Best Picture, Actor, Actress, Screenplay, Director).
The algorithm that will be implmented is the Metropolis - Hastings Algorithm, which is an MCMC algorithm that is designed to be used when the conditional
probabilities between variables are unknoww/difficult to sample from. Currently, I have implemented a few classes, which are the primary means on which the MH algorithm will work. I still have some work to do implementing the algorithm itself, but I need to ensure that I am creating the variables needed for the MH algorithm, and assigning them with proper probabilities. 

# Implementation
I have overcome the hurdle I discussed in my pseudocode with getting the data into a usable format. I sourced a csv from kaggle that contains the required data. I was able to convert to a pandas dataframe and I am using that for my main source of data. I have mainly deviated from my pseudocode in a way that is more beneficial, and will allow for easier implementation. In my pseudocode I have multiple functions that work together to create a movie list, and obtain the cast list of that movie from the cinemagoer package, and randomize the movie cast selecting from all cast lists. In my implementation, the spirit of these functions are maintained, but they are found in classes. I have also shifted focus to the success of individual nominees, rather than the movie as a whole. I have implemented both classes I need to implement: ```nominee``` and ```random_movie```. ```nominee``` will track filmography, normalized oscar win score (to not penalize many nominations), and synergy between other cast members. ```random_movie``` will create a random movie cast from all instances of the ```nominee``` object. 

Still missing is the MH implementation, which is the core of the simulation, but easier to implement when the data input is sound.

# Prototype Demo runs
For prototype demo runs, I have been creating new dataframes focused on smaller time frames. The smaller the time frame, the more deterministic the model becomes. If it is only run on movies from 2024, then the winning crew members will be heavily favored. This will be able to be run with final_project.ipynb, which expects the datafile 'oscars_after2024.csv'

A successful run will output a list of movies nominated for a given category, and their Director, Lead Actor, Lead Actress, and writer

# Data Documentation
The test data originated from a .csv file found on Kaggle that contains all oscar nominated movies and their year, corresponding nominee, and whether they won.
When reading in the .csv as a pandas dataframe, all years prior to 1960 were filtered out. These dataframes can be further processed to only look at necessary information, and prototype data runs only look at a single year. Truth from these single year runs is presented with an oscar season that contains all nominated nominees.

# Discussion

Thus far, I have found massive value in my approach parsing and using pandas dataframes as my primary data type. I have had little to no prior experience with this, so I have learned quite a bit in that regard. I have also noticed the more I at tempt to implement, the more I realize there are additionaly things I need to cosnider to make the program run smoothly. 

I ran into quite a big issue halfway through my random movie class, cinemagoer stopped returning movie information. The internet was helpful for getting to the bottom of the issue, but it sounds like the way cinemagoer obtains information from IMDb, IMDb will frequently block queries from cinemagoer. Since I want to create a program that will always work, I need to find a way around this. My implementation looks a little bare, but once I find a work around for this I need to: 

1) finish the random movie class
2) implement the MH algorithm



