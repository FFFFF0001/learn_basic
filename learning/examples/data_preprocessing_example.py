from Helper import DataPreprocessing

# demo = DataPreprocessing()
# demo.readSimpleDataSet("pca_dataset.txt", demo.ND_MAT, demo.FLOAT, "\t")
# demo.graph2D(color="#9AB4FF")
# result = demo.pca(1)
# demo.graph2D()
# demo.showGraph()


# demo = DataPreprocessing()
# demo.readParagraph("paragraph_eng.txt")
# dictionary, dictMat = demo.wordBagging(demo.ENGLISH, demo.ND_MAT, lambda x: len(x) > 2)
# print(dictMat.shape)

demo = DataPreprocessing()
demo.readParagraph("paragraph_chi.txt")
dictionary, dictMat = demo.wordBagging(demo.CHINESE, demo.ND_MAT, lambda x: len(x) > 2)
print(dictMat.shape)