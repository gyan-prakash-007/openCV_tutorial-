import cv2 as cv

# ---------- Reading Images ----------
img = cv.imread('photos/images.jpeg')#Loads the image into memory

# Returns:

# NumPy array if successful

# None if path is wrong

if img is None:
    print("❌ Image not found")
else:
    cv.imshow('Image', img)#Creates a window named "Image".Displays the image


    cv.waitKey(0)#0 → wait forever .Image stays open until any key is pressed
    cv.destroyAllWindows()#Closes image window cleanly .Frees memory
