import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

names = ["Outlook", "Temperature",
         "Humidity", "Windy", "Play Golf"]

dataset = pd.read_csv("./play_golf.csv", names=names)

le = LabelEncoder()
for feature in names:
    dataset[feature] = le.fit_transform(dataset[feature])

X = dataset.drop("Play Golf", axis=1)
y = dataset["Play Golf"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=10)

gnb = GaussianNB()

gnb.fit(X_train, y_train)

y_pred = gnb.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("Unique Bhattarai, 28136/078, Lab No.15")
