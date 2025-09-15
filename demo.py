# from src.logger import logging

# logging.debug("This is a debug message")


# from src.exception import MyException
# import sys


# try:
#     a=1+z
# except Exception as e:
#     logging.info("We are logging the error now")
#     raise MyException(e, sys) from e    
from src.pipline.training_pipeline import TrainPipeline 
pipeline=TrainPipeline()
pipeline.run_pipeline()