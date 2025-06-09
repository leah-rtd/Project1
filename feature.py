from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
def preproc(X):
    scaler = StandardScaler()
    model = LinearRegression()
    model.fit(X)
    return scaler.fit_transform(X)
