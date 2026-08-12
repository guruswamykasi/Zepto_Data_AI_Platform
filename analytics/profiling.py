class DataProfiler:

    def print_shape(self, df):

        print("\nDataset Shape")

        print(df.shape)

    def print_info(self, df):

        print("\nDataset Information")

        print(df.info())

    def print_statistics(self, df):

        print("\nDataset Statistics")

        print(df.describe(include="all"))