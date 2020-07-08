# Project-X

## Vision

This project was designed to foster a community where we vote not based on opinions created by biased media, fake-news, and political bots, but from the very source - the words of the politicians themselves. Twitter has become an ubiquituous platform when it comes to expressing political opinion and addressing the general population. We've seen millenial politicians such as @AOC having 7 million followers online while global leaders threaten each other publicly and with no shame - it's remarkable what one can do with just 150 characters. 

With Twitter being used as increasingly these days, courtesy of Covid-19 and 2020 Elections, it's obvious that the platform contains a lot of insights that would be relevant to one's decision making while voting in November. This project serves to be the spoon with which one takes in Twitter data.

## Ideas

### Politician Embeddings

The first idea that we are working on is to train a language model, 'AWD_LSTM' from fastai. Using a ton of political data, we will train the model to predict the next word and in the process, create word embeddings which will be adjusted for the political context. 

Next, using those embeddings, we train a classification model to predict which politician said a given tweet. We can then extract the last layer of the network to create embeddings for each politican. 

These embeddings can then be used to perform semantic analysis - such as extracting their political views from their embeddings by performing some transformation and mapping the results back to their initial weights, etc. 
