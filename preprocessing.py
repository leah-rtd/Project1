from sklearn.preprocessing import StandardScaler

def preprocess_X(X):
    return StandardScaler().fit(X)
