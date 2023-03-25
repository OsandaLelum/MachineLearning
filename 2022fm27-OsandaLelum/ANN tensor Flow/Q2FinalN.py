# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 11:58:18 2023

@author: osandal
"""

import pandas as pd

# Load the dataset using pandas
df = pd.read_exel('Dry_Bean_Dataset.xlsx')

# Convert the categorical variable 'Class' to numerical values
class_map = {'BARBUNYA': 0, 'BOMBAY': 1, 'CALI': 2, 'DERMASON': 3, 'HOROZ': 4, 'SEKER': 5, 'SIRA': 6}
df['Class'] = df['Class'].map(class_map)

# Separate the features and target variable
X = df.drop(['Class'], axis=1).values
y = df['Class'].values

# Normalize the features
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

import tensorflow as tf

# Define the model architecture
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, input_shape=(16,), activation='sigmoid'),
    tf.keras.layers.Dense(7, activation='softmax')
])

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, validation_split=0.2, epochs=50, batch_size=32)

# Evaluate the model on the test data
test_loss, test_acc = model.evaluate(X_test, y_test)

print(f'Test accuracy: {test_acc:.2f}')

