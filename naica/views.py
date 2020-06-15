from django.shortcuts import render, redirect

from naica.forms import PollForm
from naica.models import Poll
from naica.operations import *


def poll_list_view(request):
    """Render view to list polls"""
    polls = Poll.objects.all()
    front_elements = get_dashboard(polls)
    return render(request, 'list_poll.html', front_elements)


def poll_new_view(request):
    """Render view to create and save a poll"""
    if request.method == "POST":
        form = PollForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('polls')
    else:
        form = PollForm()
    return render(request, 'new_poll.html', {'form': form})


def get_dashboard(polls):
    """Obtain data to show on view"""
    results = general_operations(polls)
    results = apply_operations(polls.filter(financial_goals=True), polls.count(), results, 'financial')
    results = apply_operations(polls.filter(investment_knowledge=True), polls.count(), results, 'investment')
    return results


def general_operations(polls):
    """General operations with all data"""
    results = {}
    total_polls = polls.count()

    results['polls'] = polls
    results['counter'] = total_polls
    results['age_median'] = obtain_median(polls.values_list('age', flat=True))
    results['age_arithmetic_median'] = obtain_mean(polls.values_list('age', flat=True))
    results['age_mode'] = obtain_mode(polls.values_list('age', flat=True))
    results['savings_median'] = obtain_mean(polls.values_list('savings', flat=True))

    results['m_average'] = obtain_average(polls.filter(sex='M').count(), total_polls)
    results['f_average'] = obtain_average(polls.filter(sex='F').count(), total_polls)
    results['o_average'] = obtain_average(polls.filter(sex='O').count(), total_polls)

    return results


def apply_operations(polls, total_polls, results, topic):
    """Generic function to receive filtered data and calculate operations, add tu result dict all data"""
    counter = polls.count()
    results[topic+"_average"] = obtain_average(counter, total_polls)
    results[topic+"_variance".format(topic)] = obtain_variance(polls.values_list('savings', flat=True), counter)
    results[topic+"_savings_stdev".format(topic)] = obtain_standart_dev(polls.values_list('savings', flat=True))
    results[topic+"_m_average".format(topic)] = obtain_average(polls.filter(sex='M').count(), counter)
    results[topic+"_f_average".format(topic)] = obtain_average(polls.filter(sex='F').count(), counter)
    results[topic+"_o_average".format(topic)] = obtain_average(polls.filter(sex='O').count(), counter)
    return results

