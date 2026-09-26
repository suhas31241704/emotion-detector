"""
This module defines the emotion_detector function, which sends text to the
Watson NLP EmotionPredict API and returns a formatted dictionary of emotion
scores along with the dominant emotion.
"""

import json
import requests


def emotion_detector(text_to_analyze):
    """
    Analyze the emotion of the given text using the Watson NLP library.

    Args:
        text_to_analyze (str): The text to run emotion detection on.

    Returns:
        dict: A dictionary containing the scores for 'anger', 'disgust',
        'fear', 'joy', 'sadness', and the 'dominant_emotion'. If the input
        text is blank or invalid, all values are set to None.
    """
    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
           'watson.runtime.nlp.v1/NlpService/EmotionPredict')
    headers = {"grpc-metadata-mm-model-id":
               "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers, timeout=10)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotion_predictions['anger']
    disgust_score = emotion_predictions['disgust']
    fear_score = emotion_predictions['fear']
    joy_score = emotion_predictions['joy']
    sadness_score = emotion_predictions['sadness']

    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores