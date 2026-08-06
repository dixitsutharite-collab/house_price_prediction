from sklearn.datasets import fetch_california_housing
import pandas as pd
import numpy as np
from sklearn.metrics import ( mean_squared_error, r2_score)
from sklearn.model_selection import train_test_split
import xgboost as xgb
import joblib

housing = fetch_california_housing()
df = pd.DataFrame(housing.data, columns=housing.feature_names)

df["Price"] = housing.target

X = df[['MedInc', 'HouseAge', 'AveRooms', 'Population', 'Latitude', 'Longitude']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = xgb.XGBRegressor(objective='reg:squarederror',
                         n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
print(f"RMSE: {rmse}")
print(f"R²: {r2}")

joblib.dump(model, "house_price_model.joblib")
print("Model Saved Successfully!")