from sklearn.preprocessing import StandardScaler

def preproc(X):
    scaler = StandardScaler()
    return scaler.fit_transform(X)
