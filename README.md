# **Amazon Stock Price Prediction utilizing Sentiment Analysis and LSTM models.**
## *Project Description*
  This project combines Selenium for automated news article collection, pandas for data preprocessing, the Yahoo Finance Python API for retrieving historical stock price data, TensorFlow for building an LSTM-based forecasting model, and matplotlib for result visualization.
  The goal is to evaluate how sentiment analysis can improve time series forecasting, specifically in the context of stock price prediction. Instead of using broad market indices such as the FTSE 100 or the S&P 500, this project focuses on an individual company—Amazon (AMZN)
  —to reduce inherent model bias caused by long-term index stability. Amazon provides a balance between steady growth and sufficient volatility, enabling more meaningful evaluation of sentiment-driven forecasting performance.
## *Data Collection and Preprocessing*
  To ensure compatibility with the forecasting model, all data are collected and structured in CSV format. Manual collection would be time-consuming and error-prone, so Selenium is used to automate the extraction of financial news articles from Investing.com.
  Unlike many similar projects that process full article content, this approach uses only article headlines as model inputs. Headlines often capture the core topic and sentiment of an article while significantly reducing computational overhead and data collection time.
  After the news data are collected, they are merged with historical stock price data, and sentiment analysis is computed for each headline. While Selenium is effective, it can be relatively slow; therefore, future iterations of this project will transition to the Crawl4AI API, which offers improved performance with lower computational requirements.
## *Sentiment Analysis*
  Multiple sentiment analysis models were evaluated for this project, including FINBERT and VADER, both implemented using Hugging Face pipelines. After empirical comparison, VADER produced the most accurate and consistently distributed sentiment predictions, both at the text level and in terms of overall model performance.
  As a result, VADER was selected as the primary sentiment analysis method for the final pipeline, providing a reliable balance between predictive stability and computational efficiency.
## *Model Architecture*
  The forecasting model is built using a four-layer LSTM architecture, with 100 neurons per layer. Maintaining a consistent number of neurons across all LSTM layers produced the most stable results, aligning well with the recurrent nature of LSTMs and their ability to capture long-term temporal dependencies.
  The network concludes with a single-neuron output layer, responsible for predicting the target stock price value.
  
  ![Screenshot](Final%20Graphs/Screenshot%202025-05-24%20222332.png)

## *Data Windowing Strategy*
  The data-splitting strategy follows the approach used by Alison Mitchell in her stock prediction project, where the time series is divided into 60-day sliding windows, each shifted forward by one day to generate the next prediction. This windowing method allows the model to learn temporal patterns across a meaningful historical context.
  A 30-day window was also evaluated; however, the 60-day split consistently produced better results and was therefore selected for the final model configuration.

  ![Final Result](Final%20Graphs/Screenshot%202025-05-24%20201837.png)

### *Daily Changes in Stock Price*

![VADER Difference](Final%20Graphs/60%20days%20graphs/VADER_Difference.png)
  
## *Model Evaluation*
  Model performance was evaluated by comparing the loss functions across different configurations. A comparative chart was created to visualize how each model performed under varying sentiment input strategies.
  For BERT-based models, different setups were tested, including using only sentiment labels, only confidence scores, and combinations of both. Similarly, multiple VADER configurations were evaluated, ranging from using 
  only the compound score to incorporating all sentiment indicators. This experimentation helped identify the configuration that yielded the best overall performance. Those distinctions are shown on the history of the graph.
 ### *BERT*
 
  ![BERT Model Comparison](Final%20Graphs/60%20days%20graphs/BERT_Comparison_Between_models.png)

### *VADER*

![VADER 60-Day Comparison](Final%20Graphs/60%20days%20graphs/VADER_60_Day_COmparison.png)


### *Confusion Matrix*
  To assess real-world applicability, a confusion matrix was computed to evaluate the model’s performance in a simulated trading environment. The model achieved an average daily trading accuracy of 53%, indicating predictive capability above random chance but not yet at a level suitable for reliable trading deployment.
  While the results are not ideal, they highlight clear avenues for improvement. Enhancements to the model architecture, along with higher-quality and more informative news data, are expected to further improve predictive accuracy in future iterations.
  
  <p align="center">
    <img src="Final%20Graphs/60%20days%20graphs/Confusion_Matrix.png" width="500">
  </p>

## *Data Sources*
Investing.com for the articles and YFinance for historical price data.


  
  
