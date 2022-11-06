![LOGO_white](https://user-images.githubusercontent.com/90705245/200184883-02a83129-6122-4ed6-b979-40979d5824d7.png)

# Inspiration
Our group’s goal is to create a tool that lessens the handicap that the deaf or mute face, by increasing the accessibility of American Sign Language, using AI. We made it a priority to make our app accessible so that ASL might be approachable even for complete beginners.

# What it Does
The app is used to practice ASL for beginners. ASLingo allows the user to practice their ASL knowledge against a selection of quiz questions. The user is able to answer these questions by recording a video of themselves signing in ASL. Our program will then detect the ASL classifiers within the video using image recognition.

# How it was Built
Machine Learning
ASLingo implements Mediapipe to recognize human hands and fingers, as well as Tensorflow for model training and classification. We trained the machine learning model from scratch, taking pictures of our own hands for each of our supported ASL classifiers. Image recognition is performed on each frame of the recorded video recorded by the user.

# Front-End
The UI and UX were created in VueJS and is wrapped by IonicCapacitor to be compatible for Andriod devices. HTML and CSS are used to give the mobile app its look and feel.

# Back-End
The back-end of ASLingo implements Django and connects the front-end of the app to the machine learning side. A server is used to upload the video recorded by the user to an online database.

# Challenges and Accomplishments
Our greatest challenge was creating and implementing the machine learning model for ASL classifiers. While pretrained and comprehensive databases exist for ASL, most are limited to the ASL alphabet, or its digits from 0 to 9. ASL classifiers, which is what our program is trained to detect, represent broader concepts and as such are very useful to the user. It was also very challenging to integrate all facets of our code into a single program, as it includes a Django server, a Javascript website, an Android app, and a Python implementation.

As for our accomplishments, we have learned how to build and train a model, do image recognition (of hands and fingers) using it, and successfully did image classification, which are useful tools to apply in our future projects. We also learned how to work and code with other people efficiently so that we could finish the project on time.

# APP pictures
![IMG_6573](https://user-images.githubusercontent.com/90705245/200184922-133d5538-c291-4160-ab46-379009a83f64.jpg)
![IMG_6576](https://user-images.githubusercontent.com/90705245/200184940-386079b1-9cf5-42f5-ab56-5b20c6d81f0a.jpg)
![IMG_6577](https://user-images.githubusercontent.com/90705245/200184970-4cd9e2a7-fb76-4693-a648-220246fc9d27.jpg)
![IMG_6578](https://user-images.githubusercontent.com/90705245/200184984-ef726b7a-c5e2-4488-ba06-9d5a2152aba4.jpg)

