# EdCheckAI API doc and usage

# Endpoints:

## 1) Root endpoint:

### How to access it

Make a GET request to API url

### Output

A welcome message, that confirms that the connection between the flutter app and the API is working properly, without any errors/issues.


## 2) Sentiment + Paraphraser endpoint:

### How to access it

Make a POST request to API url + "/paraphraser_sentiment_checker/" with a Dictionary object of the following format:
{
text = "YOUR INPUT TEXT HERE"
}

### Output

The output is one of the following Dictionary types:

a) {"Positive", []} : This means that the response that the tutor is about to send has a positive/encouraging sentiment, hence no alternate sentence is suggested to the tutor.


b) {"Negative", ["Alternate1", "Alternate2", "Alternate3", ...]} : This means that the response that the tutor is about to send does not have a positive/encouraging sentiment, and a list of alternate sentences are suggested to the tutor in the array.



