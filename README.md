# VisionAI
VisionAI is a project designed to assist visually impaired individuals by helping them understand their surroundings.

# VisionAI

VisionAI is a project designed to assist visually impaired individuals by helping them understand their surroundings. The system utilizes a camera attached to glasses and integrates with an app via Bluetooth. The app processes real-time video data frame by frame, generates captions using CNN and LSTM models, refines these captions with an LLM, and provides the output as speech.

## Features
- **Real-Time Video Processing**: Captures and processes video data frame by frame.
- **Caption Generation**: Uses CNN and LSTM models to generate descriptive captions for each frame.
- **Caption Refinement**: The generated captions are refined into more natural language using an LLM.
- **Voice Output**: The refined captions are converted to speech and conveyed to the user.
- **Interactive Interface**: Allows users to start the processing by tapping on the screen.

## Files
- **`app.py`**: Contains the code for the main application logic, including Bluetooth communication, video processing, and interaction with the LLM and text-to-speech systems.
- **`mini_project.ipynb`**: Includes the code and experiments related to the caption generation using CNN and LSTM models.
- **`requirements.txt`**: Lists the dependencies required to run the project.

## Installation
1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/visionai.git
    cd visionai
    ```

2. **Set up the environment**:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. **Run the Application**:
    - Ensure that the camera and Bluetooth devices are properly set up and paired.
    - Run the application by executing:
      ```bash
      python app.py
      ```

2. **Process Video Data**:
    - Once the app is running, tap on the screen to start processing video data. The app will capture frames, generate captions, refine them, and convert the output to speech.

3. **Review Results**:
    - Captions and their corresponding speech outputs can be reviewed in the application interface.

## Notes
- Ensure that all necessary hardware (camera, Bluetooth-enabled specs) is correctly configured and connected.
- Adjust the configuration and parameters in `app.py` and `mini_project.ipynb` as needed for your specific setup.

## Contributing
This project is developed by **Shreya Sindhu Tumuluru**, **Navya SG**, **Anuritha L**, and **Anushka Singh**. Contributions are welcome! If you have suggestions for improvements or want to add new features, please open an issue or submit a pull request.

## Acknowledgements
We thank the open-source community for their resources and support, which have been instrumental in developing VisionAI.


