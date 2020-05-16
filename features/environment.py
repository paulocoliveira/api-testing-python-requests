def before_feature(context, feature):
    context.base_url = context.config.userdata['base_url']