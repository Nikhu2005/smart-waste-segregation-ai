import tensorflow as tf
from tensorflow.keras import layers, models

# Load dataset
data = tf.keras.preprocessing.image_dataset_from_directory(
    "dataset",
    image_size=(224, 224),
    batch_size=32
)

class_names = data.class_names
print("Classes:", class_names)

# Normalize data
data = data.map(lambda x, y: (x/255.0, y))

# Build model
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(224,224,3)),
    layers.MaxPooling2D(),

    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(),

    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(len(class_names), activation='softmax')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train model
model.fit(data, epochs=5)

# Save model
model.save("model.h5")

print("✅ Training Done!")