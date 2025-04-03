import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
import cv2
import numpy as np
from torch.utils.data import DataLoader

batch_size = 16
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
ephochs = 10
pipeline = transforms.Compose(
    [transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))]
)

train_set = datasets.MNIST(
    "data/mnist_data", train=True, download=False, transform=pipeline
)
test_set = datasets.MNIST(
    "data/mnist_data", train=False, download=False, transform=pipeline
)

train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_set, batch_size=batch_size, shuffle=True)

with open("data/mnist_data/MNIST/raw/t10k-images-idx3-ubyte", "rb") as f:
    image_data = f.read(16 + 784)[16:]
img_np = np.frombuffer(image_data, dtype=np.uint8).reshape(28, 28)
cv2.imshow("digit.jpg", img_np)
cv2.waitKey(0)
# import matplotlib.pyplot as plt

# plt.imshow(img_np)
# plt.show()
