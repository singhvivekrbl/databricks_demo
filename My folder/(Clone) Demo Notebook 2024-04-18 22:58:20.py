# Databricks notebook source
print("Hello World")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "hello World"

# COMMAND ----------

# MAGIC %run /Workspace/Users/singhvivek.rbl@gmail.com/Includes/Setups

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files= dbutils.fs.ls('/databricks-datasets')
files

# COMMAND ----------

display(files)

# COMMAND ----------


