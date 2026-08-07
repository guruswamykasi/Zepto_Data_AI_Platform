from loader import TitanicLoader
from profiling import DataProfiler
from cleaning import DataCleaner


print("Welcome to Zepto Analytics Pipeline")


loader = TitanicLoader()

df = loader.load_dataset()

loader.save_dataset(df)

profiler = DataProfiler()

profiler.print_shape(df)

profiler.print_info(df)

profiler.print_statistics(df)

cleaner = DataCleaner()

cleaner.show_missing_percentage(df)

clean_df = cleaner.clean_dataset(df)

print("\nClean Dataset Shape")

print(clean_df.shape)

clean_df.to_csv("analytics/data/titanic_clean.csv", index=False)