<head>
  <h1 align = "center"><b>Building Defect Detector</b></h1><br>
</head>
<p align = "center">
  This is a application that makes use of image classification in order to <b>detect building defects</b> through a <b>live camera</b>. Transfer
  learning is used for the deep learning model.
  
  &nbsp;
  <br>
  <p align = "center">
  <img src = "Project logo.png" width = 30%>    
</p>
  
## About the project
  This project in its core is a <b>image classification model</b> that can detect defects in a building. These defects are <b>Roof defect, cracks defect and flakes on surfaces.</b> In order for users to use the model easily, I have incorporated the model into a application with a GUI that once excecuted, runs on the local network of the device. 
  
  It has an option to <b>open the webcam</b> of the user's device. This in turn opens a new window showing the live camera feedback. The predictions can also be seen live on that same window. In other words, the user can see live prediction of the shown defects on the video screen itself.
  
  
  ## Needed python packages
  
  - Tensorflow (latest version 2.7)
  - Flask
  - OpenCV 
  - Numpy
  - Matplotlib
