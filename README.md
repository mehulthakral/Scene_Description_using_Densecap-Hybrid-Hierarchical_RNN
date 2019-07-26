# Scene_Description_using_Densecap-Hybrid-Hierarchical_RNN
##Introduction
Implementation of the paper https://drive.google.com/file/d/1d2w3wIOto4M5VWbkHSKyw8u2DLI39a2y/view?usp=sharing

##Step 1
Download the VisualGenome dataset, we get the two files: VG_100K, VG_100K_2. According to the paper, we download the training, val and test splits json files. These three json files save the image names of train, validation, test data.

Running the script:

$ python split_dataset
We will get images from [VisualGenome dataset] which the authors used in the paper.

##Step 2 Run the scripts:

$ python get_imgs_train_path.py
$ python get_imgs_val_path.py
$ python get_imgs_test_path.py
We will get three txt files: imgs_train_path.txt, imgs_val_path.txt, imgs_test_path.txt. They save the train, val, test images path.

After this, we use dense caption to extract features. Deploy the running environment follow by densecap step by step.

Run the script:

$ ./download_pretrained_model.sh
$ th extract_features.lua -boxes_per_image 50 -max_images -1 -input_txt imgs_train_path.txt \
                          -output_h5 ./data/im2p_train_output.h5 -gpu 0 -use_cudnn 1
We should download the pre-trained model: densecap-pretrained-vgg16.t7. Then, according to the paper, we extract 50 boxes from each image.

Also, don't forget extract val images and test images features:

$ th extract_features.lua -boxes_per_image 50 -max_images -1 -input_txt imgs_val_path.txt \
                          -output_h5 ./data/im2p_val_output.h5 -gpu 0 -use_cudnn 1
                          
$ th extract_features.lua -boxes_per_image 50 -max_images -1 -input_txt imgs_test_path.txt \
                          -output_h5 ./data/im2p_test_output.h5 -gpu 0 -use_cudnn 1
##Step 3
Run the script:

$ python parse_json.py
In this step, we process the paragraphs_v1.json file for training and testing. We get the img2paragraph file in the ./data directory. Its structure is like this: img2paragraph

##Step 4
Finally, we can train and test model, in the jupyter notebook using Present-5pmJuly2_Latest_WithScope.ipynb:

-For training: run train()
-For testing: run test() 
