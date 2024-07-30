"""
server.py

A Flask application for analyzing emotions in text. It provides endpoints
for emotion detection and rendering the index page.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector, emotion_predictor

app = Flask(__name__)

@app.route("/emotionDetector", methods=['GET', 'POST'])
def sent_analyzer():
    """
    Analyze the emotions in the given text.
    Handles both GET and POST requests.
    """
    if request.method == 'GET':
        text_to_analyze = request.args.get('textToAnalyze')
    elif request.method == 'POST':
        text_to_analyze = request.form.get('textToAnalyze')
    else:
        return "Unsupported method", 405

    if not text_to_analyze:
        return "No text provided for analysis", 400

    # Call emotion_detector to get the detected text
    detected_text = emotion_detector(text_to_analyze)

    if not detected_text:
        return "Error in emotion detection", 500

    # Call emotion_predictor to get emotions, which should return a dictionary
    emotions = emotion_predictor(detected_text)

    if not isinstance(emotions, dict):
        return "Error in emotion detection response", 500

    label = emotions.get('dominant_emotion')
    score = emotions.get('dominant_emotion_score')

    if label is None or score is None:
        return "Unable to detect emotion", 400

    split_label = label.split('_')
    dominant_emotion = split_label[1] if len(split_label) > 1 else label
    result = (
        f"The given text has been identified as {dominant_emotion} "
        f"with a score of {score}"
    )

    return result

@app.route("/")
def render_index_page():
    """
    Render the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
