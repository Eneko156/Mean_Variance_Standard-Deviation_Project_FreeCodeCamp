import numpy as np

def calculate(list):
  array = np.array(list)
  if len(array) < 9:
    raise ValueError ("List must contain nine numbers.")
  matrix = array.reshape(3,3)
  mean = []
  variance = []
  standard_deviation = []
  maxi = []
  mini = []
  addition = []
  for going_through in range(2):
    mean.append(matrix.mean(axis = going_through).tolist())
    variance.append(matrix.var(axis = going_through).tolist())
    standard_deviation.append(matrix.std(axis = going_through).tolist())
    maxi.append(matrix.max(axis = going_through).tolist())
    mini.append(matrix.min(axis = going_through).tolist())
    addition.append(matrix.sum(axis = going_through).tolist())
  mean.append(array.mean())
  variance.append(array.var())
  standard_deviation.append(array.std())
  maxi.append(array.max())
  mini.append(array.min())
  addition.append(array.sum())
  return {
  'mean': mean,
  'variance': variance,
  'standard deviation': standard_deviation,
  'max': maxi,
  'min': mini,
  'sum': addition
  }