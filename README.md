# Visually-impaired

First method: using tesseract

1) Change one of the png file names to coffee in the "import" directory to "coffee"
2) Run "imageprocessing.py" to be prepared to be recognised by tesseract
3) Download, install and Use tesseract application, import "final.png" and export "tesseract"
4) Run "textrecognition.py" to see the text



Second method: LSQ

Done:

LsQ.py: 		a function to compare references with the imported images using the "Least square fitting"
im_processing: 		a function to process the images with red color

    1) Choose the red color
    2) makes images blured, gray scale
    3) makes images with different qualities similar using "erosion" and "dilation"
    4) crop the images to the edge of the text for the close images
    
imageprocessing.py:	a similar function to process the images with three colors
image-test.py:		a code to test the image processing


im_processing.py:


To Do:

    1)Rotaion corrector: a function to rotate it degree by degree to obtain a better fittin
    2)Imoprting images with the new main camera (The camera which we are gonna use in the future)
    3)Try to find the best kernel parameters to obtain the best fittings in different image qualities for new camera