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
    new_game_message = "Umm, what are we... playing again?  Oh, right! Memory Loss! "\
            "I'll give you a series of words, numbers, or letters that you have to remember. "\
            "Then I'll ask you a question about them. Your job is to answer with either, "\
            "Yes, or, No, within 8 seconds. I won't repeat any questions, and I'll keep going "\
            "until someone tells me to stop. First question coming in... 3... 2... 1... "
    shuffle(QUESTIONS)
    question = choice(QUESTIONS)
    speech_output = new_game_message + question['question']
    should_end_session = False
    attributes = {
        "question": question,
        "game_status": "in_progress"
    }
    return speech(speech_output, attributes, should_end_session, None)
