# encoding: UTF-8

import os
import json
import pickle

paragraph_json_file = open('./paragraphs_v1.json').read()
paragraph = json.loads(paragraph_json_file)

img2paragraph = {}

for each_img in paragraph:
    image_id = each_img['image_id']
    each_paragraph = each_img['paragraph']
    sentences = each_paragraph.split('. ')
    if '' in sentences:
        sentences.remove('')
    img2paragraph[image_id] = [len(sentences), sentences]

for key, para in img2paragraph.items():
    print(key, para)

with open('img2paragraph', 'wb') as f:
    pickle.dump(img2paragraph, f)
