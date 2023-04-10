import torch
import numpy as np

#initializing a tensor to be used directly from data

data = [[1,2],[3,4]]
x_data = torch.tensor(data)

#initializing tensor from tensor
x_ones = torch.ones_like(x_data) #tensor of all ones
print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float)
print(f"Random Tensor: \n {x_rand} \n")

print(f"Data Tensor: \n {x_data} \n")