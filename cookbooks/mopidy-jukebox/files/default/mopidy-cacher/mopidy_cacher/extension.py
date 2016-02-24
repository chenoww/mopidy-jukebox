import os

from mopidy import config, ext

class CacherExtension(ext.Extension):
    dist_name = 'Mopidy-Cacher'
    ext_name = 'cacher'

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(CacherExtension, self).get_config_schema()
        return schema

    def get_command(self):
        from .cache import CacherCommand
        return CacherCommand(self)

    def setup(self, registry):
        pass
        #from .backend import CacherBackend
        #registry.add('backend', CacherBackend)

        # TODO: Edit or remove entirely
        #registry.add('http:static', {
        #    'name': self.ext_name,
        #    'path': os.path.join(os.path.dirname(__file__), 'static'),
        #})

        from .frontend import cacher_app_factory

        registry.add('http:app', {
            'name': self.ext_name,
            'factory': cacher_app_factory,
        })
