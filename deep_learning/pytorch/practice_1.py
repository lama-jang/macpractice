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

# 텐서의 속성 확인
tensor = torch.rand(3,4)

print(f"Shape of Tensor: {tensor.shape}")
print(f"Datatype of Tensor: {tensor.dtype}")
print(f"Device tensor is sotred on: {tensor.device}")

# 텐서의 연산
# GPU가 존재하면 텐서를 이동
if torch.cuda.is_available():
    tensor = tensor.to('cuda')

# NumPy식의 표준 인덱싱과 슬라이싱:
tensor = torch.ones(4,4)
print('First row: ',tensor[0])
print('First column: ',tensor[:,0])
print('Last column: ', tensor[...,-1])
tensor[:,1] = 0
print(tensor)

t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(t1)

 # 두 텐서 간의 행렬 곱(matrix multiplication)을 계산합니다. y1, y2, y3은 모두 같은 값을 갖습니다.
 y1 = tensor @ tensor.T
 y2 = tensor.matmul(tensor.T)

 y3 = torch.rand_like(tensor)
 torch.matmul(tensor, tensor.T, out=y3)
