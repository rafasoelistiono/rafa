# Langkah 1: Mengimpor Perpustakaan yang Diperlukan
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Langkah 2: Menyiapkan Dataset
# Dataset sederhana (contoh)
data = {
    'size': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
    'bedrooms': [1, 2, 2, 3, 3, 3, 4, 4, 4, 5],
    'price': [150, 200, 250, 300, 350, 400, 450, 500, 550, 600]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Memisahkan fitur dan target
X = df[['size', 'bedrooms']]
y = df['price']

# Langkah 3: Membagi Dataset menjadi Set Pelatihan dan Set Pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Langkah 4: Membuat dan Melatih Model
model = LinearRegression()
model.fit(X_train, y_train)

# Langkah 5: Melakukan Prediksi
y_pred = model.predict(X_test)

# Langkah 6: Evaluasi Model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"Root Mean Squared Error: {rmse}")

# Menampilkan Hasil Prediksi dan Nilai Sebenarnya
predictions = pd.DataFrame({
    'Actual': y_test,
    'Predicted': y_pred
})
print(predictions)
