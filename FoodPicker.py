# Author: Eric Fahy
# Created: 12/8/2020
# Last Modified 11/30/2020
# Description: This driver program is designed to help me and my girlfriend where to eat.
# A list of restaurants will be held in an array. The program will randomly pick one restaurant out of the list.
# If the user does not want the restaurant that was picked they can request another one. If a restaurant is not wanted
#  it will be removed from the pool of restaurants.

from random import randrange


# This function will return a random index from the list parameter
def random_index(list_length):
    return randrange(list_length)


# This function will return a random restaurant from the list parameter
def random_restaurant(res_list):
    return res_list[random_index(len(res_list))]


def main():
    restaurants = ["McDonalds", "In N Out", "Canes", "Peter Piper", "Barros", "Panda", "Shake Shack", "Jersey Mikes",
                   "Texas Roadhouse", "PF Changs"]

    choice = " "

    while choice.lower() != "y" and len(restaurants) != 0:  # Keep choosing restaurant until one is picked

        restaurant = random_restaurant(restaurants)

        print("Does " + str(restaurant) + " sound good?")

        choice = input("Y or N? \n")

        if choice.lower() != "y" and choice.lower() != "n":  # Sanitize input

            print("Please enter Y (Yes) or N (No). \n")

        if choice.lower() == "y":

            print("Enjoy!\n")

        elif choice.lower() == "n":

            restaurants.pop(restaurants.index(str(restaurant)))

            if len(restaurants) == 0:
                print("There are no more restaurants to pick from :( \n")


if __name__ == "__main__":
    main()
