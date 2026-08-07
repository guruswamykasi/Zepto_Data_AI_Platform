import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.pipeline import Pipeline

from sklearn.compose import ColumnTransformer

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.impute import SimpleImputer

class TitanicModel:

    def __init__(self):
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





