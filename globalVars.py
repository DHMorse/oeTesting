import asyncio
import random
import time
import traceback

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

CLEAN_MESSAGES = [
    "The sun is shining brightly today.",
    "I just finished reading a great book!",
    "What time is dinner tonight?",
    "Have you seen my keys anywhere?",
    "Let's take a walk in the park this afternoon.",
    "I can't wait for the weekend to arrive.",
    "The coffee at this new cafe is amazing.",
    "I need to water the plants before they dry out.",
    "Do you want to watch a movie later?",
    "The birds outside are singing so beautifully.",
    "This recipe calls for a pinch of salt.",
    "I'll call you back in ten minutes.",
    "The sky is so clear and blue right now.",
    "I think I'll try baking cookies today.",
    "How was your day at work?",
    "We should plan a trip to the mountains.",
    "Can you pick up some milk on your way home?",
    "It's amazing how fast this year has gone by.",
    "The dog loves playing fetch with the new ball.",
    "I just learned how to fold an origami crane.",
    "Do you remember where we parked the car?",
    "The sound of rain is so relaxing.",
    "Would you like some tea or coffee?",
    "This sweater is so cozy and warm.",
    "I'm looking forward to seeing you tomorrow.",
    "The flowers in the garden are blooming beautifully.",
    "Have you ever tried making homemade pasta?",
    "The smell of freshly baked bread is wonderful.",
    "It's nice to sit and relax after a busy day.",
    "I love watching the sunset by the beach.",
    "Could you help me carry these groceries inside?",
    "I'm thinking of repainting the living room.",
    "The cat is curled up on the windowsill again.",
    "Do you want to join me for a game of chess?",
    "I just discovered a new favorite song.",
    "Let's have a picnic by the lake this weekend.",
    "I really enjoyed our conversation earlier.",
    "The stars look so bright and clear tonight.",
    "Could you pass me the remote, please?",
    "I'm organizing my bookshelf this afternoon.",
    "I can't decide between vanilla or chocolate ice cream.",
    "The breeze feels so refreshing right now.",
    "We should try that new restaurant downtown.",
    "This puzzle is more challenging than I expected.",
    "The library is such a peaceful place to be.",
    "I'm so excited to start my new hobby.",
    "The waffles this morning were delicious!",
    "I can't wait to see how this project turns out.",
    "The kids are having so much fun at the park.",
    "The aroma of cinnamon always reminds me of fall.",
    "I need to finish writing that report tonight.",
    "Would you like to go hiking this weekend?",
    "I'm wrapping up a gift for a friend's birthday.",
    "The clouds look like fluffy marshmallows today.",
    "This scarf was a perfect choice for the weather.",
    "Can we stop by the farmer's market later?",
    "The concert last night was incredible!",
    "I love trying out new recipes in the kitchen.",
    "The fireplace makes the living room so cozy.",
    "The soup is simmering and smells amazing.",
    "The museum exhibit was so interesting and educational.",
    "I finally learned how to knit a scarf!",
    "The fresh air feels so invigorating today.",
    "I can't believe how much the garden has grown.",
    "Do you want to join me for a bike ride?",
    "The treehouse looks like it came straight out of a storybook.",
    "We should plan a road trip for the holidays.",
    "The fruit salad turned out really tasty!",
    "The bookstore had a great sale today.",
    "This blanket is perfect for a chilly evening.",
    "I'm thinking of planting more herbs in the garden.",
    "The river looks so peaceful and calm.",
    "It's so nice to catch up with old friends.",
    "I found a cute little shop while walking downtown.",
    "Let's make some hot cocoa and watch a movie.",
    "The breeze smells like salt and the sea.",
    "The pancakes turned out so fluffy this morning.",
    "I think I'll go for a jog after breakfast.",
    "Can you believe how fast the week has flown by?",
    "The sunrise was absolutely stunning this morning.",
    "I just finished organizing my closet and it feels great.",
    "This book is so good I can't put it down.",
    "The dog learned a new trick today!",
    "The festival downtown was so much fun.",
    "I love how soft this new sweater feels.",
    "The homemade jam tastes amazing on toast.",
    "Do you want to join me for a board game night?",
    "The train ride through the countryside was beautiful.",
    "I think the cookies need a few more minutes in the oven.",
    "The sound of waves crashing on the shore is so soothing.",
    "The picnic by the river was such a good idea.",
    "I just finished assembling the new shelf, and it looks great.",
    "Let's grab some ice cream after dinner.",
    "The stars are twinkling so brightly tonight.",
    "I'm excited to start the new project tomorrow.",
    "The new park in the neighborhood looks amazing.",
    "This candle smells like vanilla and lavender."
]

tests: List[Dict[str, any]] = []

    #[
    #    {
    #        'passed': bool,
    #        'expectedResult': any,
    #        'actualResult': any
    #        'test': str
    #    } 
    #]