"""
File: doctorservergui.py
Project 5

GUI-based view for non-directive psychotherapy.
"""

from doctor import Doctor
from breezypythongui import EasyFrame

class DoctorGUI(EasyFrame):
    """Represents the app's window."""

    COLOR = "#CCEEFF"

    def __init__(self):
        """Initialize the frame and widgets."""
        EasyFrame.__init__(self, title = "Doctor",
                           background = DoctorGUI.COLOR)
        # Instantiate the model
        self.doctor = Doctor()
        # Add the labels, fields, and button
        self.addLabel(text = "Doctor", row = 0, column = 0,
                      background = DoctorGUI.COLOR)
        self.drField = self.addTextField(self.doctor.greeting(),
                                         row = 0, column = 1,
                                         width = 50, state = "readonly")
        self.addLabel(text = "Patient", row = 1, column = 0,
                      background = DoctorGUI.COLOR)
        self.ptField = self.addTextField(text = "", row = 1,
                                         column = 1, width = 50)
        self.button = self.addButton(row = 2, column = 0,
                                     columnspan = 2,
                                     text = "Send reply",
                                     command = self.sendReply)
        # Support the return key in the input field
        self.ptField.bind("<Return>", lambda event: self.sendReply())

    def sendReply(self):
        """Sends patient input to doctor, receives
        and outputs reply."""
        ptInput = self.ptField.getText()
        if ptInput.upper() == "QUIT":
            self.drField.setText(self.doctor.farewell())
            self.button["command"] = self.newSession
            self.button["text"] = "New session"
        else:
            drReply = self.doctor.reply(ptInput)
            self.drField.setText(drReply)
            
    def newSession(self):
        """Starts a new session with the doctor."""
        self.doctor = Doctor()
        self.ptField.setText("")
        self.drField.setText(self.doctor.greeting())
        self.button["command"] = self.sendReply
        self.button["text"] = "Send reply"
            
def main():
    """Instantiate and pop up the window."""
    DoctorGUI().mainloop()

if __name__ == "__main__":
    main()



