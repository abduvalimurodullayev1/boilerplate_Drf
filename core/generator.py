from drf_yasg.generators import OpenAPISchemaGenerator


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        if request and request.is_secure():
            schema.schemes = ["https", "http"]
        else:
            schema.schemes = ["http", "https"]

        return schema
