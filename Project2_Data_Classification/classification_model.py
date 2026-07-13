import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    """
    Main function to execute the machine learning classification pipeline 
    on the Iris dataset using K-Nearest Neighbors (KNN).
    """
    
    # ==========================================
    # Step 1: Load dataset
    # ==========================================
    print("--- Step 1: Loading Iris Dataset ---")
    iris = load_iris()
    print("Dataset loaded successfully.\n")

    # ==========================================
    # Step 2: Create a pandas DataFrame
    # ==========================================
    print("--- Step 2: Creating Pandas DataFrame ---")
    # We build the DataFrame using the features (iris.data) and column names (iris.feature_names)
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    # We add the target class integers to the DataFrame for exploratory analysis
    df['target'] = iris.target
    print("DataFrame created successfully.\n")

    # ==========================================
    # Step 3: Display basic dataset information
    # ==========================================
    print("--- Step 3: Displaying Dataset Information ---")
    print(f"Dataset Shape (Rows, Columns): {df.shape}")
    print(f"Column Names: {list(df.columns)}")
    print("\nFirst Five Rows of the Dataset:")
    print(df.head())
    print(f"\nTarget Class Integers: {np.unique(iris.target)}")
    print(f"Target Class Names: {list(iris.target_names)}\n")

    # ==========================================
    # Step 4: Separate Features (X) and Target (y)
    # ==========================================
    print("--- Step 4: Separating Features and Target ---")
    # Features (X) are the measurement columns (Sepal and Petal details)
    X = df.drop(columns=['target'])
    # Target (y) is the categorical classification index (0, 1, or 2)
    y = df['target']
    print("Features (X) and Target (y) separated.\n")

    # ==========================================
    # Step 5: Split dataset (80% Training, 20% Testing)
    # ==========================================
    print("--- Step 5: Splitting Dataset ---")
    # Split using train_test_split from scikit-learn
    # We use random_state=42 to guarantee reproducibility of the split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, 
        test_size=0.2, 
        random_state=42
    )
    print(f"Training Samples (80%): {len(X_train)}")
    print(f"Testing Samples (20%): {len(X_test)}\n")

    # ==========================================
    # Step 6: Create classifier and Train the model
    # ==========================================
    print("--- Step 6: Training K-Nearest Neighbors Classifier ---")
    # Create the classifier. We set n_neighbors to 3 (a standard choice for Iris)
    model = KNeighborsClassifier(n_neighbors=3)
    # Train the model with training features and labels
    model.fit(X_train, y_train)
    print("Model training complete.\n")

    # ==========================================
    # Step 7: Predict test samples
    # ==========================================
    print("--- Step 7: Predicting Test Samples ---")
    # Run predictions on the unseen test features
    y_pred = model.predict(X_test)
    print("Predictions generated on test data.\n")

    # ==========================================
    # Step 8: Calculate Accuracy Score
    # ==========================================
    print("--- Step 8: Calculating Model Accuracy ---")
    # Compare predictions to actual values
    accuracy = accuracy_score(y_test, y_pred)
    accuracy_percentage = accuracy * 100
    print(f"Model Accuracy: {accuracy_percentage:.2f}%\n")

    # ==========================================
    # Step 9: Print Accuracy, Predictions, and Actual Values
    # ==========================================
    print("--- Step 9: Predictions vs Actual Values ---")
    print(f"Overall Accuracy: {accuracy_percentage:.2f}%")
    print(f"Predicted Labels: {list(y_pred)}")
    print(f"Actual Labels:    {list(y_test.values)}\n")

    # ==========================================
    # Step 10: Display sample predictions in a readable format
    # ==========================================
    print("--- Step 10: Sample Predictions (Class Names) ---")
    # Display the actual and predicted name for the test samples in a tabular format
    print(f"{'Sample #':<10}{'Predicted Species':<20}{'Actual Species':<20}{'Status':<10}")
    print("-" * 60)
    
    # We display up to 10 sample predictions
    for i in range(min(10, len(y_test))):
        pred_name = iris.target_names[y_pred[i]]
        act_name = iris.target_names[y_test.values[i]]
        status = "Correct" if pred_name == act_name else "Incorrect"
        print(f"Sample {i+1:<3}: {pred_name:<20}{act_name:<20}{status:<10}")
    print()

    # ==========================================
    # Optional Visualization: Generate a scatter plot
    # ==========================================
    print("--- Optional: Generating Feature Scatter Plot ---")
    plt.figure(figsize=(8, 6))
    
    # Plotting Sepal Length vs Sepal Width
    sepal_length_col = iris.feature_names[0]
    sepal_width_col = iris.feature_names[1]
    
    colors = ['#FF5733', '#33FF57', '#3357FF']  # Custom modern colors for classes
    
    # Draw scatter points for each category
    for class_idx, color, label in zip([0, 1, 2], colors, iris.target_names):
        subset = df[df['target'] == class_idx]
        plt.scatter(
            subset[sepal_length_col],
            subset[sepal_width_col],
            color=color,
            label=label.capitalize(),
            edgecolors='black',
            s=60,
            alpha=0.8
        )
    
    # Add titles and labels for clean aesthetics
    plt.title("Iris Dataset: Sepal Length vs Sepal Width", fontsize=14, fontweight='bold', pad=15)
    plt.xlabel(sepal_length_col.title(), fontsize=12)
    plt.ylabel(sepal_width_col.title(), fontsize=12)
    plt.legend(title="Species", fontsize=10, title_fontsize=11)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    
    # Save the output visualization image to disk
    output_filename = "iris_feature_plot.png"
    plt.savefig(output_filename, dpi=150)
    print(f"Scatter plot visualization successfully saved to: {output_filename}\n")

if __name__ == "__main__":
    main()
