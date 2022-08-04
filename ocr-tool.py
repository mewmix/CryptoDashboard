import easyocr 
import os 
import csv

reader = easyocr.Reader(['en'], gpu=False)
## use OCR to read the text from all images in a folder, then output results to csv.
for files in os.listdir("/home/ubuntu/Desktop/OCR/images"):
    if files.endswith(".jpg"):
        text = reader.read_text("/home/ubuntu/Desktop/OCR/images/" + files)
        print(text)
        with open('/home/ubuntu/Desktop/OCR/results.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([files, text])
        csvfile.close()
    else:
        continue



