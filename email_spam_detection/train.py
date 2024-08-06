from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pickle


def split_data(data, target):
    X_train, X_test, y_train, y_test = train_test_split(
        data, target, test_size=0.2, random_state=42
    )
    return X_train, X_test, y_train, y_test


def vectorize_text(X_train, X_test):
    vectorizer = CountVectorizer()
    vectorizer.fit(X_train)
    X_train = vectorizer.transform(X_train)
    X_test = vectorizer.transform(X_test)
    return X_train, X_test, vectorizer


def train_model(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred) * 100
    precision = precision_score(y_test, y_pred, average="weighted") * 100
    recall = recall_score(y_test, y_pred, average="weighted") * 100
    f1 = f1_score(y_test, y_pred, average="weighted") * 100
    return accuracy, precision, recall, f1


def save_model(model):
    # save model at ./models
    with open("./models/trained_model.pkl", "wb") as file:
        pickle.dump(model, file)


def save_vectorizer(vectorizer):
    with open("./models/vectorizer.pkl", "wb") as file:
        pickle.dump(vectorizer, file)
