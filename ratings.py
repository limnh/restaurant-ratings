"""Restaurant rating lister."""
def get_scores():
    
    restaurant_scores = open("scores.txt")
    scores = {}
    for line in restaurant_scores:
        line = line.rstrip()
        name, score = line.split(":")
        scores[name] = int(score)
    return scores

scores = get_scores()

def add_rating(scores):

    print("Hi! Tell us about your favorite restaurant!")
    restaurant = input("What the name of the restaurant? ")
    rating = int(input("How do you rate it? "))

    scores[restaurant] = rating

    return add_rating



def print_full_scores(scores):
    
    for name, score in sorted(scores.items()):
        print(f"{name} has a rating of {score}.")

add_rating(scores)
print_full_scores(scores)