import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1. Load CSV data
df = pd.read_csv('chewdata.csv')

# 2. Prepare data
X = df[['chews']]
y = df['mood']

# 3. Split data into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 4. Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 5. Save model
joblib.dump(model, 'mood_model.pkl')

print("🎯 Model trained and saved as mood_model.pkl!")
