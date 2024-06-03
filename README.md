<!--
# Depression-Detection-System-by-Analyzing-Tweets
Developed a system that uses the Twitter API to scrape the real-time tweets, classified the tweets using Hybrid
Naive Bayes and SVM model, and plotted a graph which was used to classify the depression into two categories
Major depression and bipolar depression.

![image](https://user-images.githubusercontent.com/20738263/145753373-3154b226-0d6b-401b-8bf2-246277f5991b.png)
![image](https://user-images.githubusercontent.com/20738263/145753413-e9cdd294-dc3f-4028-acb4-677d85818a94.png)
![image](https://user-images.githubusercontent.com/20738263/145753441-6953e800-3993-4707-86d0-0f49c5dd0751.png)
![image](https://user-images.githubusercontent.com/20738263/145753465-30a08396-cdbf-43aa-a370-fd9deaf93491.png)
![image](https://user-images.githubusercontent.com/20738263/145753488-2f683996-92c0-41ee-88aa-06caf72dec89.png)


# Dpds

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 1.7.4.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `-prod` flag for a production build.

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).

-->

# Depression Detection System by Analyzing Tweets

[![DOI](https://img.shields.io/badge/DOI-10.2139%2Fssrn.3358809-blue.svg)](https://dx.doi.org/10.2139/ssrn.3358809)

This project aims to develop a system that can detect signs of depression by analyzing tweets from Twitter. The system utilizes Natural Language Processing (NLP) techniques, machine learning algorithms, and the Twitter API to scrape and classify tweets, enabling the identification of major depression and bipolar disorder patterns.

![image](https://user-images.githubusercontent.com/20738263/145753373-3154b226-0d6b-401b-8bf2-246277f5991b.png)
![image](https://user-images.githubusercontent.com/20738263/145753413-e9cdd294-dc3f-4028-acb4-677d85818a94.png)
![image](https://user-images.githubusercontent.com/20738263/145753441-6953e800-3993-4707-86d0-0f49c5dd0751.png)
![image](https://user-images.githubusercontent.com/20738263/145753465-30a08396-cdbf-43aa-a370-fd9deaf93491.png)
![image](https://user-images.githubusercontent.com/20738263/145753488-2f683996-92c0-41ee-88aa-06caf72dec89.png)

## Motivation

With the rise of social media platforms, individuals are increasingly sharing their thoughts, emotions, and experiences online. This project leverages the wealth of data available on Twitter to detect and monitor potential signs of depression in a timely manner. Early detection and intervention can play a crucial role in preventing individuals from resorting to extreme measures and providing them with the necessary support and resources.

Developed a system that uses the Twitter API to scrape the real-time tweets, classified the tweets using Hybrid Naive Bayes and SVM model, and plotted a graph which was used to classify the depression into two categories Major depression and bipolar depression.

## Features

- **Tweet Scraping**: The system uses the Twitter API to scrape real-time tweets from specified user accounts or keyword searches.
- **Natural Language Processing**: Tweets are processed using NLP techniques, including tokenization, stop-word removal, and stemming/lemmatization, to extract relevant textual features.
- **Sentiment Analysis**: A Hybrid Naive Bayes and Support Vector Machine (NBSVM) model is employed to classify tweets based on their sentiment, distinguishing between positive and negative emotions.
- **Depression Classification**: By analyzing the patterns and trends in the classified tweets over time, the system can identify potential cases of major depression (characterized by persistent negative sentiment) and bipolar disorder (characterized by fluctuating sentiment).
- **Visualization**: The system generates visualizations, such as sentiment graphs, to aid in the interpretation and understanding of the analysis results.
- **Alerting and Reporting**: The system can send alerts and generate reports to concerned individuals or authorities, enabling timely intervention and support.

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/depression-detection-system.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Configure the Twitter API credentials by creating a `config.py` file and adding your API keys:

```python
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'
```

4. Run the application:

```
python app.py
```

## Usage

1. Enter the Twitter handle or keyword(s) for which you want to analyze tweets.
2. The system will scrape the relevant tweets and perform sentiment analysis and depression classification.
3. The results, including sentiment graphs and depression classification, will be displayed on the user interface.
4. Optionally, you can configure the system to send alerts or generate reports based on the analysis results.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgments

- [NLTK](https://www.nltk.org/) - Natural Language Toolkit
- [scikit-learn](https://scikit-learn.org/) - Machine Learning in Python
- [tweepy](https://www.tweepy.org/) - Twitter API library for Python

## References

- [Depression Detection using Emotion Artificial Intelligence](https://ieeexplore.ieee.org/document/8324195)
- [A content analysis of depression-related tweets](https://www.sciencedirect.com/science/article/pii/S0747563215301787)
