import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LinearRegression


class Dataset:
    def __init__(self, path_to_file: str):
        self.__data = pd.read_csv(path_to_file)
        self.X = None  # Features
        self.y = None  # Target variable

    def get_data(self) -> pd.DataFrame:
        """Returns the data."""
        return self.__data

    def remove_outliers(self, column: str, threshold: float = 0.99) -> pd.DataFrame:
        """Removes outliers in the specified column."""
        if column not in self.__data.columns:
            raise ValueError(f"Column '{column}' not found in data.")
        q = self.__data[column].quantile(threshold)
        self.__data = self.__data[self.__data[column] <= q]
        return self.__data

    def fill_missing(self, strategy: str = 'mode', value: float = None):
        """Fills missing values in the data."""
        strategies = ['mode', 'mean', 'median', 'constant']
        if strategy not in strategies:
            raise ValueError(f"Unsupported strategy. Choose from {strategies}.")
        for column in self.__data.columns:
            if self.__data[column].isnull().sum() > 0:
                if strategy == 'mode':
                    mode_val = self.__data[column].mode()[0]
                    self.__data[column].fillna(mode_val, inplace=True)
                elif strategy == 'mean':
                    mean_val = self.__data[column].mean()
                    self.__data[column].fillna(mean_val, inplace=True)
                elif strategy == 'median':
                    median_val = self.__data[column].median()
                    self.__data[column].fillna(median_val, inplace=True)
                elif strategy == 'constant':
                    if value is not None:
                        self.__data[column].fillna(value, inplace=True)
                    else:
                        raise ValueError("Value must be provided for 'constant' strategy.")

    def identify_categorical(self, threshold: int = 10) -> list:
        """Identifies categorical features based on unique value count."""
        if threshold is None:
            threshold = self.__data.shape[0]
        categorical_cols = []
        for column in self.__data.columns:
            unique_count = self.__data[column].nunique()
            if unique_count <= threshold:
                categorical_cols.append(column)
        return categorical_cols

    def encode_categorical(self, categorical_cols: list, strategy: str = 'OneHot'):
        """Encodes categorical features."""
        if strategy == 'Label':
            encoder = LabelEncoder()
            for col in categorical_cols:
                self.__data[col] = encoder.fit_transform(self.__data[col])
        elif strategy == 'OneHot':
            encoder = OneHotEncoder(sparse_output=False, drop='first')
            for col in categorical_cols:
                one_hot = encoder.fit_transform(self.__data[[col]])
                one_hot_df = pd.DataFrame(one_hot, columns=encoder.get_feature_names_out([col]))
                self.__data = pd.concat([self.__data, one_hot_df], axis=1)
                self.__data.drop(columns=[col], inplace=True)
        else:
            raise ValueError("Unsupported encoding strategy. Choose 'Label' or 'OneHot'.")

    def prepare_data(self, target_column: str, threshold: int = 10, fill_strategy: str = 'mean', encode_strategy: str = 'OneHot'):
        """Prepares data for analysis, excluding the target column from encoding."""
        self.fill_missing(strategy=fill_strategy)
        categorical_cols = self.identify_categorical(threshold=threshold)
        # Exclude the target column from categorical encoding
        categorical_cols = [col for col in categorical_cols if col != target_column]
        self.encode_categorical(categorical_cols, strategy=encode_strategy)
        self.split_data(target_column)

    def split_data(self, target_column: str):
        """Splits data into features (X) and target variable (y)."""
        if target_column not in self.__data.columns:
            raise ValueError(f"Target column '{target_column}' not found in data.")
        self.X = self.__data.drop(columns=[target_column])
        self.y = self.__data[target_column]

    def display_stat(self):
        """Displays main statistical information."""
        print(self.__data.head(5))
        print(self.__data.info())
        for col in self.__data.select_dtypes(include=['int64', 'float64']).columns:
            print(f"Statistics for column '{col}':")
            print(f"Non-null count: {self.__data[col].count()}")
            print(f"Mean: {self.__data[col].mean()}")
            print(f"Max: {self.__data[col].max()}")
            print(f"Min: {self.__data[col].min()}\n")
            self.__data[col].plot(kind='hist', figsize=(10, 5), grid=True, title=f'Histogram of {col}')
            plt.show()

    def transform(self, to_tensor: str = 'numpy'):
        """Converts data into tensors for selected libraries."""
        if to_tensor == 'numpy':
            return self.X.to_numpy(), self.y.to_numpy()
        elif to_tensor == 'pytorch':
            '''self.X и self.y, представленные в виде значений,
            преобразуются в тензоры с типом данных float32.'''
            import torch
            return torch.tensor(self.X.values, dtype=torch.float32), torch.tensor(self.y.values, dtype=torch.float32)
        elif to_tensor == 'tensorflow':
            import tensorflow as tf
            return tf.convert_to_tensor(self.X.values, dtype=tf.float32), tf.convert_to_tensor(self.y.values, dtype=tf.float32)
        else:
            raise ValueError("Only 'numpy', 'pytorch', and 'tensorflow' are supported.")

    def cross_validate(self, model, cv: int = 5, scoring: str = 'r2'):
        """Performs cross-validation for the model."""
        if self.X is None or self.y is None:
            raise ValueError("Data not split into features and target. Call split_data().")
        scores = cross_val_score(model, self.X, self.y, cv=cv, scoring=scoring)
        print(f"Cross-validation scores: {scores}")
        print(f"Mean score: {np.mean(scores)}")
        return scores


# Example usage
data1 = Dataset('/content/gym_members_exercise_tracking.csv')
data1.prepare_data(target_column='Age', fill_strategy='mode', encode_strategy='OneHot')
data1.display_stat()

# Transform data into tensors
X_np, y_np = data1.transform(to_tensor='numpy')

# Cross-validation
from sklearn.linear_model import LinearRegression
model = LinearRegression()
data1.cross_validate(model, cv=5, scoring='r2')
