def groups(request):
    return {
        f'is_{group_name}_group': request.user.groups.filter(
            name=group_name).exists() if not request.user.is_superuser else True
        for group_name in ('trauma', 'tumor')
    }
