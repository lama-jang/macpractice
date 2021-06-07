import torch
import numpy as np

# 데이터로부터 직접(directly) 생성하기:
data = [[1, 2],[3, 4]]
x_data = torch.tensor(data)
print(x_data)

# NumPy 배열로부터 생성하기:
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
print(x_np)

# 다른 텐서로부터 생성하기:

x_ones = torch.ones_like(x_data)    # x_data 속성 유지하기
print(f"Ones Tensor: \n {x_ones} \n")

x_rand = torch.rand_like(x_data, dtype=torch.float)    # x_data 속성 덮어쓰기
print(f"Random Tensor: \n {x_rand} \n")


# 무작위(random) 또는 상수(constant) 값을 사용하기:
shape = (2, 3, )
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)

print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor} \n")