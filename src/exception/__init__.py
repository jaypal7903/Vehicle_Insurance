import sys
import logging

def error_message_detail(error: Exception, error_detail : sys) -> str :
    """
    Extracted detailed error information including file name, line number, and the error message.

    :param error : the exception that occured.
    :param error_detail : the sys modeule to access trackback details.
    :return : a formatted error message string.
    """
    # Extract trackback details. (exception information)
    _, _, exc_tb = error_detail.exc_info()

    # get a file name where exception occured.
    file_name = exc_tb.tb_frame.f_code.co_filename

    # created formatted error message string with file name, line number, and actual error 
    line_number = exc_tb.tb_lineno
    error_message = f"Error occured in python script: [{file_name}] at the line number [{line_number}] : {str(error)}"

    # Log the error for better tracking
    logging.error(error_message)

    return error_message

class MyException(Exception):
    """
    Custom exception class for handling errors in the US visa application
    """
    def __init__(self, error_message: str, error_detail: sys):
        """
        Intializes the USvisaException with a detailed error message.

        :param error : A string describe the error
        :param error_detail : The sys module to access trackback details.
        """
        # call the base class constructer with the error message
        super().__init__(error_message)

        # format the detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self)  -> str :
        """
        Returns the string representation of the error message.
        """
        return self.error_message