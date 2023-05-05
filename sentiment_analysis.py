from transformers import pipeline
import typing as t

sentiment_pipeline = pipeline("sentiment-analysis")

def sentiment_analysis(text: t.Union[str, t.List]) -> t.List[t.Dict]:
    result = sentiment_pipeline(text)
    return result


if __name__ == "__main__":
    print(sentiment_analysis("I love your product!"))
    print(sentiment_analysis("I hate your product :("))