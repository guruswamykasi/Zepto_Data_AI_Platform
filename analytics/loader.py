import os
import pandas as pd
import seaborn as sns


class TitanicLoader:

    def load_dataset(self):
      
        print("Loading Titanic dataset...")

        df = sns.load_dataset("titanic")

        print("Dataset Loaded Successfully")

        return df

    def save_dataset(self, df):
        os.makedirs("analytics/data", exist_ok=True)

        df.to_csv("analytics/data/titanic.csv", index=False)

        print("Dataset saved successfully.")


    def load_from_csv(self):
     print("loading titanic dataset from CSV ..")    
     return pd.read_csv("analytics/data/titanic.csv")
  
        
        

        