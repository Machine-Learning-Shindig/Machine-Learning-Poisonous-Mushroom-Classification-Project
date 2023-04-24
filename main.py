import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
import tensorflow_datasets as tfds
import pathlib
from datetime import datetime

def main():
    batch_size = 48
    img_height = 277
    img_width = 277

    archive = "dataset"
    data_dir = pathlib.Path(archive).with_suffix('')

    train_ds = tf.keras.utils.image_dataset_from_directory(data_dir, validation_split=.2, subset="training", seed=123, image_size=(img_height, img_width), batch_size=batch_size)
    val_ds = tf.keras.utils.image_dataset_from_directory(data_dir, validation_split=.2, subset="training", seed=123, image_size=(img_height, img_width), batch_size=batch_size)
    
    AUTOTUNE = tf.data.AUTOTUNE
    train_ds = train_ds.cache().prefetch(buffer_size=AUTOTUNE)
    val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)


    model = tf.keras.Sequential([
        tf.keras.layers.Rescaling(1./255),
        tf.keras.layers.Dense(100, activation="relu"),
        tf.keras.layers.Dense(1)
    ])

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=100
    )

    now = datetime.now()
    model.save("models/mushroom_classifier_" + now.strftime("%m_%d_%Y"))

if __name__ == "__main__":
    main()