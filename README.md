# BINF6251_FinalProject
Final Project for BINF6251

# Quick Start

## project overview

This program simulates an oscar season, optimizing nominees for each category using historical award data, and stochastically converges on movie crews with the highest chance of winning each category. Using the Metropolis-Hastings approach, with is an MCMC designed to search complex joint probabilities between variables and define their distributions. 

This program receives a .csv file containing historical information on the academy awards, such as: film year, category, nominee, and win status. This .csv file in converted into a pandas dataframe and preprocessed to include only the big five categories (actor, actress, directing, writing, best picture). The naming of these categories are universalized to handle category title changes over the years.

Expected output of this program is a dict of dicts, where outer dict keys are categories and values are movie objects, and the inner dict keys are the movie objects, and the values are a list of nominee objects. The final implementation will include an output that walks through an oscar season simulation and prints results in a more human-readable format

## installation/setup

Python v 3.14.4
pandas 3.0.2
tmdbv3api==1.9.0

installing pandas and tmdbv3api via pip is sufficient to execute program. 

tmbdv3api requires an api key to make API calls to The Movie Data Base, but a valid API key is hardcoded into the ```_get_filmography``` method

## Quick Start, usage, and options

The entire simulation can be run within the driver program ```Academy_award_show()```. The only arguments required to input is the desired year range the program should pull from. The program does require there to be an external dataframe provided, but not as an argument to the driver function. .csv lives in the ```/data``` directory. The dataframe will be processed within the program based on the year range input. 

The expected output should be a text-based simulation, describing who was nominated and the cast supporting them, and finally the winners for each category.

```
output snippet here

```

This program is broken into 2 main functions (all of which can be run with the ```Academy_award_show()``` call).

```metropolis_hastings()```: implements the primary algorithm, it creates instances of the object ```rand_movie```, and stochastically accepts/rejects new suggestions in comparison to active 'best choice'. Each movie is consistently, yet arbitrarily weighted by an ```oscar_score``` which considers direct wins and nominations, as well as participation in movies where cast mates have won/been nominated. The order of weight is as follows: direct win, direct nomination, indirect win, indirect nomination.

```sim_oscar_season()```: executes the ```metropolis_hastings()``` for each award category and returns a dictionary of all nominated movies and their crews per category.


A large part of this program is also class object for nominees and movies. Utilizing classes for each of these eased the ability to search complex probability distributions. example:  ```nominee.synergy_boost()``` to search common movies in the fimlographies of two nominees.


Example usage for program: 

```academy_award_show(1960, 2024)```


This will run a oscar show simulation and ideally select the best nominees for each category from 1960 - 2024.


## Limitations and Assumptions

The current version of this program is highly limited to the specific data that is input. It assumes that the .csv file has the correct columns will not handle ones that don't.

It also assumes that all relationships between cast members is equal, having standard weights that are added when two cast members have history on other movies, regardless of their roles.

The program only considers the categories of actor, actress, director, and writer and no others. It would increase time complexity as more categories are added, but generally with how it is currently set up, increasing the year range does not impact scalability significanly. 

## Evidence of correctness

Running this program using only one year should select the same crew for each nomination, and it should also nearly reflect the cast/crew that won each category.

And example when run on only 2024 

```
example here

```



















