print("Hello World!")
def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Các Accuracy Score của 6 mô hình
accuracy_scores = [98.4, 98.2, 94.9, 96.4, 99.4, 99.4]

# Tính tổng Accuracy Score
total_accuracy = sum(accuracy_scores)

# Tính trọng số cho mỗi mô hình
weights = [score / total_accuracy for score in accuracy_scores]

# In trọng số tương ứng với mỗi mô hình
for i, weight in enumerate(weights, 1):
    print(f"Trọng số cho mô hình #{i}: {weight:.3f}")
