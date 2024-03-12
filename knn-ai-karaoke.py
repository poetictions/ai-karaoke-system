from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = [
    ['Bar', 'Happy', 'High'],
    ['Club', 'Energetic', 'Low'],
    ['Beach', 'Relaxed', 'Medium'],
    ['Bar', 'Happy', 'Medium'],
    ['Club', 'Energetic', 'High'],
    ['Beach', 'Relaxed', 'Low']
]


y = ['Song A', 'Song B', 'Song C', 'Song D', 'Song E', 'Song F']

label_encoders = [LabelEncoder() for _ in range(len(X[0]))]
for i in range(len(X[0])):
    X[:, i] = label_encoders[i].fit_transform([x[i] for x in X])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


k = 3
knn_model = KNeighborsClassifier(n_neighbors=k)
knn_model.fit(X_train, y_train)


y_pred = knn_model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

new_data = [[1, 2, 0]]
for i in range(len(new_data[0])):
    new_data[0][i] = label_encoders[i].transform([new_data[0][i]])[0]
prediction = knn_model.predict(new_data)
print("Predicted song recommendation:", prediction[0])