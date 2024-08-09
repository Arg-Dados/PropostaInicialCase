from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType

# Schema dos dados oriundos dos arquivos csv que serão armazenados na pasta RAW
schema = StructType([
    StructField("TransactionNo", StringType(), True),
    StructField("Date", StringType(), True),
    StructField("ProductNo", StringType(), True),
    StructField("ProductName", StringType(), True),
    StructField("Price", DoubleType(), True),
    StructField("Quantity", IntegerType(), True),
    StructField("CustomerNo", DoubleType(), True),
    StructField("Country", StringType(), True)
])