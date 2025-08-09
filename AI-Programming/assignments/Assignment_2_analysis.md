# Assignment_2 Analysis and SVM/MLP Explanation (English)

This Jupyter Notebook is a comprehensive assignment on machine learning and computer vision, focusing on the FashionMNIST dataset. It covers data preprocessing, visualization, classifiers (SVM and MLP), image processing (Sobel edge detection, bilateral filtering), and model evaluation. Detailed analysis is as follows:

---

## 1. Data Loading and Visualization
- Uses `mnist_reader` to load FashionMNIST training and test sets as `X_train, y_train, X_test, y_test`.
- Normalizes pixel values to the 0~1 range to speed up model training.
- Provides a `plot_random_images` function to randomly display training images, with options to show category labels or predictions.

## 2. Visualization of Training Images and Labels
- Randomly displays 5 training images, with the category name (e.g., T-shirt, Dress) as the title.

## 3. SVM Classifier
- Uses `sklearn.svm.SVC` with a linear kernel and regularization parameter C=0.025.
- If training on the full dataset is too slow, only the first 10,000 samples are used.
- After training, predicts on the test set and visualizes 5 samples as "predicted category (ground-truth category)".
- Outputs accuracy, classification report (precision, recall, f1-score), and confusion matrix.

### SVM (Support Vector Machine)
- Essence: Finds the optimal hyperplane to maximize the margin between different classes.
- Linear kernel is suitable for linearly separable data; C parameter controls the trade-off between margin and error.
- Pros: Performs well on small datasets and linear problems; clear decision boundaries.
- Cons: Limited scalability for large or nonlinear problems; slow training.

## 4. MLP Neural Network Classifier
- Uses `sklearn.neural_network.MLPClassifier` with max_iter=1000 and L2 regularization alpha=1.
- Trains first on 10,000 samples, then on the full dataset, comparing results.
- Also outputs prediction visualization and classification report.
- Compares MLP and SVM in terms of training time, accuracy, and metrics.

### MLP (Multi-Layer Perceptron)
- Essence: Multi-layer neural network capable of modeling complex nonlinear relationships.
- Uses hidden layers and activation functions for feature abstraction; L2 regularization prevents overfitting.
- Pros: Suitable for large datasets and nonlinear problems; strong expressive power; fast training.
- Cons: Many parameters, requires tuning, less interpretable.

## 5. Image Processing and Classification Comparison
- **Sobel Edge Detection**: Applies Sobel processing to training and test images to extract edge features, then classifies with MLP.
- **Bilateral Filtering**: Applies bilateral filtering (diameter 9, sigma=85) to original images, then classifies with MLP.
- Compares MLP training time, accuracy, and metrics for three feature types (original, Sobel, bilateral), finding Sobel features perform best.

## 6. Theory and Summary
- Explains the principles, pros, cons, and application scenarios of SVM and MLP.
- Discusses L1/L2 regularization and the advantages of MLP for nonlinear data.
- Briefly explains the principles and uses of Sobel and bilateral filtering.

## 7. Program Highlights and Applicability
- Clear code structure and detailed comments, covering the full process from data to model evaluation.
- Suitable as coursework or lab reference for machine learning, deep learning, and image processing courses.

---

### Summary
- The program covers the complete machine learning workflow: data preprocessing, visualization, SVM and MLP classification, image feature engineering (edges, filtering), and model evaluation/comparison.
- The code is well-structured and well-commented, making it easy to understand and extend.
- Suitable for coursework or lab reference in machine learning, deep learning, and image processing.

---

# Assignment_2 程序分析与SVM/MLP解释（中文）

这个Jupyter Notebook程序是一个典型的机器学习与计算机视觉综合作业，主要围绕FashionMNIST数据集，考察了数据预处理、可视化、分类器（SVM和MLP）、图像处理（Sobel边缘检测、双边滤波）等内容。下面是详细分析：

---

## 1. 数据加载与可视化
- 使用`mnist_reader`加载FashionMNIST训练和测试集，分别赋值为`X_train, y_train, X_test, y_test`。
- 对像素值归一化到0~1区间，加快模型训练。
- 提供了`plot_random_images`函数，支持随机展示训练集图片，并可显示类别标签或预测结果。

## 2. 可视化训练集图片及标签
- 随机展示5张训练集图片，并在标题上显示对应的类别名称（如T-shirt, Dress等）。

## 3. SVM分类器
- 使用`sklearn.svm.SVC`，线性核（linear kernel），正则化参数C=0.025。
- 若全量训练集训练过慢，可只用前10000个样本。
- 训练后在测试集上预测，并可视化5个样本的“预测类别（真实类别）”。
- 输出准确率、分类报告（precision, recall, f1-score）、混淆矩阵。

### SVM（支持向量机）
- 本质：寻找最优超平面，将不同类别样本最大间隔分开。
- 线性核适用于线性可分数据，C参数控制间隔与误差的权衡。
- 优点：对小样本、线性问题表现好，决策边界清晰。
- 缺点：对大样本、非线性问题扩展性有限，训练慢。

## 4. MLP神经网络分类器
- 使用`sklearn.neural_network.MLPClassifier`，最大迭代1000次，L2正则化系数alpha=1。
- 先用10000个样本训练，再用全部训练集训练，比较两者效果。
- 同样输出预测可视化和分类报告。
- 分析了MLP与SVM的区别，包括训练时间、准确率、各项指标对比。

### MLP（多层感知机）
- 本质：多层神经网络，能拟合复杂非线性关系。
- 通过隐藏层和激活函数实现特征抽象，L2正则化防止过拟合。
- 优点：适合大样本、非线性问题，表达能力强，训练速度快。
- 缺点：参数多，需调参，解释性弱。

## 5. 图像处理与分类对比
- **Sobel边缘检测**：对训练和测试图片分别做Sobel处理，提取边缘特征，再用MLP分类。
- **双边滤波**：对原始图片做双边滤波（直径9，sigma=85），再用MLP分类。
- 对比三种特征（原图、Sobel、双边滤波）下MLP的训练时间、准确率、各项指标，得出Sobel特征效果最好。

## 6. 理论与总结
- 解释了SVM和MLP的原理、优缺点、适用场景。
- 讨论了L1/L2正则化、非线性数据下MLP的优势。
- 对Sobel和双边滤波的原理和用途做了简要说明。

## 7. 程序亮点与适用性
- 代码结构清晰，注释详细，涵盖了从数据到模型评估的完整流程。
- 适合机器学习、深度学习、图像处理等课程作业或实验参考。

---

### 总结
- 该程序涵盖了数据预处理、可视化、SVM与MLP分类、图像特征工程（边缘、滤波）、模型评估与对比等完整机器学习流程。
- 代码结构清晰，注释详细，便于理解和扩展。
- 适合用于机器学习、深度学习、图像处理等课程的作业或实验参考。