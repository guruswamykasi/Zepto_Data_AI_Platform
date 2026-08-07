from loader import TitanicLoader
from profiling import DataProfiler


print("Welcome to Zepto Analytics Pipeline")


loader = TitanicLoader()

df = loader.load_dataset()

loader.save_dataset(df)

profiler = DataProfiler()

profiler.print_shape(df)

profiler.print_info(df)

profiler.print_statistics(df)