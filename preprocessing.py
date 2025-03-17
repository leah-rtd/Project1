from sklearn.preprocessing import StandardScaler, OneHotEncoder

def preprocess_X(X):
    ohe = OneHotEncoder()
    return StandardScaler().fit_transform(X)
