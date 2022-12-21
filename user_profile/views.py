from django.shortcuts import render


def user_profile_page(request, user):
    """Function that render user profile page"""
    context = {'user': user}
    return render(request=request, template_name='user_profile.html', context=context)
