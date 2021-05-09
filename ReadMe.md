<h1>Image Processing Examples for Computer Vision</h1>

<p>This image processing repository includes examples of filtering images using the Canny Filter, high and low pass filters, and the Hough Transform. It also includes an image segmentation example using k-means clustering and a blue screen example using thresholding.</p>

<h1>Image Filtering</h1>
<p>This repository contains three jupyter notebooks for image filtering using the open cv library.</p>

<h3>Canny Filter</h3>
<p>The Canny Filter can be used for edge detection.</p>
<p>Original Image</p>
<img src="https://user-images.githubusercontent.com/17497237/117586814-8d08d680-b0e8-11eb-945d-46838034eb0e.png" height="250px">
<p>After Canny Filter applied</p>
<img src="https://user-images.githubusercontent.com/17497237/117586841-b295e000-b0e8-11eb-8b0f-90e9e59c8f2f.png" height="250px">


<h3>High and Low Pass Filters</h3>
<p>High pass filters are used to sharpen an image, while low pass filters are used to blur images.</p>

<p>Original Image</p>
<img src="https://user-images.githubusercontent.com/17497237/117587044-f5a48300-b0e9-11eb-975e-22eee3b145b4.png" height="250px">

<p>Low Pass Filter (Blur)</p>
<img src="https://user-images.githubusercontent.com/17497237/117587055-048b3580-b0ea-11eb-9bb8-8ffd4e2ca701.png" height="250px">

<p>High Pass Filter (Sharpen)</p>
<img src="https://user-images.githubusercontent.com/17497237/117587076-18369c00-b0ea-11eb-8d2e-81f3240b2453.png" height="250px">



<h3>Hough Transform</h3>

<p>The Hough Transform is used to identify lines in images. In the image below, the lines identified by the algorithm are highlighted in red. The outline of the TV was successfully identified.</p>

<p>Original Image</p>
<img src="https://user-images.githubusercontent.com/17497237/117586872-ee30aa00-b0e8-11eb-90e0-bd1a0626b6e0.png" height="250px">

<p>After Hough Transform</p>
<img src="https://user-images.githubusercontent.com/17497237/117586877-f5f04e80-b0e8-11eb-8651-1e52fe39aab6.png" height="250px">

<h1>Blue Screen</h1>
<p>When something is captured in front of a blue screen in an image, a new background can be substituted in for the blue screen background using thresholding to identify the blue pixels and remove them. The created mask can then be used to remove the item from the new background image, and the two images can be combined.</p>

<p>Original Image</p>
<img src="https://user-images.githubusercontent.com/17497237/117587439-f807dc80-b0eb-11eb-8022-a4e1d3e9d4d0.png" height="250px">

<p>New Background</p>
<img src="https://user-images.githubusercontent.com/17497237/117587455-0b1aac80-b0ec-11eb-8346-2591d80befeb.png" height="250px">

<p>Final Image</p>
<img src="https://user-images.githubusercontent.com/17497237/117587463-153cab00-b0ec-11eb-990a-8a8691f73e60.png" height="250px">



<h1>Image Segmentation</h1>
<p>This example shows image segmentation using k-means clustering with k=3.</p>
<p>Original Image (Aerial Photo)</p>
<img src="https://user-images.githubusercontent.com/17497237/117587508-51700b80-b0ec-11eb-80a5-76ca18a8a807.png" height="250px">

<p>Segmented Image (One cluster is highlighted in pink)</p>
<img src="https://user-images.githubusercontent.com/17497237/117587523-5df46400-b0ec-11eb-9bc1-0f4b63a62d31.png" height="250px">

