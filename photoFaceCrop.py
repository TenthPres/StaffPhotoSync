import cv2
import glob

cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

cnt = 0

files=glob.glob("rawImages/*.jpg")
for file in files:

    # Read the image
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = []
    scale = 1.6

    valid = True

    while len(faces) < 1 and valid is True:
        scale -= 0.1

        # Detect faces in the image
        try:
            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=scale,
                minNeighbors=5,
                minSize=(100, 100),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
        except:
            print "!! Could not find face in {0}.".format(file)
            valid = False

    print "Found {0} faces with scale {1}.".format(len(faces), scale)

    # Crop Padding
    padding = .2

    if len(faces) < 1:
        print "Could not find faces.".format()
        continue

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        #print x, y, w, h

        left = round(w * padding)
        right = round(w * padding)
        top = round(h * padding)
        bottom = round(h * padding)

        # Dubugging boxes
        # cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Make sure intended bounds are not outside image bounds
        # TODO rewrite this in a way that keeps things more square, but still produces a result.
        baseH, baseW, channels = image.shape
        y1 = max([0, y-top])
        y2 = min([baseH, y+h+bottom])
        x1 = max([0, x-left])
        x2 = min([baseW, x+w+right])

        newImage = image[y1:y2, x1:x2]

        print "{0}".format(file[10:])
        cv2.imwrite("cropped\{0}".format(file[10:]), newImage)
        cnt += 1
    print ''
