# Face Detection and Recognition for Criminal Identification System

## Overview
This project presents a computer vision-based system for criminal identification using face detection and recognition techniques. The system is designed to identify individuals by analyzing facial features and matching them against stored records. It aims to support security and surveillance applications by enabling automated and efficient identification.

The application is developed using Python and integrates OpenCV for image processing and SQLite for data storage. It also provides a graphical user interface to facilitate user interaction.

## Key Features
- Registration of individuals with associated facial data
- Storage of personal and facial information in a structured database
- Face detection using Haar Cascade Classifier
- Face recognition based on trained image data
- Real-time identification using webcam input
- Graphical user interface for ease of use
- Model training and data persistence

## Technologies Used
- Python
- OpenCV (Computer Vision Library)
- SQLite (Database)
- Tkinter (GUI Framework)
- Haar Cascade Classifier

## System Workflow
1. Individuals are registered through the system with relevant details and facial images.
2. The facial data is stored in a local SQLite database.
3. The system trains a recognition model using the collected image dataset.
4. During execution, the system captures real-time video or image input.
5. Detected faces are compared with stored data to identify matches.
6. If a match is found, the corresponding individual’s details are retrieved and displayed.

## Project Structure
- `registration.py` – Handles registration and data entry of individuals
- `criminal_registration.py` – Stores and manages criminal-related data
- `gui_main.py` / `GUI_master.py` – Main graphical user interface
- `display.py` – Displays recognition results and outputs
- `trainingdata.yml` – Stores trained model data
- `haarcascade_frontalface_default.xml` – Pre-trained classifier for face detection
- Database files (`.db`) – Store user and criminal records

## Project Documentation
The complete project documentation is available at the following link:
[Insert Google Drive Link Here]

The documentation includes:
- Final Year Project Report
- Published Research Paper
- Certificate
- Project Presentation (PPT)

## Objective
The objective of this project is to develop an automated system capable of identifying individuals, particularly criminals, using facial recognition techniques. The system aims to improve the accuracy, speed, and reliability of identification processes in security-related applications.

## Future Scope
- Integration with large-scale surveillance systems such as CCTV networks
- Deployment using cloud-based infrastructure for scalability
- Enhancement using deep learning-based face recognition models
- Improvement in recognition accuracy under varying environmental conditions

## Author
Shravani Mahabare  
Bachelor of Engineering in Computer Engineering  
Full Stack Developer
