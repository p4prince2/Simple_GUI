import nlpcloud

class API:
    """
    A wrapper class for accessing NLPCloud's fine-tuned LLaMA 3 (70B) model APIs, including sentiment analysis,
    named entity recognition, and emotion prediction.

    Attributes:
        client (nlpcloud.Client): An instance of NLPCloud client initialized with the selected model and API key.
    """

    def __init__(self):
        """
        Initializes the NLPCloud client with the specified model and API key.
        Uses GPU acceleration if available.
        """
        self.client = nlpcloud.Client("finetuned-llama-3-70b", "Enter your Token from NLP cloud", gpu=True)

    def sentiment_api(self, text):
        """
        Performs sentiment analysis on the input text.

        Args:
            text (str): The input text to analyze.

        Returns:
            dict or str: The sentiment analysis result from NLPCloud, or a rate limit message if the API call fails.
        """
        try:
            return self.client.sentiment(text)
        except Exception as e:
            return """Rate limit: maximum number of requests per hour reached. Please contact support to learn how 
                    to increase this limit (if you are on the free plan, we encourage you to subscribe to the pay-as-you-go plan 
                    which provides a much higher throughput and many free requests). 
                    You can change your plan here: https://nlpcloud.com/home/plans."""

    def Name_Entity_Recognition_api(self, para, text):
        """
        Performs Named Entity Recognition (NER) on the provided paragraph and searches for a specific entity.

        Args:
            para (str): The paragraph of text in which to perform NER.
            text (str): The specific entity to search for.

        Returns:
            dict or str: The NER result highlighting found entities, or a rate limit message if the API call fails.
        """
        try:
            return self.client.entities(para, searched_entity=text)
        except Exception as e:
            return """Rate limit: maximum number of requests per hour reached. Please contact support to learn how 
                    to increase this limit (if you are on the free plan, we encourage you to subscribe to the pay-as-you-go plan 
                    which provides a much higher throughput and many free requests). 
                    You can change your plan here: https://nlpcloud.com/home/plans."""

    def Emotion_Prediction_api(self, para):
        """
        Predicts the emotional sentiment of a given paragraph using the sentiment analysis endpoint.

        Args:
            para (str): The paragraph for which to predict emotion.

        Returns:
            dict or str: The emotion prediction result (same as sentiment), or a rate limit message if the API call fails.
        """
        try:
            return self.client.sentiment(para)
        except Exception as e:
            return """Rate limit: maximum number of requests per hour reached. Please contact support to learn how 
                    to increase this limit (if you are on the free plan, we encourage you to subscribe to the pay-as-you-go plan 
                    which provides a much higher throughput and many free requests). 
                    You can change your plan here: https://nlpcloud.com/home/plans."""
