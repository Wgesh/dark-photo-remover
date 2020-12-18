import cv2
import os
import shutil

folder_files = os.listdir()  # get list of files in working dir
new_path = os.path.dirname(__file__) + "/dark_photos"  # set the new file path

for file in folder_files:  # go through each file
    if os.path.isfile(file):  # check if 'file' is a file (not folder)
        if not file == os.path.basename(__file__):  # check if 'file' is this script
            image = cv2.imread(file)  # read the file into opencv
            mean_channels = cv2.mean(image)  # get the average of each RGB channel
            average_total = mean_channels[0] + mean_channels[1] + mean_channels[2]  # get average "brightness" by
            # adding all the channels together
            if average_total < 150:  # if the average is lower than a certain value move the file. change this to
                # adjust how dark you want images to be defined "dark"
                print(average_total)
                # shutil.move(os.path.dirname(__file__) + '/' + file, new_path)

    else:
        continue
