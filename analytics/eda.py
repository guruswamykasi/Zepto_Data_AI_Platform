import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


class DataEDA:

    def __init__(self):

        os.makedirs("analytics/images", exist_ok=True)


    def age_histogram(self, df):
         plt.figure(figsize=(8,5))

         plt.hist(df["age"], bins=20)

         plt.title("Age Distribution")

         plt.xlabel("Age")

         plt.ylabel("Number of Passengers")

         plt.savefig("analytics/images/age_histogram.png")

         plt.close()

         print("Age Histogram Saved")

    def fare_histogram(self, df):

      plt.figure(figsize=(8,5))

      plt.hist(df["fare"], bins=20)

      plt.title("Fare Distribution")

      plt.xlabel("Fare")

      plt.ylabel("Passengers")

      plt.savefig("analytics/images/fare_histogram.png")

      plt.close()

      print("Fare Histogram Saved")     

    def age_boxplot(self, df):

        plt.figure(figsize=(6,5))

        plt.boxplot(df["age"])

        plt.title("Age Box Plot")

        plt.savefig("analytics/images/age_boxplot.png")

        plt.close()

        print("Age Box Plot Saved")  

    def fare_boxplot(self, df):

        plt.figure(figsize=(6,5))

        plt.boxplot(df["fare"])

        plt.title("Fare Box Plot")

        plt.savefig("analytics/images/fare_boxplot.png")

        plt.close()

        print("Fare Box Plot Saved")   

    def calculate_outliers(self, df, column):

        q1 = df[column].quantile(0.25)

        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr

        upper = q3 + 1.5 * iqr

        outliers = df[(df[column] < lower) | (df[column] > upper)]

        print("\nColumn :", column)

        print("Q1 :", q1)

        print("Q3 :", q3)

        print("IQR :", iqr)

        print("Outlier Count :", len(outliers))    

    def fare_statistics(self, df):

        mean = df["fare"].mean()

        median = df["fare"].median()

        mode = df["fare"].mode()[0]

        print("\nFare Statistics")

        print("Mean :", mean)

        print("Median :", median)

        print("Mode :", mode)


    def fare_skewness(self, df):

        mean = df["fare"].mean()

        median = df["fare"].median()

        mode = df["fare"].mode()[0]

        print("\nSkewness Analysis")

        if mean > median > mode:

            print("Fare is Right Skewed")

        elif mean < median < mode:

            print("Fare is Left Skewed")

        else:

            print("Fare distribution is approximately Symmetric")   

    def survival_by_gender(self, df):

        print("\n========== Survival Rate by Gender ==========\n")

        survival = (
            df.groupby("sex")["survived"]
            .mean()
            .mul(100)
            .round(2)
        )

        print(survival)

    def survival_by_class(self, df):

        print("\n========== Survival Rate by Passenger Class ==========\n")

        survival = (
            df.groupby("pclass")["survived"]
            .mean()
            .mul(100)
            .round(2)
        )

        print(survival)

    def survival_by_gender_and_class(self, df):

        print("\n========== Survival by Gender and Class ==========\n")

        survival = (
            df.groupby(["sex", "pclass"])["survived"]
            .mean()
            .mul(100)
            .round(2)
        )

        print(survival)      

    def correlation_matrix(self, df):

        columns = [
        "survived",
        "pclass",
        "age",
        "sibsp",
        "parch",
        "fare"
        ]

        corr = df[columns].corr()

        print("\nCorrelation Matrix\n")

        print(corr)

        return corr     

    def correlation_heatmap(self, corr):

        plt.figure(figsize=(8,6))

        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm"
        )

        plt.title("Titanic Correlation Heatmap")

        plt.savefig("analytics/images/correlation_heatmap.png")

        plt.close()

        print("Heatmap Saved")

    def strongest_correlations(self, corr):

        print("\n========== Strongest Correlations ==========\n")

        pairs = []

        columns = corr.columns

        for i in range(len(columns)):
            for j in range(i + 1, len(columns)):

                pairs.append((
                    columns[i],
                    columns[j],
                    corr.iloc[i, j]
                ))

        pairs = sorted(
            pairs,
            key=lambda x: abs(x[2]),
            reverse=True
        )

        for first, second, value in pairs[:2]:

            print(
                f"{first} <-> {second} : {value:.3f}"
            )




    