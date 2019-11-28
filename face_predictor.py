import dlib
from skimage import io

detector = dlib.get_frontal_face_detector()

img = io.imread("./image.jpg")

win = dlib.image_window()
win.set_image(img)

faces = detector(img, 1)
print(type(faces[0]), '\n')

print("Number of faces detected： ", len(faces))

for i, d in enumerate(faces):
    print("face_tiles：", i+1,
          "[[", d.left(), ",", d.right(), ") (", d.top(), ",", d.bottom()), "]]"

win.add_overlay(faces)
