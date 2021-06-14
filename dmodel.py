import random as rd
from torchvision import models
import torch.nn as nn
import torch


class Lesions(object):
    lst = ["Actinic Keratosis",  "Basal Cell Carcinoma", "Seborrheic Keratosis",
           "Dermatofibroma", "Melanocytic Nevi",  "Melanoma", "Vascular Lesions"]

    def __init__(self):
        num_classes=7
        model_ft_1 = models.densenet121(pretrained=True)
        num_ftrs = model_ft_1.classifier.in_features
        model_ft_1.classifier = nn.Linear(num_ftrs, num_classes)
        model_1 = model_ft_1

        model_ft_3 = models.resnet50(pretrained=True)
        num_ftrs = model_ft_3.fc.in_features
        model_ft_3.fc = nn.Linear(num_ftrs, num_classes)
        model_3 = model_ft_3

        model_ft = models.vgg11_bn(pretrained=True)
        num_ftrs = model_ft.classifier[6].in_features
        model_ft.classifier[6] = nn.Linear(num_ftrs, num_classes)
        model_2 = model_ft

        class Ensemble(nn.module):
            def __init__(self, model_1, model_2, model_3):
                super(Ensemble, self).__init__()
                self.model_1 = model_1
                self.model_2 = model_2
                self.model_3 = model_3

            def forward(self, x):
                pred_1 = self.model_1(x)
                pred_2 = self.model_2(x)
                pred_3 = self.model_3(x)
                pred_sum = pred_1.add(pred_2)
                pred_sum = pred_sum.add(pred_3)
                avg = pred_sum / 3
                return avg, pred_1, pred_2, pred_3

        model = Ensemble(model_1, model_2, model_3)
        model.load_state_dict(torch.load('functioning.pth', map_location='cpu'), strict=True)
        model.eval()
