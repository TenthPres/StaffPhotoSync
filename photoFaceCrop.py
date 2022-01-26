import cv2
import glob
import numpy

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
                minSize=(50, 50),
                maxSize=(4000, 4000),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
        except:
            print "!! Could not find face in {0}.".format(file)
            valid = False

    print "Found {0} faces.".format(len(faces))

    # Crop Padding
    padding = .2

    if len(faces) < 1:
        print "Could not find faces.".format()
        continue

    # Draw a rectangle around the faces
    for (fx, fy, fw, fh) in faces:
        #print x, y, w, h

        print "width: {0}.".format(fw)

        # half height and width
        fw2 = fw / 2
        fh2 = fh / 2

        # shifting these points so the X and Y is the center of the face
        fx += fw2
        fy += fh2

        # Debugging markers
        # cv2.rectangle(image, (fx - fw2, fy - fh2), (fx + fw2, fy + fh2), (0, 255, 0), 2)
        # image = cv2.circle(image, (fx, fy), 2, (255, 0, 0), 3)

        # face size.  Used for scaling.
        padding = max(fw, fh) * 0.9

        baseH, baseW, n = image.shape
        hwRatio = 17.0/12.0
        y1 = int(fy - padding * (hwRatio / 3 * 2))
        y2 = int(fy + padding * (hwRatio / 3 * 4))
        x1 = int(fx - padding)
        x2 = int(fx + padding)

        print "ratio: {}".format(hwRatio)

        white = numpy.full((y2-y1, x2-x1, 3), (255, 255, 255), numpy.uint8)
        newImage = white
        print '{} {} {} {}'.format(x1, x2, y1, y2)

        yOff = 0
        if y2 > baseH:
            print "Crop extends beyond source bounds by {} rows.".format(y2 - baseH)
            yOff = y2 - baseH
            y2 = baseH

        if y1 < 0:
            print "Crop extends above source bounds by {} rows.".format(-y1)
            yOff -= y1
            y1 = 0

        newImage[yOff:y2 - y1 + yOff, 0:x2 - x1] = image[y1:y2, x1:x2]

        newImage = cv2.resize(newImage, (200, int(200.0 * hwRatio)))

        print "{0}".format(file[10:])
        cv2.imwrite("croppedLarge\{0}".format(file[10:]), newImage)

        # ################### Small Image ###################

        # face size.  Used for scaling.
        padding = max(fw, fh) * .7

        baseH, baseW, n = image.shape
        y1 = int(fy - padding)
        y2 = int(fy + padding)
        x1 = int(fx - padding)
        x2 = int(fx + padding)

        white = numpy.full((y2-y1, x2-x1, 3), (255, 255, 255), numpy.uint8)
        newImage = white
        print '{} {} {} {}'.format(x1, x2, y1, y2)

        if y2 > baseH:
            print "Crop extends beyond source bounds by {} rows.".format(y2 - baseH)
            y2 = baseH

        yOff = 0
        if y1 < 0:
            print "Crop extends above source bounds by {} rows.".format(-y1)
            yOff = -y1
            y1 = 0

        newImage[yOff:y2 - y1 + yOff, 0:x2 - x1] = image[y1:y2, x1:x2]

        newImage = cv2.resize(newImage, (150, 150))  # need to maintain 1:1 ratio

        fileName = file[10:].split(' ', 1)
        fileName = (fileName[0][0] + fileName[1]).lower()
        print "{0}".format(fileName)
        cv2.imwrite("croppedSmall\{0}".format(fileName), newImage)

        cnt += 1

        break

    print ''  # blank line between outputs.
