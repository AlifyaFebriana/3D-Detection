import os

# the directory containing the images
img_dir = "/home/junaid/alifya/Bean/3DBEAN/images" 

# the directory where you want to save the txt files
output_dir = "/home/junaid/alifya/Bean/3DBEAN/calib" 

# the content you want to write in each text file
content = "P0: 307.2000 0.000 128.000 0.000 0.000 307.2000 128.000 0.000 0.000 0.000 1.000 0.000\nR0_rect: 1.000 0.000 0.000 0.000 1.000 0.000 0.000 0.000 1.000"

# create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# iterate over all files in the directory
for filename in os.listdir(img_dir):
    # check if the file is a jpg image
    if filename.endswith(".jpg"):
        # create a new text file with the same name but different extension
        txt_filename = os.path.splitext(filename)[0] + '.txt'
        txt_path = os.path.join(output_dir, txt_filename)
        
        # write the content to the new text file
        with open(txt_path, 'w') as f:
            f.write(content)

print("Text files creation completed.")
