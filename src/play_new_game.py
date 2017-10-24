#!/usr/bin/env python
"""
Memory Loss
github.com/irlrobot/memory_loss
"""
from __future__ import print_function
from random import choice, shuffle
from alexa_responses import speech
from brain_training import QUESTIONS

def play_new_game():
    """play new game intro and build question bank"""
    print("=====play_new_game fired...")
    new_game_message = "Welcome to Memory Loss!  Playing is easy.  I'll give "\
            "a brain teaser and then ask a question.  Your job is to answer "\
            "with a simple Yes, or, No within 8 seconds. I'll keep going until "\
            "someone tells me to stop. Invent your own scoring system and play "\
            "with others for the most fun.  "\
            "First question coming in... 3... 2... 1... "
    shuffle(QUESTIONS)
    question = choice(QUESTIONS)
    speech_output = new_game_message + question['question']
    should_end_session = False
    attributes = {
        "question": question,
        "game_status": "in_progress"
    }
    return speech(speech_output, attributes, should_end_session, None)
