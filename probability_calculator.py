import copy
import random

#logic from Beau for most part, code original+snippets from Beau
class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for item in kwargs.keys():
            for ball in range(kwargs[item]):
                self.contents.append(item)

    def draw(self, num_balls):
        num_balls = min(num_balls, len(self.contents))
        final_balls = []
        for drawing in range(num_balls):
            index_to_pop = random.randint(0, len(self.contents)-1)
            final_balls.append(self.contents.pop(index_to_pop))
        return final_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0
    
    for experiment in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        result = hat_copy.draw(num_balls_drawn)
        correct_result = 0   

        for color in expected_balls.keys():
            if result.count(color) >= expected_balls[color]:
                correct_result += 1

        if correct_result == len(expected_balls):
            num_success += 1

    probability = num_success/num_experiments

    return probability