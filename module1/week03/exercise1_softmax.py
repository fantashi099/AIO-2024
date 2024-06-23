import torch
from torch import nn
import numpy as np


class Softmax(nn.Module):
    """
    Perform Softmax with exp(xi) / Sum of exp(xj) for j from 0 -> n-1
    """
    def __init__(self,):
        super().__init__()
    

    def forward(self, x: torch.tensor, dim: int = None):
        if not dim:
            dim = -1
        output = torch.e ** x 
        output = output / torch.sum(output, axis=dim, keepdim=True)
        return output
    

class SoftmaxStable(nn.Module):
    """
    Perform Softmax with exp(xi - c) / Sum of exp(xj - c) for j from 0 -> n-1 and c = max(x)
    """
    def __init__(self,):
        super().__init__()
    

    def forward(self, x: torch.tensor, dim: int = None):
        if not dim:
            dim = -1
        c = np.max(x.numpy(), axis=dim, keepdims=True)
        output = torch.e ** (x - c)
        output = output / torch.sum(output, axis=dim, keepdim=True)
        return output


if __name__ == '__main__':
    sample_input = torch.tensor([[1,2,3], [1,2,3]]).float()
    softmax_fn = Softmax()
    softmax_stable_fn = SoftmaxStable()
    output = softmax_fn(sample_input)
    print('Softmax:')
    print(output)
    print('Softmax Stable:')
    output = softmax_stable_fn(sample_input)
    print(output)