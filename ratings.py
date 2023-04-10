"""Restaurant rating lister."""
from random import choice
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


def update_ratings():
    restaurant = choice(list(scores.keys()))
    print(f"{restaurant} is rated at {scores[restaurant]}.")
    rating = False
    while rating == False:
        rating = validate_rating(input("Please enter the rating? "))
    scores[restaurant] = rating


def main():
    restaurant_ratings('scores.txt')
    command = input(
        'Please enter a command: Show, Add, Update or Quit? ').capitalize()

    while command != 'Quit':
        if command == 'Show':
            show_ratings()
        elif command == 'Add':
            add_rating()
        elif command == 'Update':
            update_ratings()
        command = input(
            'Please enter a command: Show, Add, Update or Quit? ').capitalize()
    print('Goodbye!')


if __name__ == '__main__':
    main()
