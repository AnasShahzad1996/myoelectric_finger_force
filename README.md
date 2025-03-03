# Neuroprosthetics Finger Force Measurement Device

This project implements a finger force measurement device using Arduino and Python. It includes a Tkinter-based GUI for user input, calibration, force measurement, and data visualization.

## Overview

The system consists of the following components:

1.  **Arduino Code:** (Not included in the provided Python code, but assumed to be running on an Arduino board) Reads data from force sensors attached to the fingers and transmits the data serially to the Python application.

2.  **Python Code:**
    *   Receives serial data from the Arduino.
    *   Provides a user interface for:
        *   Collecting user information.
        *   Calibrating the force sensors.
        *   Measuring and visualizing finger forces in real-time.
        *   Displaying basic statistics.
        *   Providing an example measurement.
    *   Saves calibration data and potentially measurement data.

## Dependencies

*   Python 3.x
*   `pyserial`
*   `tkinter`
*   `pillow` (PIL - Python Imaging Library)
*   `matplotlib`
*   `numpy`
*   `json`

You can install the required Python packages using pip:


## Hardware Setup

1.  Connect force sensors to the appropriate analog pins on the Arduino board.
2.  Upload the Arduino code to the board.  Ensure the Arduino code transmits serial data in a format that the Python script can parse.  The Python code expects data in the format `"value|finger_name"`.
3.  Connect the Arduino to your computer via USB.  Identify the correct serial port (e.g., `/dev/ttyACM0` on Linux, `COM3` on Windows).  Modify the `arduinoSerialData` line in the Python code if necessary.

## Software Setup

1.  Clone this repository.
2.  Install the dependencies listed above.
3.  Run the Python script.


## Usage

1.  **User Information:**  The application starts with a user form to collect name, email, age, biological sex, and selected fingers. Fill out the form and submit.
2.  **Options:** After submitting the user form, an options window appears. You can choose between:
    *   **Calibration:** Calibrates the force sensors. This step is crucial for accurate measurements. Follow the on-screen instructions carefully, including placing and removing weights as prompted. The calibration parameters are saved to a JSON file (`data/calib_param.json`).
    *   **Force Measurement:** Starts the real-time force measurement and visualization.  A plot displays the force readings from each finger over time, along with a sine wave to guide the user's finger movements.  A "Total Force" plot is displayed in real time
    *   **Statistics:** (Not implemented)  Intended to display statistical analysis of the measured force data.
    *   **Example:** (Not implemented)  Intended to provide an example measurement or demonstration.
3.  **Calibration Procedure:**
    *   The calibration process first measures the offset (zero force reading) for each sensor.
    *   Then, it prompts the user to place a known weight (0.5 kg) on each finger sensor to determine the scaling factor.
    *   The calibration parameters (offset and scale) are saved to `data/calib_param.json`.
4.  **Force Measurement:**
    *   The force measurement window displays real-time force readings from each finger sensor.
    *   The data is plotted using Matplotlib.
    *   A sine wave is displayed to guide the user in flexing and extending their fingers.
    *   Clicking the "Save and Close" button saves the plot (the data saving is not implemented in this version of the code).

## Code Structure

*   `UserForm`:  Tkinter class for the initial user information form.
*   `OptionsForm`: Tkinter class for the main menu, providing options for calibration, measurement, etc.
*   `Calib_form`: Tkinter class for the calibration procedure. It reads the calibration parameters.
*   `Measurment_form`: Class that manages the force measurement and real-time plotting using Matplotlib.
*   `arduinoSerialData`:  Serial port object for communication with the Arduino.

## Data Format

The Arduino is expected to send data in the following format:

`value1|finger1\nvalue2|finger2\n...`

Where:

*   `value` is the raw sensor reading (an integer).
*   `finger` is the name of the finger (e.g., "little", "ring", "middle", "index", "thumbx", "thumby").

## Limitations and Future Work

*   **Data Saving:** The current code does *not* save the measured force data to a file.  This is a major area for improvement.
*   **Statistics and Example Functionality:** The "Statistics" and "Example" options are not implemented.
*   **Error Handling:** The code lacks robust error handling (e.g., handling serial communication errors, invalid user input, missing calibration file).
*   **GUI Improvements:** The GUI could be improved for better usability and aesthetics.
*   **Calibration:** The calibration process could be made more automated and accurate.
*   **Arduino Code:**  The Arduino code is not provided, but it is a necessary component of the system.
*   **Units:**  The code doesn't explicitly handle units (e.g. converting raw sensor values to Newtons or kilograms).

## Contributing

Contributions are welcome!  Feel free to fork this repository, make improvements, and submit pull requests.


