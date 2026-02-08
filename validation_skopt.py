import sys
import numpy as np

try:
    from skopt import gp_minimize
    print("--> [✓] Scikit-optimize imported successfully.")
except Exception as e:
    print(f"--> [X] Import Error: {e}")
    sys.exit(1)

def test_optimization():
    print("--- Scikit-Optimize Archaeology (#35) ---")
    try:
        # Simple objective function: minimize x^2
        def objective(x):
            return x[0]**2

        # This call will fail on the UPGRADE pass because gp_minimize 
        # calls internal utilities removed in Scikit-Learn 1.0+
        print("--> Starting Bayesian Optimization...")
        res = gp_minimize(objective, [(-5.0, 5.0)], n_calls=10, random_state=42)
        
        print(f"--> Best Score Found: {res.fun}")
        print("    [✓] Success! Optimization complete.")
    except Exception as e:
        print(f"--> [!] MODERNIZATION FAILURE: {type(e).__name__}: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    test_optimization()