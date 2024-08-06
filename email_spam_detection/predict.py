import pickle


def load_model():
    with open("./models/trained_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model


def load_vectorizer():
    with open("./models/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    return vectorizer


def predict(model, vectorizer, text):
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)
    return prediction[0]
