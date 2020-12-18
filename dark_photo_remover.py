import cv2
import os
import shutil

folder_files = os.listdir()  # get list of files in working dir
working_dir = os.path.abspath(os.getcwd())  # set working directory
new_path = os.path.join(working_dir, "dark_photos")  # set new file path

for file in folder_files:  # go through each file
    if os.path.isfile(file):  # check if 'file' is a file (not folder)
        if not file == os.path.basename(__file__):  # check if 'file' is this script
            image = cv2.imread(file)  # read file into opencv
            mean_channels = cv2.mean(image)  # get average of each RGB channel
            average_total = mean_channels[0] + mean_channels[1] + mean_channels[2]  # get average "brightness" by
            # adding all channels together
            print(average_total)  # prints the total so you can adjust parameter accordingly

            if average_total < 280:  # if average lower than certain value, move file. change this to adjust
                # "darkness" threshold

                if not os.path.exists(os.path.join(working_dir, "dark_photos")):  # check if dark_photos folder
                    # exists, if not, create it
                    os.mkdir(os.path.join(working_dir, "dark_photos"))

                shutil.move(os.path.join(working_dir, file), os.path.join(new_path, file))
    else:
        continue
