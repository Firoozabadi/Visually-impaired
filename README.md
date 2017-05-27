# Visually-impaired

First method: using tesseract

1) Change one of the png file names to coffee in the "import" directory to "coffee"
2) Run "imageprocessing.py" to be prepared to be recognised by tesseract
3) Use tesseract application, import "final.png" and export "tesseract"
4) Run "textrecognition.py" to see the text

Second method: LSQ

Done:

imageprocessing.py
    makes images blured, gray scale
    makes similar the images with different qualities using "erosion" and "dilation"
    crop the images to the edge of the text
Lsqversion.py
    compares references with the imported images using the "Least square fitting"


To Do:

Finding the most suitable images to use as reference
Try to find the best kernel parameters to obtain the best fittings in different image qualities
