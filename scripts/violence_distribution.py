'''
Alex Knowlton
3/21/2021

This file has functions analyzing the distribution and mapping of gun
violence over the us
'''

def distibution_overall(gun_data, us_map, log=False):
    '''
    breaks the gun dataset and us map into counties and breaks down the
    typical number of gun incidents by county, then returns a tuple of
    an altair histogram and the value of lambda. There is a parameter of
    whether or not to plot the x-axis on a log scale, defaults to false
    '''
    pass


def distribution_by_population(gun_data, us_map, population):
    '''
    attempts to normalize by population and repeat the breakdown of gun
    violence by county, returns an altair histogram and the value of lambda.
    There is a parameter of
    whether or not to plot the x-axis on a log scale, defaults to false
    '''
    pass


def dangerous_areas(gun_data, us_map):
    '''
    returns an altair chart of a centroid map of the violence across the US
    '''
    pass


def worst_areas(gun_data, us_map):
    '''
    returns an altair chart of of the outlying districts in the US, the ones
    past a certain value in the violence distribution
    '''
    pass