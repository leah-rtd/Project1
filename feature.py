from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
def preproc(X):
    scaler = StandardScaler()
    ohe = OneHotEncoder()
    model = LinearRegression()
    model.fit(X)
    return scaler.fit_transform(X)
