"""
emotion_detection.py

This module provides functions to interact with the Emotion Detection API. It includes
functions for sending text for emotion analysis and processing the API's response.
"""

import requests

def emotion_detector(text_to_analyze):
    """
    Sends text to the Emotion Detection API and returns the raw response text.
    
    Args:
        text_to_analyze (str): The text to be analyzed for emotions.
        
    Returns:
        str: The raw response text from the API.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    response = requests.post(url, json=myobj, headers=header, timeout=120)
    return response.text

def emotion_predictor(text_to_analyze):
    """
    Analyzes the given text to predict the dominant emotion and its score.
    
    Args:
        text_to_analyze (str): The text to be analyzed for emotions.
        
    Returns:
        dict: A dictionary with 'dominant_emotion' and 'dominant_emotion_score'.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    data = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(
        url,
        json=data,
        headers=header,
        timeout=120
    )
    formatted_response = response.json()
    emotions = formatted_response.get('emotionPredictions', [{}])[0].get('emotion', {})

    if not emotions:
        return {
            'dominant_emotion': None,
            'dominant_emotion_score': None
        }

    dominant_emotion = max(emotions, key=emotions.get)
    dominant_score = emotions[dominant_emotion]

    return {
        'dominant_emotion': dominant_emotion,
        'dominant_emotion_score': dominant_score
    }
