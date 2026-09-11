# AURA – Intelligent Voice Assistant using NLP

## Student Details

| Field | Details |
|---|---|
| Student Name | SAMRUDHI WANKHADE |
| Roll Number | ET58 |
| BT ID | BT240058ET |
| Course | Natural Language Processing (ET5M004) |
| Semester / Branch | V Semester ETC |
| Project Type | NLP Application-Based Mini Project |

---

## 1. Project Title

**AURA – Intelligent Voice Assistant using Natural Language Processing**

---

## 2. Problem Statement / Objective

The objective of AURA is to develop a website-based intelligent voice assistant that can understand spoken user commands, process them using Natural Language Processing techniques, identify the user's intent, perform the required action, and provide a suitable response through voice.

The project demonstrates the practical application of speech recognition, Natural Language Processing, intent classification, and text-to-speech technologies.

---

## 3. Introduction

Voice assistants provide a natural and convenient way for users to interact with computer systems using spoken language.

AURA is an NLP-based voice assistant designed to accept voice commands from the user, convert speech into text, analyze the user's command, determine the appropriate intent, and generate a response.

The system demonstrates how Natural Language Processing can be used to create an interactive human-computer communication system.

---

## 4. NLP Technique / Method Used

The project uses the following NLP and AI techniques:

- Speech-to-Text conversion
- Text preprocessing
- Natural Language Processing
- Intent classification
- Command/response mapping
- Text-to-Speech conversion

### Basic Processing Flow

**Voice Input → Speech Recognition → Text Preprocessing → Intent Detection → Action/Response → Text-to-Speech → Voice Output**

---

## 5. Dataset / Source of Data

The project uses a custom dataset containing example user commands and their corresponding intents.

The dataset is used to train/test the intent classification component of the voice assistant.

The dataset is stored in the `dataset/` directory of the repository.

---

## 6. Software, Tools and Libraries Used

### Programming Language

- Python

### Libraries / Technologies

- SpeechRecognition
- PyAudio
- pyttsx3
- Scikit-learn
- Jupyter

### Development Tools

- Visual Studio Code
- Git
- GitHub

---

## 7. Methodology / Workflow

1. The user provides a voice command.
2. The system captures the user's speech.
3. Speech recognition converts the audio into text.
4. The text is preprocessed for NLP processing.
5. The system identifies the user's intent.
6. The appropriate command/action is selected.
7. A response is generated.
8. The response is converted into speech.
9. The user receives the final voice response.

---

## 8. Project Structure

AURA-Voice-Assistant-NLP/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── dataset/
│   └── intents.json
│
└── source_code/
    ├── main.py
    ├── actions.py
    ├── nlp_processor.py
    ├── voice_input.py
    ├── voice_output.py
    ├── test_nlp.py
    └── test_voice.py
    ---

## 9. Steps to Execute the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/samrudhiwankhade18-hub/AURA-Voice-Assistant-NLP.git
cd AURA-Voice-Assistant-NLP