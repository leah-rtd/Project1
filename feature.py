from sklearn.preprocessing import StandardScaler, OneHotEncoder

def preproc(X_num, X_cat):
    scaler = StandardScaler()
    ohe = OneHotEncoder()
    return scaler.fit_transform(X_num), ohe.fit_transform(X_cat)
