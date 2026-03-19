def simple_neuron(input_value, weight, bias):
    # The Core Formula of AI: (Input * Weight) + Bias
    prediction = (input_value * weight) + bias
    
    # "Activation": If the result is > 5, the neuron 'fires' (Yes)
    return "YES! ✅" if prediction > 5 else "NO ❌"

# Test 1: High weight (Very important factor)
print(f"Is an Apple healthy? {simple_neuron(input_value=1, weight=10, bias=0)}")

# Test 2: Low weight (Not important factor)
print(f"Is a Donut healthy? {simple_neuron(input_value=1, weight=2, bias=0)}")
