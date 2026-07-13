# Chapter 24 Natural Language Processing

<!-- tabs:start -->

#### **Tiếng Việt**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters_Vi3/Chapter_24_Natural%20Language%20Processing.pdf" width="100%" height="100%"></iframe>
</div>

#### **Tiếng Anh**
<div class="pdf-container">
  <iframe src="TaiLieu/ebooks_Chapters/Chapter_24_Natural%20Language%20Processing.pdf" width="100%" height="100%"></iframe>
</div>

#### **Slide**
*(Chưa có slide)*

#### **Trắc nghiệm**
*(Chưa có bài tập trắc nghiệm)*

#### **Pseudocode**
*(Không có mã giả cho chương này trong thư viện)*

*(Thư mục chứa mã giả cho các thuật toán trong sách: `codeAndExercises/aima-pseudocode-master/md`)*

#### **Python**
- [Nlp](codeAndExercises/aima-python-master/notebooks/nlp.ipynb)
- [Nlp (Python File)](codeAndExercises/aima-python-master/notebooks/nlp.py)
- [Nlp Apps](codeAndExercises/aima-python-master/notebooks/nlp_apps.ipynb)
- [Nlp Apps (Python File)](codeAndExercises/aima-python-master/notebooks/nlp_apps.py)
- [Text](codeAndExercises/aima-python-master/notebooks/text.ipynb)
- [Text (Python File)](codeAndExercises/aima-python-master/notebooks/text.py)


#### **Bài tập**

##### Bài tập 24.1

In the shadow of a tree with a dense, leafy canopy, one sees a number of
light spots. Surprisingly, they all appear to be circular. Why? After
all, the gaps between the leaves through which the sun shines are not
likely to be circular.


---

##### Bài tập 24.2

Consider a picture of a white sphere floating in front of a black
backdrop. The image curve separating white pixels from black pixels is
sometimes called the “outline” of the sphere. Show that the outline of a
sphere, viewed in a perspective camera, can be an ellipse. Why do
spheres not look like ellipses to you?


---

##### Bài tập 24.3

Consider an infinitely long cylinder of radius $r$ oriented with its
axis along the $y$-axis. The cylinder has a Lambertian surface and is
viewed by a camera along the positive $z$-axis. What will you expect to
see in the image if the cylinder is illuminated by a point source at
infinity located on the positive $x$-axis? Draw the contours of constant
brightness in the projected image. Are the contours of equal brightness
uniformly spaced?


---

##### Bài tập 24.4

Edges in an image can correspond to a variety of events in a scene.
Consider Figure <a class="insideBookFigRef" target="_blank" href="https://aimacode.github.io/aima-exercises/figures/illuminationfigure.png">illuminationfigure</a>
(page <a class="pageRef" title="" href="#">illuminationfigure</a>, and assume that it is a picture of a real
three-dimensional scene. Identify ten different brightness edges in the
image, and for each, state whether it corresponds to a discontinuity in
(a) depth, (b) surface orientation, (c) reflectance, or (d)
illumination.


---

##### Bài tập 24.5

A stereoscopic system is being contemplated for terrain mapping. It will
consist of two CCD cameras, each having ${512}\times {512}$ pixels on a
10 cm $\times$ 10 cm square sensor. The lenses to be used have a focal
length of 16 cm, with the focus fixed at infinity. For corresponding
points ($u_1,v_1$) in the left image and ($u_2,v_2$) in the right image,
$v_1=v_2$ because the $x$-axes in the two image planes are parallel to
the epipolar lines—the lines from the object to the camera. The optical
axes of the two cameras are parallel. The baseline between the cameras
is 1 meter.<br>

1.  If the nearest distance to be measured is 16 meters, what is the
    largest disparity that will occur (in pixels)?<br>

2.  What is the distance resolution at 16 meters, due to the pixel
    spacing?<br>

3.  What distance corresponds to a disparity of one pixel?<br>


---

##### Bài tập 24.6

Which of the following are true, and which are false?<br>

1.  Finding corresponding points in stereo images is the easiest phase
    of the stereo depth-finding process.<br>

2.  Shape-from-texture can be done by projecting a grid of light-stripes
    onto the scene.<br>

3.  Lines with equal lengths in the scene always project to equal
    lengths in the image.<br>

4.  Straight lines in the image necessarily correspond to straight lines
    in the scene.


---

##### Bài tập 24.7

Which of the following are true, and which are false?<br>

1.  Finding corresponding points in stereo images is the easiest phase
    of the stereo depth-finding process.<br>

2.  In stereo views of the same scene, greater accuracy is obtained in
    the depth calculations if the two camera positions are
    farther apart.<br>

3.  Lines with equal lengths in the scene always project to equal
    lengths in the image.<br>

4.  Straight lines in the image necessarily correspond to straight lines
    in the scene.<br>



    <figure>
      <img src="https://aimacode.github.io/aima-exercises/figures/bottle-stereo.svg" alt="bottle-figure" id="bottle-figure" style="width:100%">
      <figcaption><center><b>Top view of
      a two-camera vision system observing a bottle with a wall behind it.</b></center></figcaption>
    </figure>


---

##### Bài tập 24.8

(Courtesy of Pietro Perona.) Figure <a class="insideExercisesFigRef"  href="#bottle-figure">bottle-figure</a> shows
two cameras at X and Y observing a scene. Draw the image seen at each
camera, assuming that all named points are in the same horizontal plane.
What can be concluded from these two images about the relative distances
of points A, B, C, D, and E from the camera baseline, and on what basis?


---


<!-- tabs:end -->
