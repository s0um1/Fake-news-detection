# FakeNewsBot
Detects fake news from text, text from images and identifies morphed images.

Natural language processing techniques and machine learning algorithms are used to classifty fake news using python libraries. 

#### Dataset used
The data source used for this project is LIAR dataset in tsv format. The dataset used for this project were in csv format named train.csv, test.csv and valid.csv.

### File descriptions

#### DataPrep.py
This file contains all the pre processing functions needed to process all input documents and texts. First we read the train, test and validation data files then performed some pre processing like tokenizing, stemming etc. There are some exploratory data analysis is performed like response variable distribution and data quality checks like null or missing values etc.

#### FeatureSelection.py
In this file we have performed feature extraction and selection methods from sci-kit learn python libraries. For feature selection, we have used methods like simple bag-of-words and n-grams and then term frequency like tf-tdf weighting. we have also used word2vec and POS tagging to extract the features, though POS tagging and word2vec has not been used at this point in the project.

#### classifier.py
Here we have build all the classifiers for predicting the fake news detection. The extracted features are fed into different classfiers. We have used Naive-bayes, Logistic Regression, Linear SVM, Stochastic gradient decent and Random forest classifiers from sklearn. Each of the extracted featues were used in all of the classifiers. Once fitting the model, we compared the f1 score and checked the confusion matrix. After fitting all the classifiers, 2 best peforming models were selected as candidate models for fake news classification. We have performed parameter tuning by implementing GridSearchCV methos on these candidate models and chosen best performing paramters for these classifier. Finally selected model was used for fake news detection with the probability of truth. In Addition to this, We have also extracted the top 50 features from our term-frequency tfidf vectorizer to see what words are most and important in each of the classes. We have also used Precision-Recall and learning curves to see how training and test set performs when we increase the amount of data in our classifiers.

#### prediction.py
Our finally selected and best performnig classifer was ```Logistic Regression``` which was then saved on disk with name ```final_model.sav```. Once you close this repository, this model will be copied to user's machine and will be used by prediction.py file to classify the fake news. It takes an news article as input from user then model is used for final classification output that is shown to user along with probability of truth.
