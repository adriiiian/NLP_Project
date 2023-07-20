from django.apps import AppConfig
from django.conf import settings
import joblib
import os


class SentAnalysisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sent_analysis'

    model = joblib.load(os.path.join(settings.BASE_DIR, "models/log_reg_oversampling_ht.joblib"))
    model2 = joblib.load(os.path.join(settings.BASE_DIR, "models/log_reg_oversampling_ht_sr.joblib"))
    vectorizer = joblib.load(os.path.join(settings.BASE_DIR, "models/tfidf_vectorizer.joblib"))
