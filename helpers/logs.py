# copy record then remove the table field
def to_log(from_obj, to_model, deleted_related_obj=None, is_delete=True):
    to_obj = to_model()
    for field in from_obj.__dict__.keys():
        to_obj.__dict__[field] = from_obj.__dict__[field]

    # relate to deleted_related_obj if exists in param
    if deleted_related_obj is not None:
        to_obj.__dict__[deleted_related_obj['key']] = deleted_related_obj['value']

    to_obj.save()

    if is_delete == True:
        from_obj.delete()

    return to_obj
