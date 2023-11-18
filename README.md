# Network Alchemist

## Overview
Network Alchemist is a desktop application designed to streamline network troubleshooting. It allows users to input Windows CLI commands and displays the output in a Graphical User Interface (GUI) built with python Tkinter, a Python binding to the Tk GUI toolkit. This makes the process of network troubleshooting more accessible to those who are not comfortable with the CLI, and more efficient for those who are.

## Features
The application supports the following commands:
- ipconfig /all
- ping "URL"
- traceroute
- nsslookup
- ipconfig /flushdns
- ipconfig /release
- netsh int ip reset
- netsh winsock reset

## Usage
1. **Command Input**: The application provides an input field for users to enter the desired CLI command.
2. **Command Processing**: The application processes the entered command in the background without freezing the GUI.
3. **Output Display**: The application displays the output of the command in a readable format in the GUI.
4. **Error Handling**: The application handles errors gracefully, providing informative error messages to the user.

## Installation

Follow these steps to install and run Network Alchemist:

1. **Create a Python Virtual Environment**: First, you need to create a virtual environment in Python. This can be done using the following command:
    ```bash
    python -m venv env
    ```
    This will create a new virtual environment named 'env'.

2. **Activate the Virtual Environment**: Activate the newly created virtual environment with this command:
    - On Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - On Unix or MacOS:
        ```bash
        source env/bin/activate
        ```

3. **Clone the Repository**: Clone the Network Alchemist repository from GitHub using the following command:
    ```bash
    git clone https://github.com/muhit-khan/NETWORK-ALCHEMIST.git
    ```

4. **Navigate to the Repository**: Change your directory to the cloned repository:
    ```bash
    cd NETWORK-ALCHEMIST
    ```

5. **Install Required Packages**: Install the necessary Python packages using the requirements.txt file included in the repository:
    ```bash
    pip install -r requirements.txt
    ```

6. **Run the Application**: Finally, you can run the application using the following command:
    - On Windows:
        ```bash
        runas /user:Administrator "python main.py"
        ```
    - On Unix or MacOS:
        ```bash
        sudo python main.py
        ```

That's it! You should now be able to use Network Alchemist on your local machine.



## Documentation
The [Software Requirements Specification (SRS)](/SRS_Document/NETWORK%20ALCHEMIST_SRS_Doc.pdf) document for Network Alchemist can be found here.

## Contributors
This Project is jointly prepared by:
* [Muhit Khan](https://linkedin.com/in/muhit-khan)
* [Sangbartika Saha](https://www.linkedin.com/in/sangbartika-saha-2866b727b/)

## Future Scope
Future enhancements could include the ability to save command outputs for future reference, and the integration of more advanced network troubleshooting tools.

## License
This project is licensed under the [MIT License](LICENSE).