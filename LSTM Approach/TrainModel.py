import datetime
import numpy as np
import tensorflow as tf
from LSTM_network import createModel
from parameters import FINGER_SIZE, CHECKPOINT_PATH, LOG_PATH, BIRNN

def trainModel(input_list, label_list, num_epochs, batch_size):
    symbol_input = np.asarray(input_list, dtype=float)
    label_list = np.asarray(label_list)

    # uncomment the following line if the input is interleaved format
    # symbol_input = np.reshape(input_list, (-1, TIME_STEPS, 1))
    symbol_one_hot = np.zeros((label_list.size, FINGER_SIZE), dtype=float)
    symbol_one_hot[np.arange(label_list.size), label_list-1] = 1.0

    cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=CHECKPOINT_PATH,
                                                    save_weights_only=True,
                                                    verbose=1)

    log_dir = LOG_PATH + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

    model = createModel(BIRNN)
    model.compile(optimizer=tf.keras.optimizers.Adam(0.001),
                loss=tf.keras.losses.CategoricalCrossentropy(),
                metrics=[tf.keras.metrics.CategoricalAccuracy()])
    model.fit(symbol_input, symbol_one_hot, epochs=num_epochs, batch_size=batch_size, callbacks=[cp_callback, tensorboard_callback])
