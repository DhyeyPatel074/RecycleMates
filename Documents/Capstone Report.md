# Introduction
This project proposes the implementation of a recycling solution to reduce waste. The project focuses on the collection and sorting of materials for reuse. The goal of the project is to design and develop a recycling solution that utilizes image recognition technology for the categorization of recyclable waste. This solution aims to improve the accuracy, efficiency, and sustainability of waste management practices by automating the sorting and categorization process. The recycling solution is intended to be a cost-effective, user-friendly tool that promotes sustainability which can aid individuals and organizations in their recycling efforts. This project involves a comprehensive analysis of the current state of waste management practices, the potential of image recognition technology, and the development and testing of a prototype recycling solution. This report highlights the objectives, methodology, results, and implication of the recycling solution with the results on this project will contribute to the advancement of sustainable waste management practices and promote the adoption of innovative technologies in the recycling industry.

# Objectives
The main objective of the project is to design and develop an efficient and effective recycling solution that utilizes image recognition technology to categorize recyclable waste. The purpose of this research is to explore the feasibility of utilizing image recognition technology in the recycling sector and to assess its effectiveness in facilitating application waste management protocols as well as educating users on proper disposal practices.

Analyzing the current state of waste management practices: This objective involves conducting an in-depth evaluation of the prevailing waste management procedures in Windsor ON, the assessment comprises an examination of the present collection, and recycling facilities, along with an identification of the challenges and prospects for enhancement. The analysis will be based on on-site assessments to acquire a comprehensive perception of the extant waste management approaches.

Investigating the potential of image recognition technology: This objective entails studying in-depth the analysis of the prospective utility of image recognition for the purpose of categorizing recyclable waste. The investigation will include an exhaustive review of the relevant literature on image recognition technology and its practical applications in the field of waste management. Furthermore, the investigation will involve identifying and evaluating various image recognition algorithms and models to determine the optimal approach for the proposed recycling solution.

Designing and developing a recycling solution: This objective involves the conception, design and construction of a prototype recycling solution that leverages image recognition technology for the purpose of categorization of recyclable waste. The solution will be founded based on the analysis, scrutiny of existing waste management practices and the inquiry of image recognition technology. This solution will comprise a software component which will have two prominent features image recognition and a knowledge base of recycling waste. The image recognition component will be predicated on the elected image recognition algorithm and model will be fine-tuned for precision, speed and expandability.

Evaluating the effectiveness and efficiency of the developed recycling solution: This objective involves validation of the accuracy, speed, and user-friendliness of the developed recycling solution. The validation will be predicated on a series of trials that involves the procession of diverse categories of recyclable waste through the developed solution. The evaluation will also encompass user feedback and usability testing to identify areas that require enhancement and additional development. 

Providing recommendations for further development and improvement: This objective involves offering insights and recommendations for the further development and amelioration of the recycling solution. The recommendations will be based on the outcomes of the analytical, investigatory, and evaluating phases of the research project. The recommendations will focus on optimizing the performance of the recycling solution, enhancing its capabilities, and increasing its scalability.
The metrics used to gauge the effectiveness of this solution would be the % of recycle request the city of Windsor would receive.

# Related Works

Scrap Uncle: Scrap Uncle is a service that is currently being implemented in India. The service offers citizens the possibility to sell their recyclable trash by scheduling a pickup location. A company expert arrives at the location and gives the client a price estimation of their waste and gives a payment to the client. The service is implemented through a website and a mobile application. The user can schedule the pickup through the app or website, and the expert arrives at the scheduled time to evaluate and purchase the waste. The service is designed to promote the recycling of trash and reduce waste in landfills.

iRecycle: iRecycle is a mobile application that helps customers sort and bin their recyclable items. The app is implemented in various locations around the world, including the United States and Europe. The app allows users to browse for the materials they want to recycle and find the recyclers who will take them or inform them where they can drop their waste. The app provides information on recycling centers and other recycling-related information. The app is designed to promote recycling and make it easier for people to recycle their waste.

Recyclemap: Recyclemap is a nonprofit project that is implemented in various locations around the world, including the United States, Canada, and Europe. The project helps in waste segregation and residential waste recycling in local communities by providing easy access to information about the closest recycling point in their living area. The project also educates citizens about waste segregation and recycling so they can improve ecological situations. Recyclemap is implemented through a website and a mobile application. Users can access the website or app to find recycling points in their area, and they can also contribute by adding new recycling points to the map.

Overall, these initiatives aim to promote recycling and reduce waste in landfills. They are implemented through websites and mobile applications and are designed to make recycling easier for people. By promoting ethical practices, these initiatives ensure that they do not contribute to any negative impact on the environment or society.

# Methods

The Exploratory Data Analysis (EDA) process for a recycling app that is aimed to recycle glass bottles, tin cans, cardboard, and plastic bottles using object detection algorithm involves several methods to ensure the app is effective and efficient in achieving its objectives.

The first method is data collection. The app will require a large amount of data to train its object detection algorithm to recognize recyclable items accurately. The app developers can collect data by taking pictures of the recyclable items or sourcing for existing datasets. The collected data should be comprehensive, diverse, and relevant to ensure the object detection algorithm can accurately identify the recyclable items. Then, The collected data will require preprocessing to clean it and prepare it for analysis. Data preprocessing involves tasks such as data cleaning, data normalization, data transformation, and data reduction. These tasks ensure that the data is in the right format, is accurate, and is ready for analysis.

Data visualization involves creating visual representations of the data to help the developers and users of the app understand the data better. The developers can use visualizations such as histograms, scatter plots, and bar charts to understand the distribution of the data, identify patterns, and detect outliers.

Feature engineering involves selecting the most important features from the data and creating new features to improve the accuracy of the object detection algorithm. The developers can use techniques such as principal component analysis (PCA), feature selection algorithms, and clustering algorithms to identify the most important features.

Model building involves developing a machine learning model that can accurately detect and classify the recyclable items. The developers can use algorithms such as Convolutional Neural Networks (CNNs), Support Vector Machines (SVMs), and Random Forests to build the model. The model should be trained using the preprocessed data, and the performance should be evaluated using metrics such as accuracy, precision, and recall.

Model deployment involves integrating the trained model into the app and making it available to users. The app should have a user-friendly interface that allows users to take pictures of the recyclable items and receive a recycling price suggestion based on the number of items detected. The app should also notify pickers in the near me area about the ad posted about the recycling item along with the suggested price so that they can pick up the recyclables and take them to the nearest recycling place to get the approximate payment.

In conclusion, the EDA process for a recycling app that is aimed to recycle glass bottles, tin cans, cardboard, and plastic bottles using object detection algorithm involves several methods, including data collection, data preprocessing, data visualization, feature engineering, model building, and model deployment. The developers must ensure that the app is accurate, efficient, and user-friendly to achieve its objectives effectively. With a well-executed EDA process, the app can help reduce waste and improve the ecological situation by encouraging recycling.

# Dataset

Cleaning and processing data is a crucial step in any machine learning project, including the development of a recycling app that uses object detection algorithms to identify and price different recyclable items. The raw data collected from users' pictures can be messy and inconsistent, with a variety of errors and inaccuracies that can impact the accuracy of the model's predictions. Therefore, data cleaning and processing is necessary to ensure that the data is consistent, accurate, and ready for analysis and modeling. This bar plot represents the counts of objects that we are targeting:

![image](https://github.com/DhyeyPatel074/RecycleMates/assets/128725424/197cb2c9-6b67-4f18-aad2-3264a64f1cc5)


The first step in cleaning and processing the data is to ensure that the pictures are correctly identified and categorized based on the type of recyclable item they contain, such as glass bottles, tin cans, cardboard, or plastic bottles. This requires a combination of manual and automated processes, including image recognition algorithms that can analyze the pictures and identify the presence of different recyclable items. The manual processes involve trained personnel who can accurately identify and categorize the images and review them for any errors or inconsistencies. Here is images of the object that we are targeting in our project:

![image](https://github.com/DhyeyPatel074/RecycleMates/assets/128725424/f2e10093-f164-48d7-b6e7-c74aba61f8fc)

Once the images have been identified and categorized, the next step is to ensure that the data is consistent and accurate. This involves identifying and correcting any errors or inconsistencies in the data, such as missing values, duplicate entries, or incorrect labels. For example, if there are multiple entries for the same item with different labels or values, these must be corrected to ensure that the data is consistent and accurate.

The data must also be processed to ensure that it is in a format that can be easily analyzed and modeled. This includes converting the raw data into a structured format, such as a table or spreadsheet, with columns and rows that can be easily analyzed and manipulated. The data must also be transformed and cleaned to remove any outliers or anomalies that could skew the analysis or modeling.

During the cleaning and processing of the data, it is important to ensure that the privacy and security of users' data are protected. This includes ensuring that the data is stored securely and that access is restricted to authorized personnel only. The app must also comply with all relevant data protection and privacy regulations, such as GDPR or CCPA.

In conclusion, cleaning and processing data is an essential step in the development of a recycling app that uses object detection algorithms to identify and price different recyclable items. It involves a combination of manual and automated processes, including image recognition algorithms, manual categorization, and data processing and transformation. The aim is to ensure that the data is consistent, accurate, and in a format that can be easily analyzed and modeled while also maintaining the privacy and security of users' data. By taking these steps, the app can be developed with a high level of accuracy and reliability, making it a valuable tool in promoting recycling and environmental sustainability.

# Exploratory Data Analysis

Data Collection and Pre-processing: The first step in any data analysis project is to collect and clean the data. In the context of the recycling app, this would involve collecting images of the recyclable objects such as glass bottles, tin cans, cardboard, and plastic bottles. These images can be obtained from various sources such as the internet, social media platforms, or crowdsourcing. The data should be pre-processed to ensure that it is in a format that is suitable for analysis. This could involve resizing, normalizing, and cropping the images.

Data Visualization: Data visualization is a powerful tool for understanding the data and identifying patterns. Histograms and box plots can be used to visualize the distribution of the variables, while scatter plots can be used to visualize the relationship between variables. In the context of the recycling app, histograms and box plots can be used to visualize the distribution of the number of objects detected in each image, while scatter plots can be used to visualize the relationship between the type of object detected and the location where it was detected.

Statistical Analysis: Statistical analysis can provide insights into the dataset and help identify trends and patterns. Measures such as mean, median, mode, standard deviation, and variance can be used to describe the dataset. In the context of the recycling app, statistical analysis can be used to determine the average number of objects detected in each image and the distribution of the types of objects detected.

Machine Learning Techniques: Machine learning techniques such as clustering, dimensionality reduction, and classification can be used to identify patterns and relationships in the data. In the context of the recycling app, clustering can be used to group images with similar types and numbers of objects, while classification can be used to categorize images based on the type of object detected.

Data Augmentation: Data augmentation is the process of generating additional data from the existing dataset. This can be done by adding noise to the data, rotating the images, or flipping them horizontally or vertically. In the context of the recycling app, data augmentation can be used to generate additional images of the same objects from different angles and perspectives.

In summary, the EDA process for a recycling app that uses object detection algorithms involves collecting and pre-processing the data, visualizing the data using histograms, box plots, and scatter plots, conducting statistical analysis to describe the dataset, using machine learning techniques such as clustering and classification to identify patterns and relationships in the data, and using data augmentation to generate additional data. By conducting a thorough EDA process, we can gain a deeper understanding of the dataset and make informed decisions about the machine learning models that we develop for the recycling app.

# Application of the Five Ethics Principles


