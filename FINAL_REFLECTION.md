# Final Reflection 

## Successes

Utilization of classes (```rand_movie``` and ```nominee```) significanlty boosted the ease of calculating the oscar strength of a movie, finding similarities in filmographies between nominees, and storing relevant data for each object of the class. I think other personal successes for me was building a new skill set and learning how to manipulate , filter, and navigate pandas dataframes. Since I was previously unfamiliar with the pandas package, I was required to do a lot of research and understand how it is used to effectively implement my project. I anticipate this will be a very usefull skill moving forward. 

## Struggles

Some aspects of this project that didn't go as well as I had planned was handling the optimization complexities that were inherent to my research question. I felt that each time I sat down to plan, or implement, I became aware of extra considerations that I had not thought about previously. An example for this was, in an early version of my program, I was treating participation in nominated movies the same for nominees, regardless if they were the one being nominated or not. I found this to be a relatively easy fix, adding lesser weights to indirect oscar wins/nominations, but this exemplifies that oversights to how the program considers oscar strength.

Another struggle was considering what truth was for my outputs since this project is largely novel and experimental. There is not an easily obtained ground truth for this theoretical simulation, but I found managing this struggle by limiting the year search range was sufficient enough. 

## Algorithm insights

I think Metropolis-Hastings was the ideal choice for navigating this program due to its relative simplicity to implement, and its ability to search complex, difficult to obtain joint probabilities. Since oscar_strength weights were arbitrarily decided by me, it was difficult to pinpoint what convergence looks like. So, instead of relying on convergence, inreasing the number of iterations ensured that by the time max iterations were reached, a strong candidate was chosen. I think there is realism in this approach too, since if I ran the algorithm until convergence, theoretically, all five of my nominated movies per category would be very similar... and what's the fun in that?

I think this was the main tradeoff, where my output might not be the movie with the absolute best chance of winning the oscar, it made for easier implementation. 

## Future Direction

Further extending this project would require making it more adaptable to different input data. Finding ways to not hardcode the desired categories into the program could extend its usability to all oscar categories, and the user could simulate a full scale oscar season. 

## Generative AI disclosure

Claude sonnet 4.6 was used: 'summarize pandas dataframe filtering methods'

justification: to summarize methods to filter and extract desirable data from pandas dataframes expressed in language for myself who was using pandas for the first time. 
