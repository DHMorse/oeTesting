from typing import List, Dict, Any, Tuple

MY_USER_ID = 1214760182576324680

MY_USER_NAME = 'john5971'

EXCEPTION_OUTPUT_FILE_LOCATION = './exceptions.log'

TEST_OUTPUT_FILE_LOCATION = './tests.csv'

FAILED_TESTS_FILE_LOCATION = './failedTests.csv'

LOG_CHANNEL_ID = 1304829859549155328
TESTING_CHANNEL_ID = 1320533335054749817
OUTPUT_CHANNEL_ID = 1320988937149349959

COLORS = {
    'red': '\u001b[1;31m',
    'yellow': '\u001b[1;33m',
    'blue': '\u001b[1;34m',
    'green': '\u001b[1;32m',
    'reset': '\u001b[0m'
}

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
        file.write(f'Exception: {exception}\nTraceback: {traceback}\n\n')