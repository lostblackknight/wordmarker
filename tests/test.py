from wordmarker.loaders.default_resource_loader import DefaultResourceLoader

if __name__ == '__main__':
    loader = DefaultResourceLoader()
    resource = loader.get_resource("E:\PycharmProjects\wordmarker\data\hh")
    print(resource.get_file())
    print(resource.get_file_name())

    print(loader.load(resource))
