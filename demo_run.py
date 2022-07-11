# Databricks notebook source
# MAGIC %sh ls -l

# COMMAND ----------

from file_utils import add_one
add_one(10)

# COMMAND ----------

from notebook_utils import double
double(10)

# COMMAND ----------

# MAGIC %sh cp -r . /tmp/testcp

# COMMAND ----------

name = "demo_run"
print("name value before %run:", name)

# COMMAND ----------

# MAGIC %run ./notebook_utils

# COMMAND ----------

double(10)

# COMMAND ----------

# notebook_utils also defines a name variable, which overrides the name variable in this notebook
print("name value after %run:", name)

# COMMAND ----------


