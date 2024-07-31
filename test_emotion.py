import unittest
from EmotionDetection import emotion_predictor

class testEmotionDetection(unittest.TestCase):

    def test_joy(self):
        dominant_emotion, _ = emotion_predictor("I am glad this happened")
        self.assertEqual(dominant_emotion, "joy", "Expect 'joy' but got something else!")
    
    def test_joy(self):
        dominant_emotion, _ = emotion_predictor("I am glad this happened")
        self.assertEqual(dominant_emotion, "joy", "Expect 'joy' but got something else!")
    
    def test_anger(self):
        dominant_emotion, _ = emotion_predictor("I am really mad about this")
        self.assertEqual(dominant_emotion, "anger", "Expect 'anger' but got something else!")
    
    def test_disgust(self):
        dominant_emotion, _ = emotion_predictor("I feel disgusted just hearing about this")
        self.assertEqual(dominant_emotion, "disgust", "Expect 'disgust' but got something else!")

    def test_sadness(self):
        dominant_emotion, _ = emotion_predictor("I am so sad about this")
        self.assertEqual(dominant_emotion, "sadness", "Expect 'sadness' but got something else!")

    def test_fear(self):
        dominant_emotion, _ = emotion_predictor("I am really afraid that this will happen")
        self.assertEqual(dominant_emotion, "fear", "Expect 'fear' but got something else!")

if __name__ == '__main__':
    unittest.main()
