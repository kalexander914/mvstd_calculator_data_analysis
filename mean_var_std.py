import numpy as np

def calculate(list):

#Conditional Statement of length list smaller than 9
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

#create 3x3 matrix
  else:
    array_list = np.array(list).reshape((3, 3))

#create glossary for arithmetic operations

  arithmetic = {
    'mean': [
      np.mean(array_list, axis = 0).tolist(),
      np.mean(array_list, axis = 1).tolist(),
      np.mean(array_list).tolist()],

    'variance': [
      np.var(array_list, axis = 0).tolist(),
      np.var(array_list, axis = 1).tolist(),
      np.var(array_list).tolist()],

    'standard deviation': [
      np.std(array_list, axis = 0).tolist(),
      np.std(array_list, axis = 1).tolist(),
      np.std(array_list).tolist()],

    'max': [
      np.max(array_list, axis = 0).tolist(),
      np.max(array_list, axis = 1).tolist(),
      np.max(array_list).tolist()],

    'min': [
      np.min(array_list, axis = 0).tolist(),
      np.min(array_list, axis = 1).tolist(),
      np.min(array_list).tolist()],

    'sum': [
      np.sum(array_list, axis = 0).tolist(),
      np.sum(array_list, axis = 1).tolist(),
      np.sum(array_list).tolist()]
  }

  return arithmetic
