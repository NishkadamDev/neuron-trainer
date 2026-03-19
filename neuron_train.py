import time

# --- TRAINING DATA ---
# (sugar_level, is_healthy?)  1 = healthy, 0 = not healthy
training_data = [
    (0.9, 1),   # High health score → Healthy
    (0.8, 1),
    (0.7, 1),
    (0.2, 0),   # Low health score → Not healthy
    (0.1, 0),
    (0.3, 0),
]

# --- NEURON STARTS DUMB ---
weight = 0.5   # Random starting guess
bias   = 0.0
learning_rate = 0.1

def sigmoid(x):
    return 1 / (1 + (2.718 ** -x))

def predict(sugar):
    return sigmoid(sugar * weight + bias)

# --- TRAINING LOOP ---
print("=" * 45)
print("  🧠 NEURON TRAINING BEGINS")
print("=" * 45)

for epoch in range(1, 501):
    total_loss = 0

    for sugar, correct_answer in training_data:
        guess = predict(sugar)
        error = correct_answer - guess
        total_loss += error ** 2

        weight += learning_rate * error * sugar
        bias   += learning_rate * error

    if epoch % 50 == 0:
        print(f"Epoch {epoch:>3} | Loss: {total_loss:.4f} | Weight: {weight:.4f} | Bias: {bias:.4f}")
        time.sleep(0.3)

print("\n✅ Training complete!\n")

# --- TEST IT ---
print("Testing the trained neuron:")
print(f"  Sugar = 0.1 (Apple?)  → {predict(0.1):.2f}  {'✅ Healthy' if predict(0.1) > 0.5 else '❌ Not healthy'}")
print(f"  Sugar = 0.5 (Soda?)   → {predict(0.5):.2f}  {'✅ Healthy' if predict(0.5) > 0.5 else '❌ Not healthy'}")
print(f"  Sugar = 0.9 (Candy?)  → {predict(0.9):.2f}  {'✅ Healthy' if predict(0.9) > 0.5 else '❌ Not healthy'}")
