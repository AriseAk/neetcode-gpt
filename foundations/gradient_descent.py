class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        fx=init
        for _ in range(iterations):
            derivative=2*fx
            fx=fx-learning_rate*derivative
        return round(fx, 5)
        
