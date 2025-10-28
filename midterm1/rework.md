# Midterm Rework  
#### Nate Lehnhof  
---

### **Question 6**  

> **Problem:**  
> Consider the same function  
> \[
> f(x) = x^2 \sin(x) + \ln(x)
> \]  
> where we are still interested in the derivative at \( x = 2 \).  
> What is the **absolute error** between forward differencing with a step size of \( 1 \times 10^{-6} \) and central differencing with a step size of \( 1 \times 10^{-4} \)?  
>  
> The error is: [some number] × 10^[exponent\].  
> What is the **exponent**?

**My error:**  
I mistakenly read the problem as asking for **relative error** and multiplied by 100 to get a percentage.  
My initial answer was **–4** because of this unnecessary multiplication.  

✅ **Correct answer:** –6  

### **Code Reference**
```python
def f(x):
    return x**2 * np.sin(x) + np.log(x)

def forward(f, xj, step=1e-6):
    return (f(xj+step) - f(xj)) / (xj+step - xj)

def central(f, xj, step=1e-4):
    return (f(xj+step)-f(xj-step)) / (xj+step - (xj-step))

fwd = forward(f, 2)
ctr = central(f, 2)

error = (ctr - fwd) / fwd  # Mistakenly multiplied by 100 here originally
```

### **Question 15**
> **Problem**
>"Newton's method for root finding is guaranteed to converge if the function is continuous."

**My answer:** True
✅ **Correct answer:** False 

Newton's method is not guaranteed to converge because it requires that f(x) must be differentiable, the initial guess must be sufficiently close to the actual root, and the derivative must not be zero near the root.