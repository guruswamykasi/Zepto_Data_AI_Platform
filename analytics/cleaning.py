import pandas as pd


class DataCleaner:

    def show_missing_percentage(self, df):

        print("\n ========= Missing value report ==========\n")

        missing = df.isnull().sum()

        missing_percent = (missing / len(df)) * 100

        report = pd.DataFrame({
            "Missing Count": missing,
            "Missing %": missing_percent.round(2)
        })

        report = report[report["Missing Count"] > 0]

        print(report)

        return report

    def clean_dataset(self, df):

        print("\n Cleaning Dataset....\n")

        cleaned_df = df.copy()

        cleaned_df.dropna(
            subset=["embarked", "embark_town"],
            inplace=True
        )


        age_median = cleaned_df["age"].median()

        cleaned_df["age"] = cleaned_df["age"].fillna(age_median)

        cleaned_df.drop(columns=["deck"], inplace=True)

        print("\nRemaining Missing values\n")

        print(cleaned_df.isnull().sum())

        return cleaned_df