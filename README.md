# Image-Preprocessor
Initial Draft for Image Pre-processor. This pre-processing script uses Otsu's Binarization in order to improve extraction of OCR using Tesseract's t4 Engine

# Flow of Code
1. Looping Through files in an input folder
2. Conversion of As-In input image to grayscale
3. Conversion to binarized image using Otsu's Binarization Function - Creates it's own subfolder within input directory
4. Stores binarized files in output path

# Inputs
inputpath = 'C:/Users/Juan/Desktop/OpenCV/Sample Documents/Images'
bzpath = 'C:/Users/Juan/Desktop/OpenCV/Binarized'

# Execute
binarizer(inputpath, bzpath)
