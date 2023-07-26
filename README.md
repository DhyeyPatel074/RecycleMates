# Image-Based Classification for Recycling Objects
This research focuses on developing an image-based classification system for recycling objects, targeting four key items: cardboard, tin, glass, and plastic bottles. Leveraging Convolutional Neural Networks (CNNs), our aim is to enhance waste sorting accuracy and efficiency through automated object classification. Unlike conventional methods, our approach classifies one item at a time, ensuring greater precision while simplifying the process.  

![image](https://github.com/DhyeyPatel074/RecycleMates/assets/128725424/0403d9bf-cebc-4ad7-a1d1-955e64f46000)



## Table of content
- [Vision](#-vision)
- [Problem Statement](#-problem-statement)
- [Proposed Solution](#-proposed-solution)
- [Dataset](#-dataset)
   - [Data Source ](#data-source )
   - [Preprocessing](#preprocessing)
- [Methods of Analysis](#-methods-of-analysis)
   - [Model Results](#model-results)
   - [Shiny for Python](#shiny-for-python)
- [Conclusion](#-conclusion)
- [Future Enhancements](#-future-enhancements)
- [Re-Create Steps](#%EF%B8%8F-re-create-steps)
- [References](#-references)
- [Contributors](#%EF%B8%8F-contributors)


-------------------------------------------------------------------------------------------------------------
## 🔭 Vision

The motivation behind this study lies in the escalating waste diversion rate and increasing unsolved recycle requests in Windsor, Ontario. With a waste diversion rate of approximately 32 percent as of 2021, there is a pressing need to improve recycling efforts. By automating the classification process, we envision contributing to Windsor's recycling rate enhancement and fostering a more sustainable and eco-friendly community. Through this report, we aim to shed light on the challenges faced by Windsor and offer a practical solution to streamline waste management. Embracing technology, we strive to create a greener future, where recycling practices play a pivotal role in mitigating environmental impact. 

![image](https://github.com/DhyeyPatel074/RecycleMates/assets/128725424/2cdbe7e8-34a8-40bb-a72d-c3332fbd3058)

![image](https://github.com/DhyeyPatel074/RecycleMates/assets/128725424/445b9ec5-ac5e-4d29-80f0-da048d1c005b)


-------------------------------------------------------------------------------------------------------------
## 🪨 Problem Statement

Recycling plays a crucial role in promoting sustainable waste management practices and mitigating environmental issues. However, with escalating recycling challenges, the need for efficient solutions has become evident. The city of Windsor faces a pressing concern regarding the increasing number of unsolved recycling requests, resulting in a surge in waste collection demands annually.  

-------------------------------------------------------------------------------------------------------------
## 💎 Proposed Solution

To address this issue, our research aims to develop an image-based classification system for recycling objects, with a specific focus on four key items: cardboard, tin, glass, and plastic bottles. Utilizing Convolutional Neural Networks (CNNs), our primary objective is to enhance waste sorting accuracy and efficiency through automated object classification.  

Unlike traditional approaches that handle multiple items simultaneously, our methodology concentrates on classifying one object at a time, ensuring greater precision and simplifying the classification process. The motivation behind this research arises from the growing waste diversion rate and the urgency to improve recycling efforts. By automating the classification process and focusing on the specified items, we envision contributing significantly to Windsor's recycling rate enhancement and fostering a more sustainable, eco-friendly community. 

-------------------------------------------------------------------------------------------------------------
## 💾 Dataset

Our research mainly focuses on the classification of Plastic Bottles, Glass Bottles, Cans, and Cardboard of no specific shape or color. The dataset was compiled using various sources from Kaggle, along with additional images captured by team members using their smartphone devices. The combination of data from Kaggle and self-taken images ensures a diverse and comprehensive dataset for our research. The combined dataset provided a total of 5,520 images used for the analysis. 

![image](https://github.com/DhyeyPatel074/RecycleMates/assets/128725424/16af60fa-3b6d-45a2-84cd-b7888d507239)

-------------------------------------------------------------------------------------------------------------
### Data Source 


| Dataset | Provided by | Source
|-|-|-|
| Plastic - Paper - Garbage Bag Synthetic Images | Marionette | [Kaggle[3]](https://www.kaggle.com/datasets/vencerlanz09/plastic-paper-garbage-bag-synthetic-images)  |
| Garbage Classification (12 classes) | Mostafa Mohamed | [Kaggle[4]](https://www.kaggle.com/datasets/mostafaabla/garbage-classification )  |
| Drinking Waste Classification | Arkadiy Serezhkin | [Kaggle[5]](https://www.kaggle.com/datasets/arkadiyhacks/drinking-waste-classification )  |
| Alcohol Bottle Images - Glass Bottles | Data Cluster Labs | [Kaggle[6]](https://www.kaggle.com/datasets/dataclusterlabs/alcohol-bottle-images-glass-bottles )  |
| Waste Classification data | Sashaank Sekhar  | [Kaggle[7]](https://www.kaggle.com/datasets/techsash/waste-classification-data )  |

-------------------------------------------------------------------------------------------------------------
### Preprocessing

In our research, we took great care to avoid using repetitive images during dataset preprocessing to mitigate the risk of overfitting in our model. Our primary objective was to prevent the model from memorizing the training data excessively, as overfitting can lead to poor generalization on new data. By ensuring that the model focuses on learning essential patterns and features rather than memorizing specific examples, we aimed to enhance its ability to make accurate predictions on unseen data. This approach yielded a more robust and reliable model that exhibited improved performance beyond the training set.  

-------------------------------------------------------------------------------------------------------------
#### Number of images by class


![image](https://github.com/DhyeyPatel074/RecycleMates/assets/128725424/35fdb9cc-1da8-4495-8ad9-0ca69af1f2e5)

-------------------------------------------------------------------------------------------------------------
#### Sample of the data

![image](https://github.com/DhyeyPatel074/RecycleMates/assets/128725424/031129bf-c767-4a50-bc7a-7a0aa38f6b89)
![image](https://github.com/DhyeyPatel074/RecycleMates/assets/128725424/637cbbf3-ce66-4667-b117-381606c28b40)
![image](https://github.com/DhyeyPatel074/RecycleMates/assets/128725424/d945f009-a13d-40b0-9343-76d19ef5dfc2)


-------------------------------------------------------------------------------------------------------------
## 🪄 Methods of Analysis


In this research, the methodology comprises two key stages: system design and Testing, and model development. The first stage involves designing the system to outline the overall approach and Performing thorough testing through the application to assess its functionality and performance.  

Subsequently, in the second stage, the focus shifts to model development, where we construct the core components of the system.  

In addition to the aforementioned approach, the report also provides a concise overview of the various libraries and tools utilized throughout the study. Notably, the paper extensively employs essential libraries, each serving specific purposes in the project. These crucial libraries include but are not limited to:  

1. TensorFlow: An essential deep learning library, utilized for building and training neural networks. 
2. Matplotlib: Employed for creating visualizations and plots to analyze data distributions and model performance. 
3. Pandas: A powerful data manipulation library, that facilitates data cleaning, aggregation, and exploration. 
4. PIL / Pillow: Employed for image processing tasks, such as loading, resizing, and converting images. 

### Model Results

During the development of our object classification application, we performed extensive experimentation with various CNN models, each having different numbers of CNN layers. After rigorous evaluation, we identified the best-performing model, which achieved an impressive accuracy of 94% on the validation dataset. This model was deemed highly suitable for our application's prototype. With the chosen CNN model in place, we proceeded to integrate it into our object classification system. The results were remarkable, demonstrating a significantly high level of accuracy in classifying objects into four distinct categories: glass bottles, tin cans, plastic bottles, and cardboard.  

Precision:  
- The model achieved the highest precision for the "plastic bottle" class with 98%. This means that when the model predicted an image as a plastic bottle, it was correct 98% of the time.
- The "can," "cardboard," and "glass bottle" classes also have good precision values, ranging from 88% to 91%. It indicates that the model made relatively accurate predictions for these classes as well.

Recall:  
- The model achieved the highest recall for the "can," "glass bottle," and "plastic bottle" classes, all with 94%. This means that the model was able to correctly identify 94% of the samples belonging to these classes out of the total number of samples of that class.
- The "cardboard" class has a lower recall of 80%, indicating that the model struggled to identify some samples belonging to this class.

F1-score:  
- The "plastic bottle" class has the highest F1-score of 96%. This metric considers both precision and recall, making it a good measure of overall performance for imbalanced datasets.
- The "can" and "glass bottle" classes also have high F1-scores of 93% and 91%, respectively, showing that the model performed well in terms of both precision and recall for these classes.
- The "cardboard" class has a relatively lower F1-score of 84%, which could be due to the lower recall for this class.  

| Metric | Can | Cardboard | Glass bottle | Plastic Bottle
|-|-|-|-|-|
| Precision | 91% | 88% | 88% | 98% |
| Recall | 94% | 80% | 94% | 94% |
| F1-Score | 93% | 84% | 91% | 96% |
| Support | 153 | 89 | 138 | 172 |

![image](https://github.com/DhyeyPatel074/RecycleMates/assets/128725424/6b1dd740-8046-4f29-aab0-bd73461900a1)


-------------------------------------------------------------------------------------------------------------
<img src="https://github.com/DhyeyPatel074/RecycleMates/assets/128725424/1678abb6-cb1e-4a08-aeb1-11f794bedf91" alt="image" width="200" height="100">  

### Shiny for Python

The proposed solution is an App Recycle Classifier, which uses image classification for categorizing the Object. The application utilizes a camera-based system to classify recyclable objects. By capturing an image, the model can identify the object and provide guidance on the appropriate drop-off location for potential refunds, if applicable. This technology simplifies the recycling process by accurately categorizing items and directing users to the most suitable recycling points.  

The presented Python application is an interactive and user-friendly platform that allows users to classify objects in images and explore their locations on a map. The application is built using Shiny for Python, a web framework for creating data visualization apps.  

The app consists of three main sections: "App Information," "Request Submission," and "Map." In the "App Information" section, general details about the application and its purpose are displayed, providing users with a brief introduction.

![image](https://github.com/DhyeyPatel074/RecycleMates/assets/128725424/acf4af6e-c46d-48c9-9811-fd7d02543f80)

In the "Request Submission" section, users can easily upload images by clicking the "Open camera" button. After uploading an image, the app uses a pre-trained neural network to predict what type of object is in the image. The results are presented in the form of a simple bar chart, indicating the probabilities of the image containing a "Can," "Cardboard," "Glass bottle," or "Plastic Bottle." This visual representation helps users understand the classification results quickly and intuitively.  

![image](https://github.com/DhyeyPatel074/RecycleMates/assets/128725424/d5975ea2-df85-4560-93d9-c5200e405e3d)

The "Map" section provides an interactive experience, allowing users to choose different map styles, such as "OpenStreetMap" or "Satellite." The map is cantered at a specific location, and a marker is placed there.  

![image](https://github.com/DhyeyPatel074/RecycleMates/assets/128725424/939ebef1-8560-43b2-837f-9553cbac4c70)

Overall, this application is designed to be user-friendly and intuitive, catering to a wide range of users, regardless of their technical expertise. It enables users to easily classify objects in images, understand the prediction results, and visualize the geographical locations related to the images. The simplicity and functionality of the Shiny framework make it an excellent choice for developing such interactive data visualization apps. 

-------------------------------------------------------------------------------------------------------------
## 🥁 Conclusion
* Businesses can make data-driven choices with model insights.
* Engaging with recycling facilities boosts sustainability impact.
* The interface allows users to validate classifications.
* RecyclingMates' CNN model achieves 94% accuracy, enhancing recycling efforts.
* Increasing the number of samples for the "cardboard" class in the dataset.
* The model evolves to match changing recycling trends.

-------------------------------------------------------------------------------------------------------------
## 🛠️ Future Enhancements

* Enable simultaneous classification of multiple recyclable objects for increased versatility.
* Regularly update CNN models using transfer learning and additional data for adaptability.
* Develop a user-friendly app for on-the-go object classification and environmental awareness.
* Collaborate on AI-powered bins for automated sorting based on RecyclingMates' results.
* Optimize recycling facilities with RecyclingMates' AI integration.
* Foster recycling awareness through partnerships and educational initiatives.
* Provide data-driven insights into recycling habits and trends.
* Offer multi-language support for global accessibility.

-------------------------------------------------------------------------------------------------------------
## 🖇️ Re-Create Steps


-------------------------------------------------------------------------------------------------------------
## 📄 References


-------------------------------------------------------------------------------------------------------------
## ⚙️ Contributors


All participants in this project are Students of Post Graduate Diploma in Data Analytics for Business @ St Clair College

* Alejandro Rodriguez Orama
  * Email: AR156@myscc.ca
  * GitHub: [github.com/arol9204](github.com/arol9204)

* Dhyey Shaileshkumar Patel
  * Email: DP250@myscc.ca
  * GitHub: [github.com/Dp74](github.com/Dp74)

* Nelson Nwachia
  * Email: NN141@myscc.ca
  * GitHub: [github.com/nelsonnwachia](github.com/nelsonnwachia)

* Arzitha Rachakonda
  * Email: AR123@myscc.ca
  * GitHub: [github.com/arzi67](github.com/arzi67)



