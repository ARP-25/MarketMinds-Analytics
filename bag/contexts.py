def bag_contents(request):

    bag_items = [1]
    total = 0
    context = {
        'bag_items': bag_items,
        'total': total,
    }

    return context