from sklearn.preprocessing import StandardScaler

def preprocess_X(X):
    scaler = StandardScaler()
    return scaler.fit_transform(X)
