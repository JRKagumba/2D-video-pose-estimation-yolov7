import math
import cv2
import numpy as np

from PIL import ImageFont, ImageDraw, Image


def findAngle(image, kpts, p1,p2,p3, draw= True):
    """
    Takes three points and returns the angle between them
    """
    coord = []
    no_kpt = len(kpts)//3
    for i in range(no_kpt):
        cx,cy = kpts[3*i], kpts[3*i +1]
        conf = kpts[3*i +2]
        coord.append([i, cx,cy, conf])

    points = (p1,p2,p3)

    # =3.1=Get landmarks========
    x1,y1 = coord[p1][1:3]
    x2,y2 = coord[p2][1:3]
    x3,y3 = coord[p3][1:3]

    # =3.2=Calculate the Angle========
    angle = math.degrees(math.atan2(y3-y2,x3-x2) - math.atan2(y1-y2, x1-x2))

    if angle < 0:
        angle += 360

    # =3.3=Draw Coordinates========
    if draw:
        cv2.line(image, (int(x1),int(y1)),(int(x2), int(y2)),(255,255,255),3 )
        cv2.line(image, (int(x3),int(y3)),(int(x2), int(y2)),(255,255,255),3 )

        cv2.circle(image, (int(x1),int(y1)),  10, (255,255,255),cv2.FILLED)
        cv2.circle(image, (int(x1), int(y1)), 20, (235, 235, 235), 5)
        cv2.circle(image, (int(x1), int(y1)), 10, (255, 255, 255), cv2.FILLED)
        cv2.circle(image, (int(x1), int(y1)), 20, (235, 235, 235), 5)
        cv2.circle(image, (int(x1), int(y1)), 10, (255, 255, 255), cv2.FILLED)
        cv2.circle(image, (int(x1), int(y1)), 20, (235, 235, 235), 5)

    return int(angle)


def rename_this_function(output):
    """
    Goal of this function:
    Take in an out

    """

    bcount = 0
    direction = 0


    fontpath = "sfpro.ttf"
    font = ImageFont.truetype(fontpath, 32)
    font1 = ImageFont.truetype(fontpath, 160)


        for idx in range(output.shape[0]):
            kpts = output[idx, 7:].T
            # Right arm =(5,7,9), left arm = (6,8,10)
            # set draw=True to draw the arm keypoints.
            angle = findAngle(img, kpts, 5, 7, 9, draw=False)
            percentage = np.interp(angle, (10, 150), (100, 0))
            bar = np.interp(angle, (20, 150), (200, fh-100))

            color = (254, 118, 136)
            # check for the bicep curls
            if percentage == 100:
                if direction == 0:
                    bcount += 0.5
                    direction = 1
            if percentage == 0:
                if direction == 1:
                    bcount += 0.5
                    direction = 0

            # draw Bar and counter
            cv2.line(img, (100, 200), (100, fh-100),
                        (255, 255, 255), 30)
            cv2.line(img, (100, int(bar)),
                        (100, fh-100), color, 30)

            if (int(percentage) < 10):
                cv2.line(img, (155, int(bar)),
                            (190, int(bar)), (254, 118, 136), 40)
            elif (int(percentage) >= 10 and (int(percentage) < 100)):
                cv2.line(img, (155, int(bar)),
                            (200, int(bar)), (254, 118, 136), 40)
            else:
                cv2.line(img, (155, int(bar)),
                            (210, int(bar)), (254, 118, 136), 40)

            im = Image.fromarray(img)
            draw = ImageDraw.Draw(im)
            draw.rounded_rectangle((fw-280, (fh//2)-100, fw-80, (fh//2)+100), fill=color,
                                    radius=40)

            draw.text(
                (145, int(bar)-17), f"{int(percentage)}%", font=font, fill=(255, 255, 255))
            draw.text(
                (fw-228, (fh//2)-101), f"{int(bcount)}", font=font1, fill=(255, 255, 255))
            img = np.array(im)