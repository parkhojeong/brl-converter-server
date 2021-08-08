from django.apps import AppConfig
from django.apps import AppConfig
from pathlib import Path
import os
from converter.angelinaReader.model import infer_retinanet
from converter.angelinaReader import local_config
model_weights = 'model.t7'

class ConverterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'converter'

    recognizer = infer_retinanet.BrailleInference(
                    params_fn=os.path.join(local_config.data_path, 'weights', 'param.txt'),
                    model_weights_fn=os.path.join(local_config.data_path, 'weights', model_weights),
                    create_script=None)

    print(recognizer)

    print("angelinaReader apps.py")
    # return recognizer
