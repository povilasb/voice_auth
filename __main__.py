
import speech_data as data
import numpy

import audio
import ml


def train(number_classes):
    model = ml.make_model(number_classes)
    batch = data.wave_batch_generator(batch_size=1000,
                                      target=data.Target.speaker)
    X, Y = next(batch)
    model.fit(X, Y, n_epoch=100, show_metric=True, snapshot_step=100)
    model.save('classifier')


def main():
    speakers = data.get_speakers()
    number_classes=len(speakers)
    print("speakers",speakers)

    model = ml.make_model(number_classes)
    model.load('classifier')

    stream = audio.Stream()
    while True:
        raw_input('press enter to record!!!')
        buff = stream.record(1.5)
        sample = audio.stream_to_ints(buff)
        label, conf = ml.predict(model, speakers, sample)
        print("predicted : result = %s  confidence = %.2f" % (label, conf))
    # gfx.plot_vector(stream_to_ints(buff))


main()
