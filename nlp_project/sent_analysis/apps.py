from django.apps import AppConfig
from django.conf import settings
import joblib
import os


class SentAnalysisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sent_analysis'

    model = joblib.load(os.path.join(settings.BASE_DIR, "models/log_reg_oversampling_ht.joblib"))
    model2 = joblib.load(os.path.join(settings.BASE_DIR, "models/log_reg_oversampling_ht_sr.joblib"))
    model3 = joblib.load(os.path.join(settings.BASE_DIR, "models/log_reg_oversampling.joblib"))
    model4_stopwords = joblib.load(os.path.join(settings.BASE_DIR, "models/log_reg_oversampling_stopwords.joblib"))
    model5_stopwords_oversampling_78 = joblib.load(os.path.join(settings.BASE_DIR, "models/log_reg_oversampling_stopwords_78acc.joblib"))
    model6_svm_stopwords_os = joblib.load(os.path.join(settings.BASE_DIR, "models/svm_os_cv.joblib"))

    vectorizer = joblib.load(os.path.join(settings.BASE_DIR, "models/tfidf_vectorizer.joblib"))
    vectorizer2 = joblib.load(os.path.join(settings.BASE_DIR, "models/tfidf_vectorizer2.joblib"))
    count_vectorizer = joblib.load(os.path.join(settings.BASE_DIR, "models/count_vectorizer.joblib"))

    # Best model
    model7_svm_lemma_os_tfidf = joblib.load(os.path.join(settings.BASE_DIR, "models/svm_lemma_os_tfidf.joblib"))

    #Best vectorizer
    lemma_tfidf_vectorizer = joblib.load(os.path.join(settings.BASE_DIR, "models/lemma_tfidf_vectorizer.joblib"))
