import torch
from torch import nn
from torch.nn import functional as F
from torch import optim

import torchvision

traindb = torchvision.datasets.MNIST(root="data/mnist_data", train=True, download=True)
