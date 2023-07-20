from django.http import HttpResponse
from django.template import loader
from sent_analysis.forms import SentAnalysisForm
from sent_analysis.forms import SentAnalysis
from sent_analysis.apps import SentAnalysisConfig
import numpy as np
import nltk
from nltk.stem import PorterStemmer

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
        # print("hello")
        if form.is_valid():

            raw_sentence = form.cleaned_data.get('sentence')
            cleaned_sent = remove_irr_char(raw_sentence)
            swr_sent = remove_stop_words(cleaned_sent)
            stem_sent = stem_sentence(swr_sent)
            print(swr_sent)
            print(stem_sent)

            vect_sentence = SentAnalysisConfig.vectorizer.transform([swr_sent]).toarray()
            # print(vect_sentence)
            # print(type(vect_sentence))
            prediction = SentAnalysisConfig.model2.predict(vect_sentence)
            # print(prediction)
            result = None
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



def remove_irr_char(sentence):
    word_list = []
    tokenized_sent = nltk.word_tokenize(sentence)

    for i in tokenized_sent:
        word_list.append(''.join(j for j in i if i.isalnum()))

    word_list = list(filter(None, word_list))

    return ' '.join(word_list)

def remove_stop_words(sentence):

    tokenized = nltk.word_tokenize(sentence)
    stop_words = set({"a", "about", "an", "are", "as", "at", "be", "by", "com", "de", "en", "for", "from", "how", "i", "in",
                      "is", "it", "la", "of", "on", "or", "that", "this", "to", "was", "what", "when", "where", "who", "will",
                      "with", "und", "the", "www"})

    filtered_list = [
        word for word in tokenized if word.casefold() not in stop_words
    ]

    return ' '.join(filtered_list)

def stem_sentence(sentence):
    stemmer = PorterStemmer()
    word_list = []
    tokenized_sent = nltk.word_tokenize(sentence)
    for i in tokenized_sent:
        stem_word = stemmer.stem(i)
        word_list.append(stem_word)

    return ' '.join(word_list)