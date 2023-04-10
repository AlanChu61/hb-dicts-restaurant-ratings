"""Restaurant rating lister."""
scores = {}


def restaurant_ratings(filename):
    #key: restaurant
    #value: ratings
    for line in open(filename):
        restaurant, ratings = line.rstrip().split(":")
        scores[restaurant] = ratings
        # print(f"{restaurant} is rated at {ratings}.")


def add_ratings():
    restaurant = input("Please enter the restaurant name? ")
    ratings = input("Please enter the rating? ")
    scores[restaurant] = ratings


def show_ratings():
    for restaurant, ratings in sorted(scores.items()):
        print(f"{restaurant} is rated at {ratings}.")


add_ratings()
restaurant_ratings('scores.txt')
show_ratings()
