#@title
!git clone https://github.com/NVIDIA/apex.git
%cd apex
!pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" .
%cd ..

import torch
import apex
from fastai.text import *
import datetime
run_start_time = datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S')

LOG_PATH=Path('logs/')
MODEL_PATH=Path('models/')

if not LOG_PATH.exists():
  LOG_PATH.mkdir()
import logging

args = {
    "run_text": "my_test",
    "max_seq_length": 512,
    "do_lower_case": True,
    "train_batch_size": 16,
    "learning_rate": 6e-5,
    "num_train_epochs": 12.0,
    "warmup_proportion": 0.002,
    "local_rank": -1,
    "gradient_accumulation_steps": 1,
    "fp16": True,
    "loss_scale": 128
}

logfile = str(LOG_PATH/'log-{}-{}.txt'.format(run_start_time, args["run_text"]))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
    handlers=[
        logging.FileHandler(logfile),
        logging.StreamHandler(sys.stdout)
    ])

logger = logging.getLogger()

device = torch.device('cuda')

if torch.cuda.device_count() > 1:
    multi_gpu = True
else:
    multi_gpu = False