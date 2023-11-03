# Weight-Unit-converter
 This Python code is a weight unit converter. It allows users to enter their weight in either pounds or kilograms and then converts it to the other unit
 
 The code uses the following steps:

It imports the tkinter library to create a graphical user interface (GUI).
It creates a main window for the GUI application and sets its title and geometry.
It creates two StringVar objects to store the user's weight and weight unit.
It creates two Label widgets to display the text "Enter the weight" and "Enter the unit".
It creates two Entry widgets to allow the user to enter their weight and weight unit.
It creates a Label widget to display the converted weight.
It creates a Button widget with the text "Enter your weight". When the button is clicked, the get_weight_value() function is called.
The get_weight_value() function strips any leading or trailing whitespace from the user's weight unit and then checks if the unit is "L", "l", "K", or "k". If the unit is "L" or "l", the function converts the user's weight to kilograms and displays it in the emptylabel widget. If the unit is "K" or "k", the function converts the user's weight to pounds and displays it in the emptylabel widget.
