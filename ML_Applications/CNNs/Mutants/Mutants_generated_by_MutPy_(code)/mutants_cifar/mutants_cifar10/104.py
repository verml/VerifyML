"""Runs a ResNet model on the CIFAR-10 dataset."""















from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import sys
import numpy as np
from sklearn import metrics
import pickle
import datetime

import tensorflow as tf
from tensorflow import set_random_seed


import resnet_model_VERML_basedOn_nas_fix4_deterministic as resnet_model

parser = argparse.ArgumentParser()


parser.add_argument('--data_dir', type=str, default='cifar10_data_small', help='The path to the CIFAR-10 data directory.')


parser.add_argument('--model_dir', type=str, default='cifar10_model', help='The directory where the model will be stored.')


parser.add_argument('--resnet_size', type=int, default=32, help='The size of the ResNet model to use.')


parser.add_argument('--train_epochs', type=int, default=5, help='The number of epochs to train.')


parser.add_argument('--epochs_per_eval', type=int, default=1, help='The number of epochs to run in between evaluations.')


parser.add_argument('--batch_size', type=int, default=128, help='The number of images per batch.')


parser.add_argument('--data_format', type=
str, default=None, choices=['channels_first', 'channels_last'], help='A flag to override the data format used in the model. channels_first provides a performance boost on GPU but is not always compatible with CPU. If left unspecified, the data format will be chosen automatically based on whether TensorFlow was built for CPU or GPU.')






_HEIGHT = 32
_WIDTH = 32
_DEPTH = 3
_NUM_CLASSES = 10
_NUM_DATA_FILES = 5



_WEIGHT_DECAY = 0.0002
_MOMENTUM = 0.9

_NUM_IMAGES = {'train': 5029, '': 1010}




_SHUFFLE_BUFFER = 20000

_SEED = 7

def record_dataset(filenames):
    """Returns an input pipeline Dataset from `filenames`."""
    record_bytes = _HEIGHT * _WIDTH * _DEPTH + 1
    return tf.contrib.data.FixedLengthRecordDataset(filenames, record_bytes)


def get_filenames(is_training, data_dir):
    """Returns a list of filenames."""
    data_dir = os.path.join(data_dir, 'cifar-10-batches-bin')
    
    assert os.path.exists(data_dir), 'Run cifar10_download_and_extract.py first to download and extract the CIFAR-10 data.'
    
    
    
    if is_training:
        return [
        os.path.join(data_dir, 'data_batch_%d.bin' % i) for 
        i in range(1, _NUM_DATA_FILES + 1)]
    else:
        
        return [os.path.join(data_dir, 'test_batch.bin')]


def dataset_parser(value):
    """Parse a CIFAR-10 record from value."""
    
    
    label_bytes = 1
    image_bytes = _HEIGHT * _WIDTH * _DEPTH
    record_bytes = label_bytes + image_bytes
    
    
    raw_record = tf.decode_raw(value, tf.uint8)
    
    
    label = tf.cast(raw_record[0], tf.int32)
    
    
    
    depth_major = tf.reshape(raw_record[label_bytes:record_bytes], [
    _DEPTH, _HEIGHT, _WIDTH])
    
    
    
    image = tf.cast(tf.transpose(depth_major, [1, 2, 0]), tf.float32)
    
    return (image, tf.one_hot(label, _NUM_CLASSES))


def train_preprocess_fn(image, label):
    """Preprocess a single training image of layout [height, width, depth]."""
    
    image = tf.image.resize_image_with_crop_or_pad(image, _HEIGHT + 8, _WIDTH + 8)
    
    
    image = tf.random_crop(image, [_HEIGHT, _WIDTH, _DEPTH], seed=_SEED)
    
    
    image = tf.image.random_flip_left_right(image, seed=_SEED)
    
    return (image, label)


def input_fn(is_training, data_dir, batch_size, num_epochs=1):
    """Input_fn using the contrib.data input pipeline for CIFAR-10 dataset.

  Args:
    is_training: A boolean denoting whether the input is for training.
    num_epochs: The number of epochs to repeat the dataset.

  Returns:
    A tuple of images and labels.
  """
    dataset = record_dataset(get_filenames(is_training, data_dir))
    dataset = dataset.map(dataset_parser, num_threads=1, output_buffer_size=2 * 
    batch_size)
    
    
    if is_training:
        dataset = dataset.map(train_preprocess_fn, num_threads=1, output_buffer_size=2 * 
        batch_size)
        
        
        
        dataset = dataset.shuffle(buffer_size=_SHUFFLE_BUFFER, seed=_SEED)
    
    
    dataset = dataset.map(lambda image, label: (
    tf.image.per_image_standardization(image), label), num_threads=1, output_buffer_size=2 * 
    
    batch_size)
    
    dataset = dataset.repeat(num_epochs)
    
    
    
    iterator = dataset.batch(batch_size).make_one_shot_iterator()
    (images, labels) = iterator.get_next()
    
    return (images, labels)


def cifar10_model_fn(features, labels, mode, params):
    """Model function for CIFAR-10."""
    tf.summary.image('images', features, max_outputs=6)
    
    network = resnet_model.cifar10_resnet_v2_generator(
    params['resnet_size'], _NUM_CLASSES, params['data_format'])
    
    inputs = tf.reshape(features, [(-1), _HEIGHT, _WIDTH, _DEPTH])
    logits = network(inputs, mode == tf.estimator.ModeKeys.TRAIN)
    
    predictions = {'classes': 
    tf.argmax(logits, axis=1), 'probabilities': 
    tf.nn.softmax(logits, name='softmax_tensor')}
    
    
    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions)
    
    
    cross_entropy = tf.losses.softmax_cross_entropy(logits=
    logits, onehot_labels=labels)
    
    
    tf.identity(cross_entropy, name='cross_entropy')
    tf.summary.scalar('cross_entropy', cross_entropy)
    
    
    loss = cross_entropy + _WEIGHT_DECAY * tf.add_n([
    tf.nn.l2_loss(v) for v in tf.trainable_variables()])
    
    if mode == tf.estimator.ModeKeys.TRAIN:
        
        
        initial_learning_rate = 0.1 * params['batch_size'] / 128
        batches_per_epoch = _NUM_IMAGES['train'] / params['batch_size']
        global_step = tf.train.get_or_create_global_step()
        
        
        boundaries = [int(batches_per_epoch * epoch) for epoch in [100, 150, 200]]
        values = [initial_learning_rate * decay for decay in [1, 0.1, 0.01, 0.001]]
        learning_rate = tf.train.piecewise_constant(
        tf.cast(global_step, tf.int32), boundaries, values)
        
        
        tf.identity(learning_rate, name='learning_rate')
        tf.summary.scalar('learning_rate', learning_rate)
        
        optimizer = tf.train.MomentumOptimizer(learning_rate=
        learning_rate, momentum=
        _MOMENTUM)
        
        
        update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS)
        with tf.control_dependencies(update_ops):
            train_op = optimizer.minimize(loss, global_step)
    else:
        train_op = None
    
    accuracy = tf.metrics.accuracy(
    tf.argmax(labels, axis=1), predictions['classes'])
    metrics = {'accuracy': accuracy}
    
    
    tf.identity(accuracy[1], name='train_accuracy')
    tf.summary.scalar('train_accuracy', accuracy[1])
    
    return tf.estimator.EstimatorSpec(mode=
    mode, predictions=
    predictions, loss=
    loss, train_op=
    train_op, eval_metric_ops=
    metrics)


def main(unused_argv):
    
    os.environ['TF_ENABLE_WINOGRAD_NONFUSED'] = '1'
    
    
    
    run_config = tf.estimator.RunConfig().replace(tf_random_seed=_SEED, save_checkpoints_secs=1000000000.0)
    cifar_classifier = tf.estimator.Estimator(model_fn=
    cifar10_model_fn, model_dir=FLAGS.model_dir, config=run_config, params={'resnet_size': 
    
    FLAGS.resnet_size, 'data_format': 
    FLAGS.data_format, 'batch_size': 
    FLAGS.batch_size})
    
    
    for _ in range(FLAGS.train_epochs // FLAGS.epochs_per_eval):
        tensors_to_log = {'learning_rate': 'learning_rate', 'cross_entropy': 'cross_entropy', 'train_accuracy': 'train_accuracy'}
        
        
        
        
        
        logging_hook = tf.train.LoggingTensorHook(tensors=
        tensors_to_log, every_n_iter=100)
        
        cifar_classifier.train(input_fn=lambda : 
        input_fn(True, 
        FLAGS.data_dir, FLAGS.batch_size, FLAGS.epochs_per_eval), hooks=[
        logging_hook])
        
        
        eval_results = cifar_classifier.evaluate(input_fn=lambda : 
        input_fn(False, FLAGS.data_dir, FLAGS.batch_size))
        print(eval_results)
    
    pred_results = cifar_classifier.predict(input_fn=lambda : input_fn(False, FLAGS.data_dir, FLAGS.batch_size))
    
    pred_classes = [i['classes'] for i in pred_results]
    (images, labels) = input_fn(False, FLAGS.data_dir, _NUM_IMAGES['validation'])
    orig_classes = labels.eval(session=tf.Session())
    confMatrix = metrics.confusion_matrix(np.argmax(orig_classes, axis=1), pred_classes)
    outputData = {'data_array': confMatrix}
    with open('output.pkl', 'wb') as outputFile:
        pickle.dump(outputData, outputFile)
    print(confMatrix)
    print(eval_results)
    print(datetime.datetime.now())


if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    (FLAGS, unparsed) = parser.parse_known_args()
    tf.app.run(argv=[sys.argv[0]] + unparsed)