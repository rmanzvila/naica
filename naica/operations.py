import statistics


def obtain_median(elements):
    """Function which return medium value"""
    if elements:
        return '{0:.2f}'.format(statistics.median(elements))
    return ''


def obtain_mean(elements):
    """Function which return arithmetic media"""
    if elements:
        return '{0:.2f}'.format(statistics.mean(elements))
    return ''


def obtain_mode(elements):
    """Function which return mode in case elements has one"""
    if not elements:
        return ''
    try:
        return statistics.mode(elements)
    except statistics.StatisticsError:
        return 'Existe más de 1 moda'


def obtain_average(elements, total_elements):
    """Function which return an average"""
    if elements:
        return '{0:.1%}'.format(elements / total_elements)
    return 0


def obtain_standart_dev(elements):
    """Function which return standard deviation"""
    if not elements or len(elements) < 2:
        return ''
    return '{0:.3f}'.format(statistics.stdev(elements))


def obtain_variance(elements, total_elements):
    """Function which return variance"""
    if not elements:
        return ''
    return '{0:.4f}'.format(statistics.variance(elements))
