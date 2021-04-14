from wordmarker.contexts import Context
from wordmarker.loaders import YamlResourceLoader


class XmlContext(Context, YamlResourceLoader):
    def _init(self):
        pass
