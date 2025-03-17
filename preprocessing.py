from sklearn.preprocessing import StandardScaler, OneHotEncoder

def preprocess_X(X):
    scaler = StandardScaler()
    ohe = OneHotEncoder()

    return scaler.fit_transform(X)
