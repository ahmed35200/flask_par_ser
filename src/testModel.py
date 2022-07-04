from src.model_fetch import modelImageFetch

def testModel(link):
    classes_x = modelImageFetch(link, "cnn.h5", 224, 224)

    return classes_x