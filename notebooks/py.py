import torch

print(f"PyTorch Version: {torch.__version__}")
print(f"Is CUDA available? {torch.cuda.is_available()}")

# Test with a random tensor
x = torch.rand(5, 3)
print(x)