import torch

tc = torch.tensor([0.5, 14.0, 15.0, 28.0, 11.0, 8.0, 3.0, -4.0, 6.0, 13.0, 21.0])
tu = torch.tensor([35.7, 55.9, 58.2, 81.9, 56.3, 48.9, 33.9, 21.8, 48.4, 60.4, 68.4])

tun = tu * 0.1


def model(tu, w, b):
    return w * tu + b


def lossfn(tp, tc):
    sqdiff = (tp - tc) ** 2
    return sqdiff.mean()


nsamples = tu.shape[0]
nval = int(0.2 * nsamples)
shuffled_idx = torch.randperm(nsamples)

train_idx = shuffled_idx[:-nval]
val_idx = shuffled_idx[-nval:]

print(train_idx)
print(val_idx)
