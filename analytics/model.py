import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.pipeline import Pipeline

from sklearn.compose import ColumnTransformer

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.impute import SimpleImputer

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import GridSearchCV

from imblearn.over_sampling import SMOTE

from imblearn.pipeline import Pipeline as ImbPipeline
from sklearn.linear_model import LinearRegression


from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
    RocCurveDisplay
)

import matplotlib.pyplot as plt
import os
import joblib

from sklearn.model_selection import GridSearchCV

from imblearn.over_sampling import SMOTE

from imblearn.pipeline import Pipeline as ImbPipeline

class TitanicModel:

    def __init__(self):

        os.makedirs("analytics/images", exist_ok=True)

        print("Titanic Machine Learning Started")

    def split_dataset(self, df):

        features = [

            "pclass",

            "sex",

            "age",

            "sibsp",

            "parch",

            "fare",

            "embarked"
        ]

        target = "survived"

        X = df[features]

        y = df[target]

        X_train, X_test, y_train, y_test = train_test_split(

            X,

            y,

            test_size=0.20,

            random_state=42,

            stratify=y

        )

        print()

        print("Training Records :", len(X_train))

        print("Testing Records :", len(X_test))

        return X_train, X_test, y_train, y_test


    def build_preprocessor(self):

        numeric_columns = [

       "age",

        "fare",

        "sibsp",

        "parch",

        "pclass"
    ]

        numeric_pipeline = Pipeline(

        steps=[

            (

                "imputer",

                SimpleImputer(strategy="median")

            ),

            (

                "scaler",

                StandardScaler()

            )

        ]

        )

        categorical_columns = [

        "sex",

        "embarked"
        ]

        categorical_pipeline = Pipeline(

        steps=[

            (

                "imputer",

                SimpleImputer(strategy="most_frequent")

            ),

            (

                "encoder",

                OneHotEncoder(handle_unknown="ignore")

            )

        ]

        )


        preprocessor = ColumnTransformer(

        transformers=[

            (

                "numeric",

                numeric_pipeline,

                numeric_columns

            ),

            (

                "categorical",

                categorical_pipeline,

                categorical_columns

            )

        ]

        )
    
        return preprocessor

    def train_logistic(
            self,
            preprocessor,
            X_train,
            y_train
        ):

        pipeline = Pipeline(

            [

                ("preprocessor", preprocessor),

                ("model", LogisticRegression(max_iter=1000))

            ]

        )

        pipeline.fit(X_train, y_train)

        return pipeline

    def train_tree(
            self,
            preprocessor,
            X_train,
            y_train
        ):

        pipeline = Pipeline(

            [

                ("preprocessor", preprocessor),

                ("model", DecisionTreeClassifier(random_state=42))

            ]

        )

        pipeline.fit(X_train, y_train)

        return pipeline

    def train_forest(
            self,
            preprocessor,
            X_train,
            y_train
        ):

        pipeline = Pipeline(

            [

                ("preprocessor", preprocessor),

                (
                    "model",

                    RandomForestClassifier(random_state=42)
                )

            ]

        )

        pipeline.fit(X_train, y_train)

        return pipeline

    def evaluate_model(

            self,

            model,

            X_test,

            y_test,

            name

        ):

        predictions = model.predict(X_test)

        probabilities = model.predict_proba(X_test)[:,1]
 
        accuracy = accuracy_score(
            y_test,
            predictions
        )

        precision =  precision_score(
            y_test,
            predictions
        )

        recall = recall_score(
            y_test,
            predictions
        )

        f1 = f1_score(
            y_test,
            predictions
        )

        auc = roc_auc_score(
            y_test,
            probabilities
        )
        print("\n========================")
        print(name)
        print("========================")

        print("Accuracy :", accuracy)
        print("Precision :", precision)
        print("Recall :", recall)
        print("F1 :", f1)
        print("AUC :", auc)

        print("\nConfusion Matrix")

        print(
            confusion_matrix(
                y_test,
                predictions
            )
        )

        RocCurveDisplay.from_estimator(

            model,

            X_test,

            y_test

        )

        plt.savefig(f"analytics/images/{name}_roc.png")

        plt.close()
        return{
            "Model":name,
            "Accuracy":accuracy,
            "Precision":precision,
            "Recall":recall,
            "F1":f1,
            "AUC":auc
        }

    def save_tree(

            self,

            tree_pipeline

        ):

        feature_names = tree_pipeline.named_steps[
            "preprocessor"
            ].get_feature_names_out()

        tree = tree_pipeline.named_steps["model"]

        plt.figure(figsize=(20,10))

        plot_tree(

            tree,

            feature_names=feature_names,

            class_names=["Dead","Survived"],

            filled=True

        )

        plt.savefig("analytics/images/decision_tree.png")

        plt.close()    

    def class_balance(self, y):

        print("\n===== Class Balance =====")

        counts = y.value_counts()

        percentages = (counts / len(y) * 100).round(2)

        print(pd.DataFrame({
            "Count": counts,
            "Percentage": percentages
        }))

    def baseline_model(self, preprocessor, X_train, y_train):

        pipeline = Pipeline([
            ("preprocessor", preprocessor),
            ("model", RandomForestClassifier(random_state=42))
        ])

        pipeline.fit(X_train, y_train)
        return pipeline

    def balanced_model(self, preprocessor, X_train, y_train):

        pipeline = Pipeline([
            ("preprocessor", preprocessor),
            ("model",
                RandomForestClassifier(
                    random_state=42,
                    class_weight="balanced"
                )
            )
        ])

        pipeline.fit(X_train, y_train)

        return pipeline

    def smote_model(self, preprocessor, X_train, y_train):

        pipeline = ImbPipeline([

            ("preprocessor", preprocessor),

            ("smote", SMOTE(random_state=42)),

            ("model",
                RandomForestClassifier(
                    random_state=42
                )
            )
        ])

        pipeline.fit(X_train, y_train)

        return pipeline

    def compare_models(
            self,
            models,
            X_test,
            y_test
        ):

        results = []

        for name, model in models.items():

            pred = model.predict(X_test)

            results.append({

                "Model": name,

                "Precision": precision_score(y_test, pred),

                "Recall": recall_score(y_test, pred),

                "F1": f1_score(y_test, pred)

            })

        result_df = pd.DataFrame(results)

        print(result_df)

        return result_df

    def tune_random_forest(
            self,
            preprocessor,
            X_train,
            y_train
        ):

        pipeline = Pipeline([

            ("preprocessor", preprocessor),

            ("model",
                RandomForestClassifier(
                    random_state=42,
                    oob_score=True,
                    bootstrap=True
                )
            )

        ])

        parameters = {

            "model__n_estimators": [100, 200],

            "model__max_depth": [5, 10, None],

            "model__max_features": ["sqrt", "log2"]

        }

        grid = GridSearchCV(

                pipeline,

                parameters,

                cv=5,

                scoring="accuracy",

                n_jobs=-1

        )

        grid.fit(X_train, y_train)

        print("\nBest Parameters")

        print(grid.best_params_)

        best_pipeline = grid.best_estimator_

        print("\nOOB Score")

        print(best_pipeline.named_steps["model"].oob_score_)

        return best_pipeline

    def train_regression(self, df):

        features = [
            "pclass",
            "sex",
            "age",
            "sibsp",
            "parch",
            "embarked"
        ]

        X = df[features]

        y = df["fare"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42
        )

        numeric_columns = [
            "pclass",
            "age",
            "sibsp",
            "parch"
        ]

        categorical_columns = [
            "sex",
            "embarked"
        ]

        numeric_pipeline = Pipeline([
            (
                "imputer",
                SimpleImputer(strategy="median")
            ),
            (
                "scaler",
                StandardScaler()
            )
        ])

        categorical_pipeline = Pipeline([
            (
                "imputer",
                SimpleImputer(strategy="most_frequent")
            ),
            (
                "encoder",
                OneHotEncoder(handle_unknown="ignore")
            )
        ])

        preprocessor = ColumnTransformer([
            (
                "numeric",
                numeric_pipeline,
                numeric_columns
            ),
            (
                "categorical",
                categorical_pipeline,
                categorical_columns
            )
        ])

        pipeline = Pipeline([
            (
                "preprocessor",
                preprocessor
            ),
            (
                "model",
                LinearRegression()
            )
        ])

        pipeline.fit(X_train, y_train)

        predictions = pipeline.predict(X_test)

        return pipeline, y_test, predictions, X_test

    def evaluate_regression(
            self,
            y_test,
            predictions,
            pipeline,
            X_test
        ):

        mae = mean_absolute_error(
            y_test,
            predictions
        )

        rmse = np.sqrt(
            mean_squared_error(
                y_test,
                predictions
            )
        )

        r2 = r2_score(
            y_test,
            predictions
        )

        transformed_X = pipeline.named_steps[
            "preprocessor"
        ].transform(X_test)

        p = transformed_X.shape[1]

        n = len(y_test)

        adjusted_r2 = (1- ((1 - r2) * (n - 1)) / (n - p - 1))

        print("\n========== Regression Results ==========")

        print("MAE :", round(mae, 4))

        print("RMSE :", round(rmse, 4))

        print("R2 :", round(r2, 4))

        print("Adjusted R2 :", round(adjusted_r2, 4))

        return {
            "MAE": mae,
            "RMSE": rmse,
            "R2": r2,
            "Adjusted R2": adjusted_r2
        }

    def residual_plot(
            self,
            y_test,
            predictions
        ):

        residuals = y_test - predictions

        plt.figure(figsize=(8, 5))

        plt.scatter(
            predictions,
            residuals
        )

        plt.axhline(
            y=0,
            linestyle="--"
        )

        plt.xlabel("Predicted Fare")

        plt.ylabel("Residual")

        plt.title("Fare Regression Residual Plot")

        plt.savefig(
            "analytics/images/fare_residual_plot.png"
        )

        plt.close()

        print(
            "Saved fare_residual_plot.png"
        )

    def save_pipeline(self, pipeline):

        joblib.dump(
            pipeline,
            "analytics/titanic_best_pipeline.joblib"
        )

        print("Complete pipeline saved successfully")    

    def load_pipeline(self):

        pipeline = joblib.load(
            "analytics/titanic_best_pipeline.joblib"
        )

        print("Pipeline loaded successfully")

        return pipeline




