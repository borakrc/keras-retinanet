import keras


class RunFunction(keras.callbacks.Callback):

    def __init__(self, function):
        self.function       = function

        super(RunFunction, self).__init__()

    def on_epoch_end(self, epoch, logs=None):
        logs = logs or {}

        # run function
        self.function()
