# food_informer
Allowing Dutch users to make unbiased cheap and healthy decisions.

## Introduction
Supermarkets are notorious for aggressive and confusing marketing tactics. This might
trick the customer into buying overly expensive or unhealthy food. Sadly it is made difficult
to make informed discicions about what to buy.

## Aim
This project aims to provide a crude insight into the nutricion to price relationship per
foodgroup. This is done by applying frequentist statistics to
the [NEVO](https://www.rivm.nl/en/dutch-food-composition-database/use-of-nevo-online/request-dataset) 
and retrieving the most significant products using the hidden jumbo api.

## Dependencies
This Project requires the following dependences to be installed using the followint pip command:
`pip install bokeh seaborn pandas panel matplotlib supermarktconnector scipy jupyter-notebook`

## Installation & running the project
1) Clone repository using `git clone https://github.com/jgray1996/food_informer`
2) Open a terminal in the cloned director
3) run `jupyter-notebook .`
4) run the cells
