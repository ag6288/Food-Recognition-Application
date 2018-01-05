import tensorflow as tf
import boto3
import os
import sys

os.system("rm *.png")

image_path = sys.argv[1]

s3 = boto3.resource('s3',
    aws_access_key_id = '',
    aws_secret_access_key = '')

s3.Bucket('').download_file(image_path, image_path)

image_data = tf.gfile.FastGFile(image_path, 'rb').read()

label_lines = [line.rstrip() for line 
                   in tf.gfile.GFile("labels.txt")]

with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    
    predictions = sess.run(softmax_tensor, \
             {'DecodeJpeg/contents:0': image_data})
    
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    
    result = label_lines[top_k[0]]
    print "result = ", result
