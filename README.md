# Socratic-Sorting-Algorithm-Assistant (Image Classifier using Generative AI)

**Tagline:** Empowering Image Recognition with Generative AI

## Project Overview

This project leverages Generative AI to build a robust image classifier capable of learning from large datasets and making highly accurate predictions. By utilizing deep learning models like Convolutional Neural Networks (CNNs), the classifier autonomously learns features from images, reducing the need for manual feature engineering. This makes it adaptable to various domains and scalable for complex datasets. Additionally, by employing pre-trained models and fine-tuning them, the project demonstrates the flexibility of Generative AI in solving classification challenges.

## Project Structure

```
├── saved_models
│   └── checkpoint.pth
├── images
│   └── <test_images>
├── utils
│   ├── load_my_model.py
│   ├── pre_process.py
│   ├── my_label_mapping.py
├── predict.py
├── train.py
├── requirements.txt
├── README.md
```

## How the Project Solves the Challenge

Generative AI is ideal for this image classification challenge because it excels at learning intricate patterns from data, allowing for accurate generalizations to unseen images. By using deep learning architectures like CNN, the model automatically extracts relevant features, eliminating manual feature engineering. This solution is both flexible and scalable, adapting to different categories and making it easy to handle complex datasets.

## In-Scope

- **Training & Prediction:** The project includes both training the model and predicting image classes using pre-trained checkpoints.
- **Generative AI Models:** Fine-tuning of pre-trained generative models for improved accuracy.
- **Top-K Predictions:** The model returns the top K most likely classes for each input image.
- **GPU Support:** The project includes GPU acceleration to speed up training and inference.

## Out of Scope

- **Real-time Deployment:** While the model works in a standalone environment, deployment into a real-time system is out of scope.
- **Large-Scale Dataset Handling:** The project does not include optimization for handling extremely large datasets beyond what fits in memory.
  
## Future Opportunities

- **Real-time Application:** Future iterations could deploy the model to web services or mobile applications for real-time image recognition.
- **Multi-Class Detection:** The model could be extended to detect multiple objects in a single image.
- **Integration with AutoML:** AutoML techniques could be used for model optimization and automated hyperparameter tuning.

## Technologies Used

PyTorch, Python, Torchvision, OpenCV, NumPy, Matplotlib, argparse, CNN, Generative AI, Jupyter Notebook

## Challenges I Ran Into

One of the main challenges faced during the project was handling the error when loading the model checkpoint. Initially, the model checkpoint could not be found or loaded due to incorrect file paths or issues with the model's saved format. To resolve this, the path handling for loading the checkpoint was updated, and a manual inspection of the checkpoint file was conducted to ensure compatibility with the PyTorch framework. Additionally, processing the input image tensor caused dimensional errors when feeding the image into the model. The image preprocessing function was corrected to format the image properly by using `unsqueeze()` to add the batch dimension. Another hurdle was ensuring that the model utilized GPU for faster computations when available, which required appropriate handling of CUDA devices.

## How to Use

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-repo/image-classifier.git
   cd image-classifier
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Training the Model:**

   ```bash
   python train.py --data_dir <path_to_dataset> --gpu
   ```

4. **Predicting Image Classes:**

   ```bash
   python predict.py <path_to_image> <path_to_checkpoint> --top_k 5 --category_names cat_to_name.json --gpu
   ```

5. **Directory Structure:**

   - `saved_models/checkpoint.pth`: The pre-trained model checkpoint.
   - `utils/`: Contains utility scripts for model loading, preprocessing, and label mapping.
   - `predict.py`: Script for predicting image classes.
   - `train.py`: Script for training the model.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

