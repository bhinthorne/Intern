import csv

#classname is the name of the class this file contains, for ex: 'thumbs down'
def make_lst(classname, read_file_name, write_file_name):
    tab = '\t'
    #Open the file to read
    with open(read_file_name) as _file:
        reader = csv.DictReader(_file)
        img_id = 0
        boxes_per_img = []
        count = 0
        #iterate over each row in the file
        for row in reader:
            #Collect the bounding box info for the current row
            label = row['class']
            if label == classname:
                label = '0'
            xmin = row['xmin']
            ymin = row['ymin']
            xmax = row['xmax']
            ymax = row['ymax']
            box_info = label + tab + xmin + tab + ymin + tab + xmax + tab + ymax + tab
            ## If its the first row, or this row is labeling the same image
            ## append to the list containing bounding box info for each image
            if(count == 0 or prev_row['filename'] == row['filename']):
                count += 1
                boxes_per_img.append(box_info)
            ##Otherwise, write the line for the image we've collected all data for
            else:
                #This is all the header stuff. A = 4 (length of header). B = 5 is length of [id, xmin, ymin, xmax, ymax]
                line = str(img_id) + tab + str(4) + tab + str(5) + tab + prev_row['width'] + tab + prev_row['height'] + tab
                for box in boxes_per_img:
                    line += box
                line += prev_row['filename'] + '\n'
                with open(write_file_name, 'a') as the_file:
                    the_file.write(line)
                img_id += 1
                boxes_per_img = [box_info]
            prev_row = row
        
        ##Now we are out of the loop but did not have a chance to print the last line
        line = str(img_id) + tab + str(4) + tab + str(5) + tab + prev_row['width'] + tab + prev_row['height'] + tab
        #If this is a different image then boxes_per_img should only contain info for the last row
        #If it is the same, then it should still contain info for everything, including this row
        for box in boxes_per_img:
            line += box
        line += row['filename'] + '\n'
        with open(write_file_name, 'a') as the_file:
            the_file.write(line)
            
make_lst('thumbs down', 'test_labels.csv', 'mydata_test.lst')
make_lst('thumbs down', 'train_labels.csv', 'mydata_train.lst')

