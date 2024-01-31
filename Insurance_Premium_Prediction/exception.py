import sys

# Custom exception class
class customexception(Exception):
    def __init__(self, error_message, error_details):
        # Initializing error message and details
        self.error_message = error_message
        self.error_details = error_details
        
        # Extracting line number and file name if available
        _, _, exc_tb = self.error_details.exc_info()
        if exc_tb:
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.lineno = None
            self.file_name = None
    
    def __str__(self):
        # String representation of the custom exception
        return "Error occurred in Python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message))

if __name__ == "__main__":
    try:
        # Sample code raising an exception
        a = 1 / 0
    except Exception as e:
        # Raising custom exception with error message and system details
        raise customexception(e, sys)
