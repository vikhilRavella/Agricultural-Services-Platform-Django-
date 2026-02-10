def demo_context(request):
    return {
        'demo': request.session.get('demo', False)
    }
