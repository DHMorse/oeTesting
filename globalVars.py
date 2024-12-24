from typing import List, Dict, Any, Tuple

MY_USER_ID = 1214760182576324680

MY_USER_NAME = 'john5971'

EXCEPTION_OUTPUT_FILE_LOCATION = './exceptions.log'

LOG_CHANNEL_ID = 1304829859549155328
TESTING_CHANNEL_ID = 1320533335054749817

tests: List[Dict[str, any]] = []

    #[
    #    {
    #        'passed': bool,
    #        'expectedResult': any,
    #        'actualResult': any
    #        'test': str
    #    } 
    #]

async def writeExepctoinToLogFile(exception: Exception, traceback: str):
    with open(EXCEPTION_OUTPUT_FILE_LOCATION, 'a') as file:
        file.write(f'{exception}\n')