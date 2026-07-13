# Data Classification Using Artificial Intelligence

A simple, beginner-friendly Machine Learning project to classify flowers from the famous Iris dataset using Python and the K-Nearest Neighbors (KNN) algorithm.

This project is part of the DecodeLabs Artificial Intelligence Industrial Training Project 2.

---

## 🎯 Objective
The primary objective of this project is to build an AI classification model that can learn from measurements of Iris flowers (features) and predict the correct species (class) of unseen flowers with high accuracy.

---

## 🔍 Project Overview
Classification is a fundamental task in Machine Learning. In this project, we:
1. **Load** the standard Iris dataset.
2. **Explore** its structure using `pandas`.
3. **Preprocess & split** the data into 80% training and 20% testing sets.
4. **Train** a K-Nearest Neighbors (KNN) classifier.
5. **Predict** classes on the test set.
6. **Evaluate** accuracy and print sample predictions.
7. **Visualize** the features using a clean scatter plot.

---

## 🛠️ Technologies Used
- **Language**: Python 3.x
- **Libraries**:
  - `numpy`: For numerical computations and array operations.
  - `pandas`: For structured data manipulation (DataFrames).
  - `scikit-learn`: For dataset loading, train-test splitting, training the model, and calculating accuracy.
  - `matplotlib`: For generating the feature visualization scatter plot.

---

## 📊 Dataset Used
We use the **Iris Dataset** directly imported from `scikit-learn` (`sklearn.datasets.load_iris`).
It contains **150 samples** of Iris flowers from three species:
- `Iris-setosa` (Class 0)
- `Iris-versicolor` (Class 1)
- `Iris-virginica` (Class 2)

Each sample has **4 features**:
1. Sepal Length (cm)
2. Sepal Width (cm)
3. Petal Length (cm)
4. Petal Width (cm)

---

## 📁 Project Structure
```text
Data Classification Using AI/
│
├── classification_model.py   # Main Python script containing the ML pipeline
├── iris_feature_plot.png     # Generated feature visualization plot (Sepal Length vs Sepal Width)
├── requirements.txt          # Project library dependencies
├── .gitignore                # File specifying files to ignore in Git
└── README.md                 # Project documentation and guide
```

---

## 🚀 Installation & Setup

Follow these steps to set up and run the project locally.

### 1. Clone or Download the Project
Ensure you are in the project folder directory:
```bash
cd "Data Classification Using AI"
```

### 2. Create a Virtual Environment (Optional but Recommended)
Creating a virtual environment ensures that the libraries installed do not conflict with other Python projects on your computer.
- **Windows**:
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
- **macOS / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
Install all required libraries using the provided `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## 🏃 How to Run
Execute the main classification script using the terminal:
```bash
python classification_model.py
```

---

## 📈 Expected Output & Example Log
Upon running the script, you should see the following steps and output printed to your console:

```text
--- Step 1: Loading Iris Dataset ---
Dataset loaded successfully.

--- Step 2: Creating Pandas DataFrame ---
DataFrame created successfully.

--- Step 3: Displaying Dataset Information ---
Dataset Shape (Rows, Columns): (150, 5)
Column Names: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'target']

First Five Rows of the Dataset:
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  target
0                5.1               3.5                1.4               0.2       0
1                4.9               3.0                1.4               0.2       0
2                4.7               3.2                1.3               0.2       0
3                4.6               3.1                1.5               0.2       0
4                5.0               3.6                1.4               0.2       0

Target Class Integers: [0 1 2]
Target Class Names: ['setosa', 'versicolor', 'virginica']

--- Step 4: Separating Features and Target ---
Features (X) and Target (y) separated.

--- Step 5: Splitting Dataset ---
Training Samples (80%): 120
Testing Samples (20%): 30

--- Step 6: Training K-Nearest Neighbors Classifier ---
Model training complete.

--- Step 7: Predicting Test Samples ---
Predictions generated on test data.

--- Step 8: Calculating Model Accuracy ---
Model Accuracy: 100.00%

--- Step 9: Predictions vs Actual Values ---
Overall Accuracy: 100.00%
Predicted Labels: [1, 0, 2, 1, 1, 0, 1, 2, 1, 1, 2, 0, 0, 0, 0, 1, 2, 1, 1, 2, 0, 2, 0, 2, 2, 2, 2, 2, 0, 0]
Actual Labels:    [1, 0, 2, 1, 1, 0, 1, 2, 1, 1, 2, 0, 0, 0, 0, 1, 2, 1, 1, 2, 0, 2, 0, 2, 2, 2, 2, 2, 0, 0]

--- Step 10: Sample Predictions (Class Names) ---
Sample #  Predicted Species   Actual Species      Status    
------------------------------------------------------------
Sample 1  : versicolor          versicolor          Correct   
Sample 2  : setosa              setosa              Correct   
Sample 3  : virginica           virginica           Correct   
Sample 4  : versicolor          versicolor          Correct   
Sample 5  : versicolor          versicolor          Correct   
Sample 6  : setosa              setosa              Correct   
Sample 7  : versicolor          versicolor          Correct   
Sample 8  : virginica           virginica           Correct   
Sample 9  : versicolor          versicolor          Correct   
Sample 10 : versicolor          versicolor          Correct   

--- Optional: Generating Feature Scatter Plot ---
Scatter plot visualization successfully saved to: iris_feature_plot.png
```

Additionally, a scatter plot named `iris_feature_plot.png` will be generated in the project directory showing the distribution of the different classes based on Sepal Length and Sepal Width.

---

## 🎁 Bonus Section: AI & Machine Learning Fundamentals

Here are simple explanations of core machine learning concepts for beginners:

### 1. What is Classification?
**Classification** is a process in machine learning where the computer learns to categorize input data into distinct groups or "classes". 
* *Real-world analogy:* It is like sorting mail into "Spam" and "Inbox" folders, or looking at a fruit and deciding if it is an "Apple", "Orange", or "Banana". In this project, the model classifies flowers into "Setosa", "Versicolor", or "Virginica".

### 2. What is Supervised Learning?
**Supervised Learning** is a type of machine learning where the model is trained using labeled data. This means that for every training sample, we provide both the features (the question) and the correct label (the answer). The model learns the relationship between the features and the labels.
* *Real-world analogy:* It is like a student learning with the help of a teacher who marks their practice test answers as correct or incorrect. The student corrects their mistakes using the provided answers.

### 3. Why was KNN (K-Nearest Neighbors) Selected?
**K-Nearest Neighbors (KNN)** is a simple, intuitive classification algorithm. It works on the principle that "similar things exist in close proximity." To classify a new data point, KNN looks at the $K$ closest labeled data points in the training set and assigns the class that is most common among those neighbors.
* **Why it fits this project:**
  1. **Simplicity**: It requires no complex mathematical assumptions or intensive optimization to understand.
  2. **No Training Time**: KNN is a "lazy learner"—it just stores the training data and does the calculations only during prediction.
  3. **High Effectiveness**: It performs exceptionally well on clean, small, and distinct datasets like the Iris dataset.

---

## 🔮 Future Improvements
1. **Try other algorithms**: Compare the results of KNN with alternative classifiers like a *Decision Tree Classifier* or *Support Vector Machines (SVM)*.
2. **Feature Scaling**: Apply feature scaling (e.g., standardizing features using `StandardScaler`) to check if it improves prediction performance for datasets with widely different scales.
3. **Cross-Validation**: Use K-Fold Cross-Validation to get a more robust and reliable estimate of the model's performance.
