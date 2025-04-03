# from torch.utils.data import DataLoader
from torchvision import datasets

train_set = datasets.MNIST(root="data/mnist_data", train=True, download=True)
test_set = datasets.MNIST(root="data/mnist_data", train=False, download=True)
