import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Citire date
df = pd.read_csv("statie_meteo.csv", sep=";")

# 2. Definire target (ex.: temperatura_viitoare)
target_col = "target"  # schimbă cu numele real al coloanei țintă
X = df.drop(columns=[target_col])
y = df[target_col]

# 3. Împărțire train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Model XGBoost
model = XGBRegressor(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)
model.fit(X_train, y_train)

# 5. Feature importance
importances = model.feature_importances_
feat_imp = pd.DataFrame({
    "feature": X.columns,
    "importance": importances
}).sort_values("importance", ascending=False)

print("Feature importance XGBoost:")
print(feat_imp)

# 6. Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=feat_imp, x="importance", y="feature", orient="h")
plt.title("Importanța caracteristicilor – XGBoost (Stație Meteo Inteligentă)")
plt.tight_layout()
plt.show()
