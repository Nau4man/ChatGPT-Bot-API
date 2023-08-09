# ChatGPT Bot API

Welcome to the ChatGPT Bot! This project demonstrates a simple web interface that allows users to interact with the OpenAI GPT-3 model to generate responses based on prompts.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview <a name="overview"></a>

This web application uses Flask and JavaScript to provide a user-friendly interface for interacting with the OpenAI GPT-3 API. Users can create prompts, generate responses, update prompts, and delete prompts via a web browser.

## Features <a name="features"></a>

- Create prompts and get generated responses from the GPT-3 model.
- Update existing prompts with new text.
- Delete unwanted prompts from the system.
- Sidebar to display and manage created prompts.

## Getting Started <a name="getting-started"></a>

### Prerequisites <a name="prerequisites"></a>

Before you begin, ensure you have the following installed:

- Python (3.6 or higher)
- Flask
- OpenAI Python package
- A valid OpenAI API key

### Installation <a name="installation"></a>

1. Clone the repository:

```bash
git clone https://github.com/Nau4man/chatgpt-bot-webapp.git
```

2. Navigate to the project directory:
```bash
cd ChatGPT-Bot-API
```
3. Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```
4. Set your OpenAI API key as an environment variable. You can store it in a .env file in the project root:
```bash
OPENAI_API_KEY=your_api_key_here
```
### Usage <a name="usage"></a>
1. Start the Flask application:
```bash
python app.py
```
2. Open your web browser and navigate to http://localhost:5000.

3. Use the web interface to create prompts, generate responses, update prompts, and delete prompts.

### Contributing <a name="contributing"></a>
Contributions are welcome! Please fork the repository and create a pull request with your proposed changes.

### License <a name="license"></a>
This project is licensed under the MIT License.

### Contact <a name="contact"></a>

For any inquiries or feedback, please contact:
Email: officialnaumansabir@gmail.com

