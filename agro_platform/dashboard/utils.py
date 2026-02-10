def is_demo(request):
    return request.session.get('demo', False)
