from django.shortcuts import render
import logging
# Create your views here.

logger = logging.getLogger('log')


def initial_page(request):
    logger.info("start!!!")
    return render(request, 'initial.html')