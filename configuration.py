# Dataset
DATA_DIR = "/content/data/"
PRISTINE_FOLDER = "Pristine"
FORGERED_FOLDER = "Forgered"
GROUND_TRUTH_FOLDER = "Ground_Truth"
DATASET_NAME = "CMFDdb_grip"
DATASET_DIR = '/content/drive/MyDrive/VisioPe_FinalProject/' 
DATASET_SIZE = 80
IMG_SHAPE = (1024,768)
IMG_CHANNELS = 3

# Training
TRAIN_SIZE = 50
VAL_SIZE = 10
TEST_SIZE = 20
BATCH_SIZE = 5
EPOCHES = 20

# Learning
MOMENTUM = 0.9
WEIGHT_DECAY = 0.0005
LEARNING_RATE = 0.1

# Noise and compression attacks
NOISE_VARIANCES = [0.002, 0.004, 0.006, 0.008, 0.01]

