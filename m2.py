import tensorflow as tf
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.applications import ResNet152
from tensorflow.keras import layers, models, optimizers, regularizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint

# ✅ Ensure GPU Memory Growth
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

# ✅ Directories
train_dir = r"/home/sanjana-r/roop/Dataset/train"
val_dir = r"/home/sanjana-r/roop/Dataset/val"
test_dir = r"/home/sanjana-r/roop/Dataset/test"  # Labeled test data

# ✅ Image Preprocessing with Augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest"
)
val_test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary'
)

val_generator = val_test_datagen.flow_from_directory(
    val_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary'
)

test_generator = val_test_datagen.flow_from_directory(
    test_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',  # Now labeled
    shuffle=False  # Ensure filenames match predictions
)

# ✅ Load Pretrained ResNet152 Model
base_model = ResNet152(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model.trainable = True  # Enable fine-tuning

# Unfreeze only the last few layers for fine-tuning
for layer in base_model.layers[:-30]:
    layer.trainable = False

# ✅ Build the Updated Model
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),

    layers.Dense(512, activation='relu', kernel_regularizer=regularizers.l2(0.0001)),
    layers.BatchNormalization(),
    layers.Dropout(0.3),  # Dropout added

    layers.Dense(256, activation='relu', kernel_regularizer=regularizers.l2(0.0001)),
    layers.BatchNormalization(),
    layers.Dropout(0.4),  # Dropout added

    layers.Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.0001)),
    layers.BatchNormalization(),
    layers.Dropout(0.4),  # Dropout added

    layers.Dense(1, activation='sigmoid')  # Binary classification
])

# ✅ Compile Model with Faster Convergence
optimizer = optimizers.AdamW(learning_rate=0.0005, weight_decay=0.0001)  # AdamW with weight decay
model.compile(optimizer=optimizer,
              loss='binary_crossentropy',
              metrics=['accuracy'])

# ✅ Callbacks for Faster Training
early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
lr_scheduler = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=2, verbose=1)
checkpoint = ModelCheckpoint('optimized_resnet152_model.h5', monitor='val_loss', save_best_only=True)

# ✅ Resume Training from Saved Model
if os.path.exists("resnet152_binary_classification_model.h5"):
    print("Loading existing model...")
    model.load_weights("resnet152_binary_classification_model.h5")

# ✅ Train the Model
history = model.fit(
    train_generator,
    epochs=3,
    validation_data=val_generator,
    callbacks=[early_stopping, lr_scheduler, checkpoint]
)

# ✅ Save the Optimized Model
model.save('optimized_resnet152_model.h5')
print("Optimized Model saved successfully!")

# ✅ Evaluate Model
test_loss, test_acc = model.evaluate(test_generator, verbose=2)
print(f'Test accuracy: {test_acc}')

train_loss, train_acc = model.evaluate(train_generator, verbose=2)
print(f'Training accuracy: {train_acc}')

# ✅ Plot Training & Validation Accuracy
plt.plot(history.history['accuracy'], label='Training accuracy')
plt.plot(history.history['val_accuracy'], label='Validation accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')
plt.show()

# ✅ Predict on Labeled Test Data
test_preds = model.predict(test_generator)
predicted_classes = (test_preds > 0.5).astype(int).flatten()
true_classes = test_generator.classes
class_labels = list(test_generator.class_indices.keys())

# ✅ Save Test Predictions to CSV
test_filenames = test_generator.filenames  # Get filenames from test set
test_results = pd.DataFrame({"filename": test_filenames, "predicted_label": predicted_classes})
test_results.to_csv("optimized_test_predictions.csv", index=False)  
print("✅ Test predictions saved as optimized_test_predictions.csv")

# ✅ Save Classification Report as a Text File
report = classification_report(true_classes, predicted_classes, target_names=class_labels)
with open("optimized_classification_report.txt", "w") as f:
    f.write(report + "\n")
print("✅ Classification report saved as optimized_classification_report.txt")

# ✅ Save Confusion Matrix as CSV
conf_matrix = confusion_matrix(true_classes, predicted_classes)
conf_matrix_df = pd.DataFrame(conf_matrix, index=class_labels, columns=class_labels)
conf_matrix_df.to_csv("optimized_confusion_matrix.csv")
print("✅ Confusion matrix saved as optimized_confusion_matrix.csv")

