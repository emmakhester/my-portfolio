import numpy as np

# Pretty simple, as numpy provides functions for all of these statistics.
def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  # Convert list into a 3x3 numpy array and create an empty dictionary
  mx = np.array(list).reshape(3, 3)
  calculations = {}

  # As these numpy functions return arrays, use .tolist() to convert them
  calculations['mean'] = [
    np.mean(mx, axis=0).tolist(), np.mean(mx, axis=1).tolist(),
    np.mean(mx)
  ]
  calculations['variance'] = [
    np.var(mx, axis=0).tolist(), np.var(mx, axis=1).tolist(),
    np.var(mx)
  ]
  calculations['standard deviation'] = [
    np.std(mx, axis=0).tolist(), np.std(mx, axis=1).tolist(),
    np.std(mx)
  ]
  calculations['max'] = [np.max(mx, axis=0).tolist(), np.max(mx, axis=1).tolist(), np.max(mx)]
  calculations['min'] = [np.min(mx, axis=0).tolist(), np.min(mx, axis=1).tolist(), np.min(mx)]
  calculations['sum'] = [np.sum(mx, axis=0).tolist(), np.sum(mx, axis=1).tolist(), np.sum(mx)]

  return calculations