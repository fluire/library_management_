import logging
import pprint

class CustomLogger:
    def __init__(self, level=logging.DEBUG):
        self.logger = logging.getLogger()
        self.logger.setLevel(level)

        # retty_data = pprint.pformat(message, indent=4)
        log_format = "%(levelname)s %(asctime)s - %(message)s"
        formatter = logging.Formatter(log_format)
                
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)


    def ppinfo(self, data, level=logging.INFO):
        # Pretty-print the dictionary
        pretty_data = pprint.pformat(data, indent=4)
        
        # Log the pretty-printed dictionary
        self.logger.log(level, "%s", pretty_data)

    def get_logger(self):
        return self.logger
    

custom_logger = CustomLogger()
logger = custom_logger.get_logger()
