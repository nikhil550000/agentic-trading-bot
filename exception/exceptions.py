import sys
import os


class TradingBotException(Exception):


    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exec_tb = error_details.exc_info()
        

        self.lineno = exec_tb.tb_lineno
        self.filename  = exec_tb.tb_frame.f_code.co_filename


    def __str__(self):
        return "Error occurred in the python script name [{0}] at line number [{1}] with  error message [{2}]".format(
            self.filename,
            self.lineno,
            self.error_message
        )
    


if __name__ == "__main__":

    try:
        a=1/0
        print("This will not be printed",a)
    except Exception as e:
        raise TradingBotException(e,sys)