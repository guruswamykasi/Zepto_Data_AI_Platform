from loader import TitanicLoader
from profiling import DataProfiler
from cleaning import DataCleaner
from eda import DataEDA
from model import TitanicModel


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

eda = DataEDA()

eda.age_histogram(clean_df)

eda.fare_histogram(clean_df)

eda.age_boxplot(clean_df)

eda.fare_boxplot(clean_df)

eda.calculate_outliers(clean_df, "age")

eda.calculate_outliers(clean_df, "fare")

eda.fare_statistics(clean_df)

eda.fare_skewness(clean_df)

eda.survival_by_gender(clean_df)

eda.survival_by_class(clean_df)

eda.survival_by_gender_and_class(clean_df)

corr = eda.correlation_matrix(clean_df)

eda.correlation_heatmap(corr)

eda.strongest_correlations(corr)

eda.chart_survival_by_gender(clean_df)

eda.chart_survival_by_class(clean_df)

eda.chart_age_survival(clean_df)

eda.chart_fare_survival(clean_df)

standard_df = eda.standardize_features(clean_df)

model = TitanicModel()

X_train, X_test, y_train, y_test = model.split_dataset(clean_df)

preprocessor = model.build_preprocessor()

print(preprocessor)