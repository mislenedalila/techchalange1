import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor
import pickle

# 1. Carregar o dataset
df = pd.read_csv("insurance.csv")

# 2. Pré-processamento
df['sex'] = LabelEncoder().fit_transform(df['sex'])        # female=0, male=1
df['smoker'] = LabelEncoder().fit_transform(df['smoker'])  # no=0, yes=1
df = pd.get_dummies(df, columns=['region'], drop_first=True)

# 3. Separar variáveis
X = df.drop('charges', axis=1)
y = df['charges']

# 4. Dividir dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Treinar modelo
xgb_model = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
xgb_model.fit(X_train, y_train)

# 6. Salvar modelo treinado
with open("model_xgb.pkl", "wb") as f:
    pickle.dump(xgb_model, f)

print("✅ Modelo treinado e salvo como model_xgb.pkl")
