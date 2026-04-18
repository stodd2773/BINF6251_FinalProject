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







