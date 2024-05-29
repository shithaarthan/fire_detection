# Fire Detection AI Using YOLO 🔥📷
## Project Description📝
This project implements a fire detection system using the YOLO (You Only Look Once) object detection algorithm. The system processes live camera feeds to detect instances of fire in real-time. Upon detecting fire, the system sends an alert via email and SMS to the concerned authorities to facilitate a prompt response.

## Features 🪄

-   **Real-Time Detection:** Utilizes the YOLO algorithm for efficient and accurate real-time fire detection.
-   **Alert System:** Automatically sends notifications via email and SMS when fire is detected.
-   **Scalable:** Can be integrated with multiple camera feeds.
-   **Customizable:** Thresholds for detection sensitivity and notification settings can be easily adjusted.

## Prerequisites 🌟

-   Python 3.7 or higher
-   OpenCV
-   YOLOv4 or YOLOv5 model weights and configuration files
-   TensorFlow or PyTorch (depending on the version of YOLO used)
-   SMTP server for sending emails
-   Twilio account for sending SMS

## Installation ⬇️

1.  **Clone the repository:**
    
    `git clone https://github.com/yourusername/fire-detection-ai.git` 

1.  **Download YOLO weights and configuration:**
    
    -   For YOLOv4: [YOLOv4 Weights and Config](https://github.com/AlexeyAB/darknet)
    -   For YOLOv5: [YOLOv5 Repository](https://github.com/ultralytics/yolov5)
  ## Set up environment variables for email and SMS notifications:**
    
   Edit a `gen_message.py` file in the root directory of the project and add your SMTP and Twilio credentials.
        
        makefile        
        EMAIL_ADDRESS=your_email@example.com
        EMAIL_PASSWORD=your_email_password
        TWILIO_ACCOUNT_SID=your_twilio_account_sid
        TWILIO_AUTH_TOKEN=your_twilio_auth_token
        TWILIO_PHONE_NUMBER=your_twilio_phone_number
        ALERT_PHONE_NUMBER=alert_recipient_phone_number`
## Usage

1.  **Run the fire detection script:**
    
    `main.py` 
    
2.  **Configuration:**
    
    -   You can adjust the detection sensitivity and notification settings in the `operate.py` file.
3.  **Integrating with Multiple Cameras:**
    
    -   Modify the `camera_sources` list in `operate.py` to include URLs or device indices of the cameras.
  

## Contributing 🤝

We welcome contributions to enhance the functionality and performance of this fire detection system. Please follow these steps to contribute:

1.  Fork the repository.
2.  Create a new branch with a descriptive name for your feature or fix.
3.  Make your changes and commit them with clear and concise messages.
4.  Push your changes to your forked repository.
5.  Open a pull request with a detailed description of your changes.
