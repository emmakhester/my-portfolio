== Specifications ==
This project creates a function in mean_var_std.py named calculate() that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
The input of the function should be a list containing 9 numbers. The function converts the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.
The returned dictionary follows this format:
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}

If a list containing more or less than 9 elements is passed into the function, it raises a ValueError exception. The function returns lists and not Numpy arrays.