"""Restaurant rating lister."""
scores = {}


def restaurant_ratings(filename):
    #key: restaurant
    #value: ratings
    for line in open(filename):
        restaurant, rating = line.rstrip().split(":")
        scores[restaurant] = rating
        # print(f"{restaurant} is rated at {ratings}.")


def add_rating():
    restaurant = input("Please enter the restaurant name? ")
    rating = False
    while rating == False:
        rating = validate_rating(input("Please enter the rating? "))
        print(rating)

    scores[restaurant] = rating


def show_ratings():
    for restaurant, rating in sorted(scores.items()):
        print(f"{restaurant} is rated at {rating}.")


def validate_rating(rating):
    try:
        rating = int(rating)
        if rating >= 1 and rating <= 5:
            return rating
        else:
            return False
    except:
        return False


add_rating()
restaurant_ratings('scores.txt')
show_ratings()
