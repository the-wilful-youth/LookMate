import tensorflow as tf
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

model_dir = "/Users/Anurag/Anurag/Projects/LookMate/model"
models = {
    "men": "men.keras",
    "female": "Female.h5",
    "gender": "gender.keras"
}

for name, filename in models.items():
    path = os.path.join(model_dir, filename)
    print(f"\n--- Inspecting {name} model ({filename}) ---")
    try:
        model = tf.keras.models.load_model(path)
        print(f"Input Shape: {model.input_shape}")
        print(f"Output Shape: {model.output_shape}")
        # Try to guess classes from last layer if possible, usually not directly stored unless in config
        # But we can infer from output size.
    except Exception as e:
        print(f"Error loading {filename}: {e}")
