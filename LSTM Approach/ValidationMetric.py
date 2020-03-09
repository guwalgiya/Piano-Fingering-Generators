import tensorflow as tf
from tensorflow.keras import layers, callbacks
import EvaluateVectorPhrase
from TestVectorModel import testVecModel
class IntervalEvaluation(callbacks.Callback):
    def __init__(self, input_list, label_list):
        super(callbacks.Callback, self).__init__()
        self.input_list = input_list
        self.label_list = label_list

    def on_epoch_end(self, epoch, logs=None):
        testVecModel(self.input_list, self.label_list, self.model)