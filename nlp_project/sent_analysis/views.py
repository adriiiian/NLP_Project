from django.http import HttpResponse
from django.template import loader
from sent_analysis.forms import SentAnalysisForm
from sent_analysis.forms import SentAnalysis
from sent_analysis.apps import SentAnalysisConfig
import numpy as np
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Create your views here.

def home(request):
    template = loader.get_template("sent_analysis/home.html")
    form = SentAnalysisForm()

    context = {
        'form': form
    }

    return HttpResponse(template.render(context, request))

def predict(request):
    if request.method == "POST":
        form = SentAnalysisForm(request.POST)

        context = {
            'form': form
        }
        
        # Checks if the submitted inputs are valid
        if form.is_valid():

            raw_sentence = form.cleaned_data.get('sentence')        # Gets the string input from the input text field
            cleaned_sent = remove_irr_char(raw_sentence)            # Cleans the sentence by removing irrelevant characters and converting everything to lowercase
            swr_sent = remove_stop_words(cleaned_sent)              # Removes stopwords in the sentence
            lem_sent = lemmatize(swr_sent)                          # Lemmatize the sentence to break the words to its root.

            # Vectorize the pre-processed input text by the best performing vectorizer
            vect_sentence = SentAnalysisConfig.lemma_tfidf_vectorizer.transform([lem_sent]).toarray()

            # Calls the best performing model to predict the sentiment given the pre-processed input text
            prediction = SentAnalysisConfig.model7_svm_lemma_os_tfidf.predict(vect_sentence)
            result = None

            # Converts the output of the model to Positive, Negative or Neutral texts
            if prediction == 1:
                result = "Positive"

            elif prediction == -1:
                result = "Negative"

            else:
                result = "Neutral"

            context = {
                'form': form,
                'results': result,
            }

        template = loader.get_template("sent_analysis/home.html")

        return HttpResponse(template.render(context, request))

"""
    This function is used to remove irrelevant characters.
    Accepts a string (sentence)
    Returns a string (sentence cleaned form)
"""
def remove_irr_char(sentence):
    word_list = []
    tokenized_sent = nltk.word_tokenize(sentence)

    for i in tokenized_sent:
        word_list.append(''.join(j for j in i if i.isalnum()))

    word_list = list(filter(None, word_list))

    return ' '.join(word_list).lower()

"""
    This function is used to remove stopwords in the given list of stopwords.
    Accepts a string (sentence)
    Returns a string (sentence with removed stopwords)
"""
def remove_stop_words(sentence):

    tokenized = nltk.word_tokenize(sentence)
    stop_words = set({"a", "about", "an", "are", "as", "at", "be", "by", "com", "de", "en", "for", "from", "how", "i", "in",
                      "is", "it", "la", "of", "on", "or", "that", "this", "to", "was", "what", "when", "where", "who", "will",
                      "with", "und", "the", "www"})

    filtered_list = [
        word for word in tokenized if word.casefold() not in stop_words
    ]

    return ' '.join(filtered_list)

"""
    This function is used to lemmatize the sentence to convert each token into their root form.
    Accepts a string (sentence)
    Returns a string (sentence with lemmatize tokens)
"""
def lemmatize(sentence):
    lemmatizer = WordNetLemmatizer()
    word_list = []
    tokenized_sent = nltk.word_tokenize(sentence)
    for i in tokenized_sent:
        token = lemmatizer.lemmatize(i)
        word_list.append(token)

    return ' '.join(word_list)