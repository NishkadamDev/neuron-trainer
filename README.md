# 🧠 Neuron Trainer

> A neural network built from scratch — no libraries, just math, Python, and a Raspberry Pi.

---

## 🧠 About This Project

**Neuron Trainer** is a hand-coded single neuron (perceptron) that learns to classify whether a food is healthy or not based on its sugar level. No TensorFlow. No PyTorch. No shortcuts. Just raw Python math running on a Raspberry Pi 5 — demonstrating exactly how a neural network learns at the most fundamental level.

Claude helped design and debug the training logic.

---

## 🛠️ Tech Stack

| Layer | Tool |
|---|---|
| **Hardware** | Raspberry Pi 5 |
| **Language** | Python (no ML libraries) |
| **AI Assist** | Claude (Anthropic), Gemini (Google) |
| **Activation Function** | Sigmoid |
| **Optimizer** | Gradient Descent (manual) |

---

## ⚙️ How It Works

The neuron starts completely dumb — with a random weight and zero bias. Over 500 training epochs, it adjusts itself using gradient descent until it can correctly classify inputs.

### The Math
```
output = sigmoid(sugar × weight + bias)
error  = correct_answer - output
weight += learning_rate × error × sugar
bias   += learning_rate × error
```

### The Sigmoid Function
```python
def sigmoid(x):
    return 1 / (1 + (2.718 ** -x))
```
Squashes any number into a value between 0 and 1 — perfect for yes/no classification.

---

## 🍎 Training Data

| Sugar Level | Label |
|---|---|
| 0.9 | ✅ Healthy |
| 0.8 | ✅ Healthy |
| 0.7 | ✅ Healthy |
| 0.2 | ❌ Not Healthy |
| 0.1 | ❌ Not Healthy |
| 0.3 | ❌ Not Healthy |

---

## 📈 Training Output

```
=============================================
  🧠 NEURON TRAINING BEGINS
=============================================
Epoch  50 | Loss: 0.0821 | Weight: 2.1043 | Bias: -1.0021
Epoch 100 | Loss: 0.0412 | Weight: 2.8834 | Bias: -1.4211
...
Epoch 500 | Loss: 0.0023 | Weight: 5.1234 | Bias: -2.6891

✅ Training complete!

Testing the trained neuron:
  Sugar = 0.1 (Apple?)  → 0.08  ❌ Not healthy
  Sugar = 0.5 (Soda?)   → 0.51  ✅ Healthy
  Sugar = 0.9 (Candy?)  → 0.96  ✅ Healthy
```

---

## 💡 Key Learnings

- How a single neuron learns through gradient descent
- What weights and biases actually do mathematically
- Why the sigmoid function is used for binary classification
- How loss decreases over training epochs as the model improves
- The foundations that underpin every modern AI model

---

## 🚀 Part of the AI Bootcamp

This project was built during the **Week 2 Physical AI** phase of a 15-day AI Developer Bootcamp.  
See the full bootcamp repo → [The AI Bootcamp](../README.md)

---

*Every AI model in the world — GPT, Claude, Gemini — is just this, repeated billions of times.* 🤯
