# Computer Vision:
This node is primarily based on image processing and image recognition to help dectect colored targets, objects, and borders. We will also implement machine learning for the image recognition.

## How it works
Yolo uses machine learning to identify objects in an image. Yolo can return an image with a label, confidence, and a box surrounding the object. We can use this information to detect the bin's background (White), cover (Orange), and handle (Purple) as well as the torpedo border (Red) and the octagon's background (Orange). We can also use this information to determine the position of the images to align the sub with the desired object.

![image](https://user-images.githubusercontent.com/61888693/155066634-d7d0121b-7155-466a-bfaf-e7f3ece98926.png)
![image](https://user-images.githubusercontent.com/61888693/155066686-ad0c03c1-b69b-4164-b4d5-d97817d3f3dc.png)
![image](https://user-images.githubusercontent.com/61888693/155066721-7269f4b7-7eeb-4eda-8292-5ea9f797253e.png)
![image](https://user-images.githubusercontent.com/61888693/155066821-48f6605e-77d4-4a62-b037-1ea26184dc38.png)

## How to work with the code
Use a computer with Ubuntu installed to use ROS.

Open the terminal

`git clone https://github.com/RoboSubCSULA/SeniorDesign21-22.git`

`cd computer_vision`

create a branch with `git checkout -b <branch name>`

You can now begin working on the code in your local environment

### Push your code

After you have made your changes push your code to be approved

`git add -A`

`git commit -m "brief description of the changes made"`

`git push origin`

On the github website, create a pull request and add team members to look over your code and add their approval if all is correct.

Have all required packages installed from the RoboSubCSULA README.md\

Before running any of the commands when testing the LetterA 
I. Locate the LetterA.data file within the yolov4_files folder within the catkin_ws
II. For the "names" value within the LetterA.data file change the path to your local path for LetterA.names file within the yolov4_files folder.

1. run following commands in your system's terminal:
- `cd catkin_ws`
- `catkin_make`
- `source devel/setup.bash`
- `roscore`

2. Create a new terminal and run the following commands;
- `cd catkin_ws`
- `source devel/setup.bash`
- `rosrun computer_vision cv_start.py`

alternative to step 2:
- `cd src/computer_vision/`
- `python cv_start.py`



## Testing
... How can you test the different states

## Data it publishes

Data:

This node publishes an array if mixed datatypes.

`data[0] - Object, label for the object found, string if no object is detected, will return'Null'`

`data[1] - Confidence, float, 0 - 1, 1 being absolutely certainty. If no object is detected, returns -999`

`data[2] - Vertical, int vertical distance in pixels of center of object to center of frame.
Negative number means center of object is above center of image, positive means below.
returns = 999 if no object found`

`data[3] - Horizontal, int horizontal distance in pixels of center of object to center of frame.
Negative number means center of object is left of center of image, positive means right.
returns = 999 if no object found`
