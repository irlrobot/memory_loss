#!/usr/bin/env python
"""
Memory Loss
github.com/irlrobot/memory_loss
"""
from __future__ import print_function
import json
from play_new_game import play_new_game
from handle_answer_request import handle_answer_request
from alexa_responses import speech, play_end_message

def lambda_handler(event, _context):
    """main function for AWS Lambda"""
    print('=====lambda handler started...')
    print(json.dumps(event))

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])
        # this will trigger if a one shot is used
        if event['request']['type'] == "IntentRequest":
            return on_launch(event['request'], event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    if event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    if event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

def on_session_started(session_started_request, session):
    """when starting a new session"""
    print("=====on_session_started requestId:  " +
          session_started_request['requestId'] + ", sessionId=" +
          session['sessionId'])

def on_launch(event_request, session):
    """when customer launches the skill via modal"""
    print("=====on_launch requestId:  " + event_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return play_new_game()

def on_intent(event_request, session):
    """when customer launches the skill via modal"""
    print("=====on_intent requestId:  " + event_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent_name = event_request['intent']['name']
    print("=====intent is: " + intent_name)

    if intent_name == "AMAZON.YesIntent":
        print("=====YesIntent fired...")
        if 'attributes' in session:
            if session['attributes']['game_status'] == "in_progress":
                return handle_answer_request('yes', session)
    if intent_name == "AMAZON.NoIntent":
        print("=====NoIntent fired...")
        if 'attributes' in session:
            if session['attributes']['game_status'] == "in_progress":
                return handle_answer_request('no', session)
    if intent_name == "NotSureIntent":
        print("=====NotSureIntent fired...")
        if 'attributes' in session:
            if session['attributes']['game_status'] == "in_progress":
                return handle_answer_request('', session)
    if intent_name in ("AMAZON.StopIntent", "AMAZON.CancelIntent"):
        print("=====StopIntent or CancelIntent fired")
        return play_end_message()
    if intent_name == 'AMAZON.HelpIntent':
        print("=====HelpIntent...")
        tts = "All you have to do is answer Yes or No to each question I ask. "\
            "I won't repeat any of the questions, "\
            "so try to remember all the details. The game is best played with "\
            "a large group, and you should invent a scoring system or hand out "\
            "penalties for wrong answers.  I'll keep "\
            "asking questions until someone tells me to Stop. "\
            "Now, what's your guess for the last question?"
        return speech(tts, session['attributes'], False, None)

def on_session_ended(event_request, session):
    """when the user ends the session intentionally or timeout"""
    print("=====on_session_ended requestId=" + event_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return play_end_message()
