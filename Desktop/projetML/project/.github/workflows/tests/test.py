import pytest
import numpy as np
import joblib

# Charger le modèle
@pytest.fixture
def load_model():
    model = joblib.load("model.pkl")
    return model

#
