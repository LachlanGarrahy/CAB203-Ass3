import numpy as np
import numpy.linalg
import csv

def fertiliser(csvfilename, n, p, k):
  # set initial values
  unknown = []
  percent = [[],[],[]]
  # create matrix t as the weights required
  t = np.array([n,p,k], dtype=numpy.float64)

  # read values from the csv
  with open(csvfilename, 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)
    for row in csvreader:
      unknown.append(row[0])
      percent[0].append(row[1])
      percent[1].append(row[2])
      percent[2].append(row[3])
  
  a = np.array(percent, dtype=numpy.float64)/100 # create the matrix in numpy
  if (np.linalg.det(a) == 0): return None # check if the matrix can be inverted through the determinate
  aInv = np.linalg.inv(a) # invert the matrix
  s = np.around(aInv@t, decimals=2) # multiply the inverted matrix a with the matrix t

  if (True in (s < 0)): return None # check if any values in s are below zero (cant have negative weight)

  # set result to the name and weight of each fertilizer
  result = {
      unknown[0]: s[0],
      unknown[1]: s[1],
      unknown[2]: s[2]
  }

  return (result)