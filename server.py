"""
This module runs a Flask application for emotion detection.
"""

from flask import Flask, render_template, request  # Import Flask modules
# Import the emotion_detector function
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_emotion_detector():
    """
    Endpoint to analyze the sentiment of given text.
    
    Returns:
        str: Formatted response with emotion scores and dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    # Extract the emotion scores
    anger_score = response["anger"]
    disgust_score = response["disgust"]
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        formatted_response = "Invalid text! Please try again!."
    else:
        # Format the response string
        formatted_response = (
            f"For the given statement, the system response is 'anger': {anger_score}, "
            f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} and "
            f"'sadness': {sadness_score}. The dominant emotion is <b>{dominant_emotion}</b>."
        )
    return formatted_response

@app.route("/")
def render_index_page():
    """
    Renders the index HTML page.
    
    Returns:
        str: Rendered HTML of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # This function executes the Flask app and deploys it on localhost:5000.
    app.run(host="0.0.0.0", port=5000)
