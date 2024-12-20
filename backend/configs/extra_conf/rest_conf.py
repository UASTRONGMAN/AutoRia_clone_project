REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer',],
    'DEFAULT_PAGINATION_CLASS': 'core_app.pagination.PageNumberPagination',
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework_simplejwt.authentication.JWTAuthentication',),
    'DEFAULT_PERMISSION_CLASSES': ['core_app.permissions.is_superuser_permission.IsSuperUser',],
    'EXCEPTION_HANDLER': 'core_app.handlers.error_handler.error_handler',
}
